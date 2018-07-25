from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .import views


# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^ridepostings/create/$',
        views.RidePostingCreateAPIView.as_view()),
    url(r'^ridepostings/(?P<pk>[0-9]+)/edit/$',
        views.RidePostingRUDAPIView.as_view()),
    url(r'^ridepostings/(?P<pk>[0-9]+)/accept/$',
        views.RidePostingAcceptView.as_view()),
    url(r'^ridepostings/$',
        views.RidePostingListView.as_view()),
    url(r'^places/create/$',
        views.PlaceCreateView.as_view()),
])
