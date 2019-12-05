from django.conf.urls import url

from .views import StatusListSearchAPIView


urlpatterns = [
    url(r'^$', StatusListSearchAPIView.as_view()),
]
