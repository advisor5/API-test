import os


class Url:
    HOST = os.environ.get('HOST_API')

class UserAPI:
    LOGIN = "/api/v1.00/public/login"
    SETTINGS = "/api/v1.00/public/user/settings"
    
class Parameters:
    HEADERS = {"Content-type": "application/json"}

class StatusCode:
    OK_200 = 200
    UNAUTHORIZED_401 = 401
    UNPROCESSABLE_ENTITY_422 = 422

class MessageText:
    MESSAGE_IF_WRONG_BODY = "Invalid username or password."
    TYPE_ERROR_NAME = "name"
    TYPE_ERROR_TIMEZONE = "time_zone"
    TYPE_ERROR_EVENTS = "events_view_type"
    ERROR_NAME = "The Name and Surname field is required."
    ERROR_TIMEZONE = "The User’s time zone field is required."
    ERROR_EVENTS = "The Events list visualization type field is required."
    ERROR_EVENTS_INVALID = "The Events list visualization type is invalid."

class UserData:
    EMAIL = os.environ.get('EMAIL')
    PASSWORD = os.environ.get('PASSWORD')
    TOKEN = "token"
    ERROR = "errors"
    
    USER = {
        "email": EMAIL,
        "password": PASSWORD
        }

    USER_WHITH_WRONG_PASS = {
        "email": EMAIL,
        "password": "12345"
        }
    
    USER_WHITH_WRONG_EMAIL = {
        "email": "wrong@demo.ru",
        "password": PASSWORD
        }

    USER_DATA_WITHOUD_NAME = {
        "time_zone": "Europe/Moscow",
        "sip_number": "123", 
        "sip_extension": "22344", 
        "events_view_type": 1,
        "locale": "ru"
        }
    
    USER_DATA_WITHOUD_TIME_ZONE= { 
        "name": "IVAN Ivanov",
        "sip_number": "123", 
        "sip_extension": "22344", 
        "events_view_type": 1,
        "locale": "ru"
        }

    USER_DATA_WITHOUD_EVENTS = { 
        "name": "IVAN Ivanov",
        "time_zone": "Europe/Moscow",
        "sip_number": "123", 
        "sip_extension": "22344",
        "locale": "ru"
        }
