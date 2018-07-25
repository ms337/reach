from rest_framework import serializers
from .models import Place, Profile, RideRequest, RidePosting

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('city',)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('email','name','user','age','rating','num_ratings','num_rides','friendlist','phone_num')

class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = ('__all__')

class RidePostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RidePosting
        fields = ('__all__')
        
class RidePostingAcceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = RidePosting
        fields = ('seats_left','confirmed_riders')
