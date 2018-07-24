from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import APIViews
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PlaceSerializer, ProfileSerializer, RidePostingSerializer, RideRequestSerializer, RidePostingAcceptSerializer
from .permissions import IsOwnerOrReadOnly
from .models import RidePosting, RideRequest, Profile

#User does not need to be signed in (authenticated) to access this view
class RidePostingReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RidePosting.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)#This will need to be changed to implement social auth
    permission_classes = (AllowAny,)
    serializer_class = RidePostingSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `price` query parameter in the URL.
        """
        queryset = RidePosting.objects.all()
        desired_price = self.request.query_params.get('price', None)
        desired_seats = self.request.query_params.get('seats', None)
        if desired_price is not None:
            queryset = queryset.filter(price__lte= desired_price)
        if desired_seats is not None:
            queryset = queryset.filter(seats_left__gte=desired_seats)

        return queryset

#User needs to be signed in (authenticated) to use this create view
class RidePostingCreateAPIView(APIViews.CreateAPIView):
    queryset = RidePosting.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = RidePostingSerializer

#User must be owner to perform PUT or DELETE requests
class RidePostingRUDAPIView(APIViews.RetrieveUpdateDestroyAPIView):
    queryset = RidePosting.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = RidePostingSerializer

class RidePostingAcceptView(APIViews.RetrieveUpdateAPIView):
    queryset = RidePosting.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = RidePostingAcceptSerializer

class RideRequestReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RideRequest.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)
    serializer_class = RideRequestSerializer

class RideRequestCreateAPIView(APIViews.CreateAPIView):
    queryset = RideRequest.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = RideRequestSerializer

class RideRequestRUDAPIView(APIViews.RetrieveUpdateDestroyAPIView):
    queryset = RideRequest.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = RideRequestSerializer

class ProfileReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)
    serializer_class = RideRequestSerializer

class ProfileCreateAPIView(APIViews.CreateAPIView):
    queryset = Profile.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = RideRequestSerializer

class ProfileRUDAPIView(APIViews.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = RideRequestSerializer
