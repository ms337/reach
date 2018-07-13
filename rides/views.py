from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import APIViews
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PlaceSerializer, ProfileSerializer, RidePostingSerializer, RideRequestSerializer
from .permissions import IsOwnerOrReadOnly

#User does not need to be signed in (authenticated) to access this view
class RidePostingReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RidePosting.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)#This will need to be changed to implement social auth
    permission_classes = (AllowAny,)
    serializer_class = RidePostingSerializer

#User needs to be signed in (authenticated) to use this create view
class RidePostingCreateAPIView(CreateAPIView):
    queryset = RidePosting.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = RidePostingSerializer

#User must be owner to perform PUT or DELETE requests
class RidePostingRUDAPIView(RetriveUpdateDestroyAPIView):
    queryset = RidePosting.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = RidePostingSerializer

class RideRequestReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RideRequest.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)
    serializer_class = RideRequestSerializer

class RideRequestCreateAPIView(CreateAPIView):
    queryset = RideRequest.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = RideRequestSerializer

class RideRequestRUDAPIView(RetriveUpdateDestroyAPIView):
    queryset = RideRequest.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = RideRequestSerializer

class ProfileReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)
    serializer_class = RideRequestSerializer

class ProfileCreateAPIView(CreateAPIView):
    queryset = Profile.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = RideRequestSerializer

class ProfileRUDAPIView(RetriveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = RideRequestSerializer

