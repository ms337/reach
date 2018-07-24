from django.db import models
from django.contrib.auth.models import User
from django.db.models.manager import Manager
#from django.contrib.gis.db import models as geomodels
from django.db.models import Manager as GeoManager
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Place(models.Model):
    city = models.CharField(max_length=255)
    location = LocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0))
    objects = GeoManager()

    def __str__(self):
        return self.city + "at" + self.location

class Profile(models.Model):
    user = models.OneToOneField(User, related_name= 'person', unique = True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=25, unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    rating = models.FloatField(default= 5.0)
    num_rides = models.IntegerField(default=0)
    friendlist = models.ManyToManyField(User)
    phone_num = models.BigIntegerField(blank=True, null = True, unique= True)
    #is_active = models.BooleanField(default=True)
    #is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.name + 'with email: ' + self.email

class RidePosting(models.Model):
    dest = models.ForeignKey(Place,related_name="rides_from",on_delete=models.CASCADE)
    start =  models.ForeignKey(Place, related_name="rides_to",on_delete=models.CASCADE)

    driver = models.ForeignKey(User,related_name = "RidePosts",on_delete=models.CASCADE)

    date = models.DateField(db_index=True)
    time_min = models.TimeField(db_index=True)
    time_max = models.TimeField(db_index=True, default=time_min)

    price = models.FloatField()
    seats = models.IntegerField()
    description = models.TextField(blank=True)

    confirmed_riders = models.ManyToManyField(User, related_name = "Rides")
    potential_riders = models.ManyToManyField(User, related_name = "Ride_Offers")

    stops = ArrayField(base_field=models.CharField(max_length=30), size = 100)

    #objects = RidePostingManager()

    #REQUIRED_FIELDS = ['dest','start','date','time_min','price','seats']

    def __str__(self):
        return self.dest +self.start +self.date +self.driver

class RideRequest(models.Model):
    dest = models.ForeignKey(Place, related_name= 'destination', verbose_name= "Destination", on_delete= models.CASCADE)
    start = models.ForeignKey(Place, related_name= 'start', verbose_name= "Starting city",  on_delete= models.CASCADE)
    date = models.DateField(db_index= True)

    time_min = models.TimeField()
    time_max = models.TimeField()

    #timeInRange = (models.TimeField, models.TimeField)
    seatsNeeded = models.IntegerField(default= 1)
    rider = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= "The rider taking the ride", related_name= "riderrequests") # check related_name. Is supposed to create a reverse relationship where riderrequests.all will return all rider all instances of RideRequests it is linked to.
    #flexibleTime = models.BooleanField(default= False)
    #currentlyRequestedList = models.ManyToManyField(null=True, blank=True, symmetrical= False)
    requestCompleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.dest + "to" + self.start + "by" + self.user + "on" + self.date + "at" + self.timeInRange)
