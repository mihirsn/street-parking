from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from .serializers import UsersSerializer
from .utils import validate_phone_number
from .users_exceptions import PhoneNumberException

@api_view(['GET', 'POST'])
def get_post_users(request):
    try:
        # get all users
        if request.method == 'GET':
            users = Users.objects.all()
            serializer = UsersSerializer(users, many=True)
            return Response(serializer.data)
        # insert a new record for a user
        if request.method == 'POST':
            data = {
                'name': request.data.get('name'),
                'phone_number': request.data.get('phone_number')
            }
            validation_response = validate_phone_number(data['phone_number'])
            if 'valid' in validation_response and validation_response['valid']:
                serializer = UsersSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                raise PhoneNumberException(validation_response)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except PhoneNumberException as err:
        print(f'{err}')
        error = {'message': 'Invalid phone number'}
        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)