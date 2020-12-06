from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from .serializers import UsersSerializer

@api_view(['GET', 'POST'])
def get_post_users(request):
    # get all users
    if request.method == 'GET':
        puppies = Users.objects.all()
        serializer = UsersSerializer(puppies, many=True)
        return Response(serializer.data)
    # insert a new record for a user
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'phone_number': request.data.get('phone_number')
        }
        serializer = UsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)