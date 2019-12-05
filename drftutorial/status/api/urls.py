from django.conf.urls import url

from .views import StatusListSearchAPIView
from .views import StatusAPIView, StatusCreateAPIView, StatusDetailAPIView


urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^create/$', StatusCreateAPIView.as_view()),
    url(r'^(?P<pk>.*)/$', StatusDetailAPIView.as_view()),
]
