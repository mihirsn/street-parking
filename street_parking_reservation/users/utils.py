import logging

import requests
import re
from django.conf import settings
from requests.exceptions import HTTPError

from .users_exceptions import PhoneNumberException

logger = logging.getLogger(__name__)

def valid_password(password):
    return re.fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$", password)
    
def validate_phone_number(phone_number):
    try:
        logger.info("Validating phone number")
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
