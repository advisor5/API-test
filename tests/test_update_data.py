import allure
import pytest
from src.user.routes import ApiLogin
from src.data.constants import UserData, StatusCode, MessageText


class TestUpdate:
    #  ПОЗИТИВНЫЕ ПРОВЕРКИ
    @allure.title("Тест получения кода 200 при изменении имени пользователя")
    @allure.description("Проверка: После успешного изменения имени пользователя возвращается код 200")
    def test_update_user_return_200(self, generate_update_date, auth_user):

        token = auth_user
        update_data = generate_update_date
        response_update = ApiLogin().update_user(update_data, token)

        actually_value = response_update.status_code
        expected_value = StatusCode.OK_200
        assert actually_value == expected_value
        allure.attach(f"Status {response_update.status_code}", "Response status")
    
    @allure.title("Тест получения кода 200 после изменения языковых настроек")
    @allure.description("Проверка: После изменение допустимых языковых настроек, возвращается код 200")
    @pytest.mark.parametrize("locale",["ru", "en","pt"])
    def test_update_user_locale_return_200(self, auth_user, locale):
        token = auth_user
        update_data = { 
        "name": "IVAN Ivanov",
        "time_zone": "Europe/Moscow",
        "sip_number": "123", 
        "sip_extension": "22344", 
        "events_view_type": 1,
        "locale": locale
        }

        response_update = ApiLogin().update_user(update_data, token)

        actually_value = response_update.status_code
        expected_value = StatusCode.OK_200
        assert actually_value == expected_value
        allure.attach(f"Status {response_update.status_code}", "Response status")

    @allure.title("Тест получения измененного значения после изменения языковых настроек")
    @allure.description("Проверка: После изменение языковых настроек,\
                        при запросе возвращаются измененные данные")
    @pytest.mark.parametrize('locale',["ru", "en","pt"])
    def test_update_user_locale_return_locale(self, auth_user, locale):
        token = auth_user
        update_data = { 
        "name": "IVAN Ivanov",
        "time_zone": "Europe/Moscow",
        "sip_number": "123", 
        "sip_extension": "22344", 
        "events_view_type": 1,
        "locale": locale
        }

        response_update = ApiLogin().update_user(update_data, token)
        response = ApiLogin().get_user(token)

        actually_value = response.json()["locale"]
        expected_value = locale
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")

    @allure.title("Тест получения кода 200 при изменении способа отображения списков событий")
    @allure.description("Проверка: При успешном изменении способа отображения списков событий\
                        отображается возвращается код 200")
    @pytest.mark.parametrize('events',[1, 2])
    def test_update_user_events_return_200(self, auth_user, events):
        token = auth_user
        update_data = { 
        "name": "IVAN Ivanov",
        "time_zone": "Europe/Moscow",
        "sip_number": "123", 
        "sip_extension": "22344", 
        "events_view_type": events,
        "locale": "ru"
        }

        response_update = ApiLogin().update_user(update_data, token)

        actually_value = response_update.status_code
        expected_value = StatusCode.OK_200
        assert actually_value == expected_value
        allure.attach(f"Status {response_update.status_code}", "Response status")

    @allure.title("Тест получения измененного значения способа отображения списков событий")
    @allure.description("Проверка: При успешном изменении способа отображения списков событий\
                        возвращается измененное значение")
    @pytest.mark.parametrize('events',[1, 2])
    def test_update_user_events_return_value(self, auth_user, events):
        token = auth_user
        update_data = { 
        "name": "IVAN Ivanov",
        "time_zone": "Europe/Moscow",
        "sip_number": "123", 
        "sip_extension": "22344", 
        "events_view_type": events,
        "locale": "ru"
        }

        response_update = ApiLogin().update_user(update_data, token)
        response = ApiLogin().get_user(token)

        actually_value = response.json()["events_view_type"]
        expected_value = events
        assert actually_value == expected_value
        allure.attach(f"Status {response.status_code}", "Response status")

    # НЕГАТИВНЫЕ ПРОВЕРКИ
    @allure.title("Тест невозможности внести некорретные данные в языковые настройки")
    @allure.description("Проверка: После внесения некорректных языковых настроек, возвращается код 422")
    @pytest.mark.parametrize('locale',["jp", "us","ch"])
    def test_not_update_user_return_422(self, auth_user, locale):
        token = auth_user
        update_data = { 
        "name": "IVAN Ivanov",
        "time_zone": "Europe/Moscow",
        "sip_number": "123", 
        "sip_extension": "22344", 
        "events_view_type": 1,
        "locale": locale
        }

        response_update = ApiLogin().update_user(update_data, token)

        actually_value = response_update.status_code
        expected_value = StatusCode.UNPROCESSABLE_ENTITY_422
        assert actually_value == expected_value
        allure.attach(f"Status {response_update.status_code}", "Response status")

    @allure.title("Тест получения кода 422 при отправке запроса на обновление данных без обязательных ключей")
    @allure.description("")
    @pytest.mark.parametrize(
        'user_data',
        [
            UserData.USER_DATA_WITHOUD_NAME,
            UserData.USER_DATA_WITHOUD_TIME_ZONE,
            UserData.USER_DATA_WITHOUD_EVENTS
        ]
        )
    def test_without_required_key_return_422(self, auth_user, user_data):
        token = auth_user
        update_data = user_data

        response_update = ApiLogin().update_user(update_data, token)

        actually_value = response_update.status_code
        expected_value = StatusCode.UNPROCESSABLE_ENTITY_422
        assert actually_value == expected_value
        allure.attach(f"Status {response_update.status_code}", "Response status")

    @allure.title("Тест получения 'errors' при отправке запроса на обновление данных без обязательных ключей")
    @allure.description("При отправке запроса на обновление данных без обязательных ключей\
                        в тексте возвращаемого сообщения содержится текст 'errors'")
    @pytest.mark.parametrize(
        'user_data',
        [
            UserData.USER_DATA_WITHOUD_NAME,
            UserData.USER_DATA_WITHOUD_TIME_ZONE,
            UserData.USER_DATA_WITHOUD_EVENTS
        ]
        )
    def test_without_required_key_impossible_update_data(self, auth_user, user_data):
        token = auth_user
        update_data = user_data

        response_update = ApiLogin().update_user(update_data, token)

        actually_value = response_update.json()
        expected_value = UserData.ERROR
        assert expected_value in actually_value
        allure.attach(f"Status {response_update.status_code}", "Response status")
        allure.attach(f"{response_update.json()}", "Message")

    @allure.title("Тест получения 422 при отправке недопустимых значений способа отображения списков событий")
    @allure.description("Проверка: при отправке недопустимых значений (-1,0,3) возвращается код ошибки 422")
    @pytest.mark.parametrize('events',[-1, 0, 3])
    def test_update_user_events_wrong_value_return_422(self, auth_user, events):
        token = auth_user
        update_data = { 
        "name": "IVAN Ivanov",
        "time_zone": "Europe/Moscow",
        "sip_number": "123", 
        "sip_extension": "22344", 
        "events_view_type": events,
        "locale": "ru"
        }

        response_update = ApiLogin().update_user(update_data, token)

        actually_value = response_update.status_code
        expected_value = StatusCode.UNPROCESSABLE_ENTITY_422
        assert actually_value == expected_value
        allure.attach(f"Status {response_update.status_code}", "Response status")

    @allure.title("Тест получения текста ошибки при отправке недопустимых значений способа отображения списков событий")
    @allure.description("Проверка: при отправке недопустимых значений (-1,0,3) возвращается текст указывыающий на тип ошибки")
    @pytest.mark.parametrize('events',[-1, 0, 3])
    def test_update_user_events_wrong_value_return_message_error(self, auth_user, events):
        token = auth_user
        update_data = { 
        "name": "JONN koner",
        "time_zone": "Europe/Moscow",
        "sip_number": "123", 
        "sip_extension": "22344", 
        "events_view_type": events,
        "locale": "ru"
        }

        response_update = ApiLogin().update_user(update_data, token)

        actually_value = response_update.json()["message"]
        expected_value = MessageText.ERROR_EVENTS_INVALID
        assert actually_value == expected_value
        allure.attach(f"Status {response_update.status_code}", "Response status")
        allure.attach(f"{response_update.json()}", "Message")

    @allure.title("Тест получения текста ошибки для каждого типа недостающих данных")
    @allure.description("При запросе на обновление данных, без обязательных полей,\
                         возвращается текст ошибки для каждые недостащих данных")
    @pytest.mark.parametrize(
        "user_data, type_error, text_error",
        [
            [UserData.USER_DATA_WITHOUD_NAME, MessageText.TYPE_ERROR_NAME ,MessageText.ERROR_NAME],
            [UserData.USER_DATA_WITHOUD_TIME_ZONE, MessageText.TYPE_ERROR_TIMEZONE, MessageText.ERROR_TIMEZONE],
            [UserData.USER_DATA_WITHOUD_EVENTS, MessageText.TYPE_ERROR_EVENTS, MessageText.ERROR_EVENTS]
        ]
        )
    def test_without_required_key_return_error_message_for_each_type(self, auth_user, user_data, type_error, text_error):
        token = auth_user
        update_data = user_data

        response_update = ApiLogin().update_user(update_data, token)

        actually_value = response_update.json()["errors"][type_error]
        expected_value = [text_error]
        assert actually_value == expected_value
        allure.attach(f"Status {response_update.status_code}", "Response status")
        allure.attach(f"{response_update.json()}", "Message")
