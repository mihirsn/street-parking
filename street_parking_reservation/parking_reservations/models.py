from django.db import models

class ParkingSpot(models.Model):
    TWO_WHEELER = 2
    FOUR_WHEELER = 4
    VEHICLE_TYPE = [
        (TWO_WHEELER, 'Two-wheeler'),
        (FOUR_WHEELER, 'Four-wheeler'),
    ]
    latitude = models.FloatField()
    longitude = models.FloatField()
    cost = models.FloatField()
    spot_type = models.IntegerField(
        choices=VEHICLE_TYPE,
        default=FOUR_WHEELER,
    )

class Reservation(models.Model):
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    vehicle_no = models.CharField(max_length=128)
    created_on = models.DateTimeField(auto_now_add=True)

