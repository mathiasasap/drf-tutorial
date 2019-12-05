from django.conf.urls import url

from .views import StatusListSearchAPIView
from .views import StatusAPIView, StatusDetailAPIView


urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$', StatusDetailAPIView.as_view()),
]
