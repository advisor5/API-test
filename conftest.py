import pytest
import json
import random
import string
import pytz
from src.user.routes import ApiLogin
from src.data.constants import UserData, Parameters


@pytest.fixture
def generate_update_date():
    letters = string.hexdigits
    digits = string.digits
    time_zone = pytz.all_timezones
    random_string = ''.join(random.choice(letters) for _ in range(6))
    random_digits = ''.join(random.choice(digits) for _ in range(3))
    random_time_zone = ''.join(random.choice(time_zone) for _ in range(1))
       
    update_user_data = { 
        "name": {random_string},
        "time_zone": {random_time_zone},
        "sip_number": {random_digits},
        "sip_extension": "22344", 
        "events_view_type": 1,
        "locale": "ru"
        }
    return update_user_data

@pytest.fixture
def auth_user():
    data = UserData.USER
    payload = json.dumps(data)
    
    headers = Parameters.HEADERS
    response = ApiLogin().login_user(payload, headers)
    token = response.json()["token"]    
    return token
