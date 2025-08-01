import allure
import json
from src.user.routes import ApiLogin
from src.data.constants import UserData, StatusCode, Parameters, MessageText


class TestLogin:
    #  ПОЗИТИВНЫЕ ПРОВЕРКИ
    @allure.title("Тест получения кода 200, при авторизации текущего пользователя")
    @allure.description("Проверка: при авторизации под существующим пользователем, возвращается 200")
    def test_login_return_200(self):

        data = UserData.USER
        payload = json.dumps(data)
        response = ApiLogin().login_user(payload, Parameters.HEADERS)

        actually_value = response.status_code
        expected_value = StatusCode.OK_200
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
        
    @allure.title('Тест получения токена при успешной авторизации')
    @allure.description(
    'Проверка, что авторизация успешна и возвращается токен')
    def test_login_and_return_token(self):
        
        data = UserData.USER
        payload = json.dumps(data)
        response = ApiLogin().login_user(payload, Parameters.HEADERS)
        
        actually_value = response.json()
        expected_value = UserData.TOKEN
        assert expected_value in actually_value 
        allure.attach(f"{response.json()}", "Message")
    
    @allure.title("Тест получения значения ключа 'token' после авторизации")
    @allure.description("Проверка: После авторизации возвращаемое значение ключа 'token' не пустое")
    def test_login_and_return_token_value(self):
        
        data = UserData.USER
        payload = json.dumps(data)
        response = ApiLogin().login_user(payload, Parameters.HEADERS)
        
        actually_value = response.json()[UserData.TOKEN]
        expected_value = None
        assert actually_value is not expected_value
        allure.attach(f"{response.json()}", "Message")

    # НЕГАТИВНЫЕ ПРОВЕРКИ
    @allure.title("Тест получения кода 401 при неверном пароле")
    @allure.description("Проверка: при неверном пароле возвращается ошибка 401")
    def test_login_whith_wrong_pass_return_401(self):

        data = UserData.USER_WHITH_WRONG_PASS
        payload = json.dumps(data)
        response = ApiLogin().login_user(payload, Parameters.HEADERS)

        actually_value = response.status_code
        expected_value = StatusCode.UNAUTHORIZED_401
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")

    @allure.title("Тест получения кода 401 при неверной почте")
    @allure.description("Проверка: при неверной почте возвращается ошибка 401")
    def test_login_whith_wrong_email_return_401(self):        

        data = UserData.USER_WHITH_WRONG_EMAIL
        payload = json.dumps(data)
        response = ApiLogin().login_user(payload, Parameters.HEADERS)

        actually_value = response.status_code
        expected_value = StatusCode.UNAUTHORIZED_401
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")

    @allure.title("Тест получения текста ошибки при вводе неверного логина")
    @allure.description("Проверка, что при запросе c несуществущим логином получим текст ошибки")
    def test_login_whith_wrong_email_return_error_text(self):        

        data = UserData.USER_WHITH_WRONG_EMAIL
        payload = json.dumps(data)
        response = ApiLogin().login_user(payload, Parameters.HEADERS)

        actually_value = response.json()['message']
        expected_value = MessageText.MESSAGE_IF_WRONG_BODY
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
        allure.attach(f"{response.json()}", "Message")
    
    @allure.title("Тест получения текста ошибки при вводе неверного пароля")
    @allure.description("Проверка, что при запросе c неверным паролем получим текст ошибки")
    def test_login_whith_wrong_pass_return_error_text(self):        

        data = UserData.USER_WHITH_WRONG_PASS
        payload = json.dumps(data)
        response = ApiLogin().login_user(payload, Parameters.HEADERS)

        actually_value = response.json()['message']
        expected_value = MessageText.MESSAGE_IF_WRONG_BODY
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")
        allure.attach(f"{response.json()}", "Message")
