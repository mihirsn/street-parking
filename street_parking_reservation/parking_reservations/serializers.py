from rest_framework import serializers
from .models import ParkingSpot


class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = ('id','latitude', 'longitude', 'cost', 'spot_type', 'status')