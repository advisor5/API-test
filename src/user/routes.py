import allure
import requests
from src.data.constants import Url, UserAPI, Parameters


class ApiLogin:
    def login_user(self, json, headers):
        with allure.step("POST запрос на ручку '/api/v1.00/public/login' - авторизация пользователя"):
            return requests.post(f"{Url.HOST}{UserAPI.LOGIN}", json, headers=headers)
    
    def update_user(self, json, token):
        with allure.step("PUT запрос на ручку 'api/v1.00/public/user/settings' - изменение данных"):
            allure.dynamic.description(f"Request body: {json}")
            headers = Parameters.HEADERS
            headers = {"Authorization": f"Bearer {token}"}
            return requests.put(f"{Url.HOST}{UserAPI.SETTINGS}", json, headers=headers)
    
    def get_user(self, token):
        with allure.step("GET запрос на ручку 'api/v1.00/public/user/settings' - изменение данных"):
            headers = Parameters.HEADERS
            headers = {"Authorization": f"Bearer {token}"}
            return requests.get(f"{Url.HOST}{UserAPI.SETTINGS}", headers=headers)
