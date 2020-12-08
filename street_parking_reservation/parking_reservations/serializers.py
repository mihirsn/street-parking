from rest_framework import serializers
from .models import ParkingSpot
from users.serializers import UsersSerializer


class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = ('id','latitude', 'longitude', 'cost', 'spot_type', 'status')

class ReservationSerializer(serializers.ModelSerializer):
    user = UsersSerializer
    spot = ParkingSpotSerializer
    vehicle_no = serializers.CharField(max_length = 128, required = True)
    created_on = serializers.DateTimeField()