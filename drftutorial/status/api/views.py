from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication
from django.shortcuts import get_object_or_404
import json
from utils.json import is_json

from status.models import Status
from .serializers import StatusSerializer


# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)


# CreateModelMixin --- post data
# UpdateModelMixin --- put data
# DestroyModelMixin --- delete data


# Login required mixin / decorator
class StatusAPIView(
    mixins.CreateModelMixin,
    generics.ListAPIView
):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [SessionAuthentication]
    # Commented because they are the default permission and auth classes defined in restconf folder
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        # print(request.user)
        qs = Status.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        print(body_)
        if is_json(body_):
            print("Is json")
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)
        # request.data
        passed_id = url_passed_id or new_passed_id or None
        print(passed_id)
        if passed_id is not None:
            return self.retrieve(self, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StatusAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Equivalent to the bellow class
# class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

# class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id' # To define which url argument use
#
#     # def get_object(self, *args, **kwargs):
#     #     kwargs = self.kwargs
#     #     kw_id = kwargs.get('id')
#     #     return Status.objects.get(id=kw_id)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)






