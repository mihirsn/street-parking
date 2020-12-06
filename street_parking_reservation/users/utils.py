import requests
from requests.exceptions import HTTPError
from django.conf import settings
from .users_exceptions import PhoneNumberException

def validate_phone_number(phone_number):
    try:
        url = f'{settings.NUMVERIFY_URL}?access_key={settings.NUMVERIFY_ACCESS_KEY}&number={phone_number}&country_code={settings.NUMVERIFY_COUNTRY_CODE}&format=1'
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        raise PhoneNumberException(http_err)
    except Exception as err:
        print(f'Other error occurred: {err}')
        raise PhoneNumberException(err)
    else:
        response_json = response.json()
        return response_json