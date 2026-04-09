from . import models
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = ('id', 'title', 'price', 'inventory')
        

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = ('id', 'name', 'no_of_guest', 'bookingDate')
        extra_kwargs = {' no_of_guest': {'max value': 10, 'min value': 2}}
