from rest_framework.views import APIView
from rest_framework.response import Response

from drftutorial.status.models import Status
from .serializers import StatusSerializer


class StatusListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        return Response(qs)
