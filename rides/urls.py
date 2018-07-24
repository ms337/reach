from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'ridepostings', views.RidePostingReadOnlyViewSet)
# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^ridepostings/create/$',
        views.RidePostingCreateAPIView.as_view()),
    url(r'^ridepostings/(?P<pk>[0-9]+)/edit/$',
        views.RidePostingRUDAPIView.as_view()),
    url(r'^ridepostings/(?P<pk>[0-9]+)/accept/$',
        views.RidePostingAcceptView.as_view()),
    url(r'^', include(router.urls))
])
