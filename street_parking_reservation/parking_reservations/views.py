import math
from datetime import datetime, timezone

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import Users

from .models import ParkingSpot, Reservation
from .serializers import ParkingSpotSerializer

from .utils import find_spots_in_radius


# Create your views here.
@api_view(['POST'])
def add_parking_spots(request):
    if request.method == 'POST':
        data = {
            'latitude': request.data.get('latitude'),
            'longitude': request.data.get('longitude'),
            'cost': request.data.get('cost'),
            'spot_type': request.data.get('spot_type'),
        }
        serializer = ParkingSpotSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_available_spots(request):
    try:
        if request.method == 'GET':
            available_spot = ParkingSpot.objects.filter(status='A')
            serializer = ParkingSpotSerializer(available_spot, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(f'{err}')
        return Response(err, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_all_reserved_spots(request):
    try:
        if request.method == 'GET':
            available_spot = ParkingSpot.objects.filter(status='R')
            serializer = ParkingSpotSerializer(available_spot, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(f'{err}')
        return Response(err, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def reserve_a_spot(request):
    try:
        if request.method == 'POST':
            spot = request.data.get('spot_id')
            user = request.data.get('user_id')
            vehicle_no = request.data.get('vehicle_no')
            user_obj = Users.objects.filter(id=user)
            spot_obj = ParkingSpot.objects.filter(id=spot)
            if (
                spot_obj.count() == 1
                and user_obj.count() == 1
                and spot_obj[0].status == 'A'
            ):
                spot_obj = spot_obj[0]
                spot_obj.status = 'R'
                spot_obj.save()
                serializer_spot = ParkingSpotSerializer(spot_obj)
                reservation = Reservation.objects.create(
                    user=user_obj[0], parking_spot=spot_obj, vehicle_no=vehicle_no
                )
                reservation.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(f'{err}')
        return Response(err, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def cancel_a_spot(request):
    try:
        if request.method == 'PUT':
            spot = request.data.get('spot_id')
            user = request.data.get('user_id')
            vehicle_no = request.data.get('vehicle_no')
            user_obj = Users.objects.filter(id=user)
            spot_obj = ParkingSpot.objects.filter(id=spot)
            if (
                spot_obj.count() == 1
                and user_obj.count() == 1
                and spot_obj[0].status == 'R'
            ):
                spot_obj = spot_obj[0]
                spot_obj.status = 'A'
                spot_obj.save()
                Reservation.objects.filter(user=user).filter(parking_spot=spot).delete()
                return Response(status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(f'{err}')
        return Response(err, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def show_cost(request):
    try:
        if request.method == 'POST':
            spot = request.data.get('spot_id')
            user = request.data.get('user_id')
            reservation_obj = Reservation.objects.filter(user=user).filter(
                parking_spot=spot
            )
            spot_obj = ParkingSpot.objects.filter(id=spot)

            reservation_datetime = reservation_obj[0].created_on
            current_datetime = datetime.now(timezone.utc)
            reservation_time = current_datetime - reservation_datetime
            reservation_time_in_hrs = math.ceil(reservation_time.total_seconds() / 3600)
            print(f"diff array:{reservation_time}")
            print(f"duration of reservation:{reservation_time_in_hrs}")

            total_cost = reservation_time_in_hrs * spot_obj[0].cost
            return Response({'reservation_cost': total_cost}, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(f'{err}')
        return Response(err, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def get_spots_by_radius(request):
    try:
        if request.method == 'POST':
            latitude = request.data.get('latitude')
            longitude = request.data.get('longitude')
            radius = request.data.get('radius')
            vehicle_type = request.query_params.get('vehicle_type', None)

            available_spots = ParkingSpot.objects.filter(status='A').filter(spot_type=vehicle_type) if vehicle_type else ParkingSpot.objects.filter(status='A')
            serializer = ParkingSpotSerializer(available_spots, many=True)

            if len(serializer.data) > 0:
                available_spots_in_radius = find_spots_in_radius(serializer.data, latitude = latitude, longitude = longitude, radius = radius)
                print("found spots")
                return Response({"spots": available_spots_in_radius}, status=status.HTTP_200_OK)
            else:
                error = {'message': f"No available spots from your location within {radius}km of radius"}
                return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as err:
        print(f'{err}')
        return Response(err, status=status.HTTP_500_INTERNAL_SERVER_ERROR)