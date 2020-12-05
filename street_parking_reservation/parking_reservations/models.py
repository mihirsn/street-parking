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
    spot_type = models.IntegerField(
        choices=VEHICLE_TYPE,
        default=FOUR_WHEELER,
    )
    #categories = models.ManyToManyField('Category', related_name='posts')
