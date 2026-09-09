import allure
from base.pages.api_pages.authorized.auth_base import AuthBase
import random

class MethodsAuthorized:

    @staticmethod
    @allure.step("Авторизация пользователя через POST /Account/v1/Authorized")
    def post_v1_account_authorized():
        """
        Метод для выполнения авторизации пользователя через POST-запрос на эндпоинт /Account/v1/Authorized.

        Этот метод используется для авторизации пользователя, используя предоставленные имя пользователя и пароль.
        В процессе выполнения метода происходит несколько шагов:

        1. Создается экземпляр класса `AuthBase`, где задаются параметры авторизации (имя пользователя и пароль).
        2. Формируются данные для запроса и полный URL для авторизации.
        3. Выполняется отправка POST-запроса на сервер с предоставленными данными.
        4. Выполняется валидация ответа сервера, проверяется успешность авторизации.

        В случае успешной авторизации, результат валидации добавляется в отчет Allure и выводится в консоль.
        Если авторизация не удалась, тест завершится с ошибкой, и информация об этом также будет включена в отчет Allure.
        """
        auth_base = AuthBase(username="Hello1", password="Qwerty1234!")

        with allure.step("Формирование данных и отправка запроса"):
            data, url = auth_base.form_request_data(auth_base.get_authorized_endpoint())
            response = auth_base.send_post_request(data, url)

        with allure.step("Валидация ответа"):
            auth_base.validate_response(response, auth_base.validate_success_response)

    @staticmethod
    @allure.step("Генерация токена через POST /Account/v1/GenerateToken")
    def post_token_authorized():
        """
        Метод для генерации токена пользователя через POST-запрос на эндпоинт /Account/v1/GenerateToken.

        Этот метод используется для получения токена пользователя, используя предоставленные имя пользователя и пароль.
        В процессе выполнения метода происходит несколько шагов:

        1. Создается экземпляр класса `AuthBase`, где задаются параметры авторизации (имя пользователя и пароль).
        2. Формируются данные для запроса и полный URL для генерации токена.
        3. Выполняется отправка POST-запроса на сервер с предоставленными данными.
        4. Выполняется валидация ответа сервера, проверяется успешность генерации токена.

        В случае успешного получения токена, результат валидации добавляется в отчет Allure и выводится в консоль,
        включая сгенерированный токен. Если запрос на генерацию токена не удался, тест завершится с ошибкой, и информация
        об этом также будет включена в отчет Allure.
        """
        auth_base = AuthBase(username="Hello1", password="Qwerty1234!")

        with allure.step("Формирование данных и отправка запроса"):
            data, url = auth_base.form_request_data(auth_base.get_generate_token_endpoint())
            response = auth_base.send_post_request(data, url)

        with allure.step("Валидация ответа"):
            auth_base.validate_response(response, auth_base.validate_token_response)

    @staticmethod
    @allure.step("Создание пользователя через POST /Account/v1/User")
    def post_create_user():
        """
        Метод для создания пользователя через POST-запрос на эндпоинт /Account/v1/User.

        Этот метод используется для создания пользователя, используя предоставленные имя пользователя и пароль.
        В процессе выполнения метода происходит несколько шагов:

        1. Создается экземпляр класса `AuthBase`, где задаются параметры авторизации (имя пользователя и пароль).
        2. Формируются данные для запроса и полный URL для создания пользователя.
        3. Выполняется отправка POST-запроса на сервер с предоставленными данными.
        4. Выполняется валидация ответа сервера, проверяется успешность создания.

        В случае успешного создания пользователя, результат валидации добавляется в отчет Allure и выводится в консоль,
        включая имя пользователя, id. Если запрос на генерацию токена не удался, тест завершится с ошибкой, и информация
        об этом также будет включена в отчет Allure.
        """

        auth_base = AuthBase(username=f"EvgenyGord{random.randint(0,9999)}", password="Qwerty1234!")

        with allure.step("Формирование данных и отправка запроса"):
            data, url = auth_base.form_request_data(auth_base.get_user_endpoint())
            response = auth_base.send_post_request(data, url)

        with allure.step("Валидация ответа"):
            auth_base.validate_create_response(response, auth_base.validate_create_user_response)

    @staticmethod
    @allure.step("Удаление пользователя через API")
    def delete_v1_user():
        """
        Тест для проверки удаления пользователя через DELETE-запрос на эндпоинт /Account/v1/User/uid.

        Этот тест выполняет следующие шаги:
        1. Создается экземпляр класса `AuthBase`, где задаются параметры авторизации (имя пользователя и пароль).
        2. Формируются данные для запроса и полный URL для создания пользователя.
        3. Выполняется отправка DELETE-запроса на сервер с предоставленными данными.
        4. Выполняется валидация ответа сервера, проверяется успешность создания.

        """

        auth_base = AuthBase(username=f"EvgenyGord{random.randint(0, 9999)}", password="Qwerty1234!")

        with allure.step("Формирование данных и отправка запроса на создание пользователя"):
            data_create, url_create = auth_base.form_request_data(auth_base.get_user_endpoint())
            response_create = auth_base.send_post_request(data_create, url_create)

        with allure.step("Формирование данных и отправка запроса на генерацию токена, авторизация true"):
            data_generate_token, url_generate_token = auth_base.form_request_data(auth_base.get_generate_token_endpoint())
            response_generate_token = auth_base.send_post_request(data_generate_token, url_generate_token)

        with allure.step("Формирование данных и отправка запроса на удаление пользователя"):
            url = auth_base.form_request_data_delete(auth_base.get_delete_user_endpoint(f'{response_create.json()["userID"]}'))
            headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {response_generate_token.json().get('token')}"
        }
            response = auth_base.send_delete_request(url,headers)

        with allure.step("Валидация ответа"):
            auth_base.validate_response(response, auth_base.validate_delete_response)

    @staticmethod
    @allure.step("Получение информации о пользователе GET/Account/v1/User/uid ДО/ПОСЛЕ удаления")
    def get_v1_user():
        """
        Тест для проверки получения информации о пользователе через GET-запрос на эндпоинт /Account/v1/User/uid ДО/ПОСЛЕ удаления.

        Этот тест выполняет следующие шаги:
        1. Создается экземпляр класса `AuthBase`, где задаются параметры авторизации (имя пользователя и пароль).
        2. Формируются данные для запроса и полный URL для создания пользователя.
        3. Выполняется отправка DELETE-запроса на сервер с предоставленными данными.
        4. Выполняется валидация ответа сервера, проверяется успешность создания.

        """

        auth_base = AuthBase(username=f"EvgenyGord{random.randint(0, 9999)}", password="Qwerty1234!")

        with allure.step("Формирование данных и отправка запроса на создание пользователя"):
            data_create, url_create = auth_base.form_request_data(auth_base.get_user_endpoint())
            response_create = auth_base.send_post_request(data_create, url_create)

        with allure.step("Формирование данных и отправка запроса на генерацию токена, авторизация true"):
            data_generate_token, url_generate_token = auth_base.form_request_data(
                auth_base.get_generate_token_endpoint())
            response_generate_token = auth_base.send_post_request(data_generate_token, url_generate_token)
            headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {response_generate_token.json().get('token')}"
            }
        with allure.step("ПОЛУЧЕНИЕ ИНФОРМАЦИИ О ПОЛЬЗОВАТЕЛЕ v1 ДО УДАЛЕНИЯ"):
            url_get_user = auth_base.form_request_data_get(auth_base.get_user_info_endpoint(f'{response_create.json()["userID"]}'))
            response_get_info_user_do = auth_base.send_get_request(url_get_user, headers)

        with allure.step("Валидация ответа"):
            auth_base.validate_response(response_get_info_user_do, auth_base.validate_get_user_response)

        with allure.step("Формирование данных и отправка запроса на удаление пользователя"):
            url = auth_base.form_request_data_delete(
                auth_base.get_delete_user_endpoint(f'{response_create.json()["userID"]}'))

            response = auth_base.send_delete_request(url, headers)

        with allure.step("Валидация ответа ДО УДАЛЕНИЯ"):
            auth_base.validate_response(response, auth_base.validate_delete_response)

        with allure.step("ПОЛУЧЕНИЕ ИНФОРМАЦИИ О ПОЛЬЗОВАТЕЛЕ v1 ПОСЛЕ УДАЛЕНИЯ"):
            url_get_user = auth_base.form_request_data_get(
                auth_base.get_user_info_endpoint(f'{response_create.json()["userID"]}'))
            response_get_info_user_do = auth_base.send_get_request(url_get_user, headers)

        with allure.step("Валидация ответа ПОСЛЕ УДАЛЕНИЯ"):
            auth_base.validate_user_not_found_response(response_get_info_user_do)
