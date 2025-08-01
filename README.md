# API-test

Структура

    в папке allure_results/ - хранятся отчеты о тестировании
    
    в файле src/data/constants.py - константы
    в файле src/user/routes.py - API методы
    в папке tests/ - хранятся файлы с тестами
    в файле - .gitignore - игнорирование
    в файле - conftest.py - фикстуры
    в файле - pyproject.toml - необходимые зависимости

Установка зависимостей

    $ pip3 install poetry
    $ poetry install

Запуск автотестов
    
    $ pytest -v tests/

Запуск автотестов и создание HTML-отчета

    $ pytest -v tests/ --alluredir=allure_results

Запуск автотестов и создание HTML-отчета, предварительно очистив старые отчеты

    $ pytest -v tests/ --alluredir=allure_results --clean-alluredir   

Просмотр отчета 

    $ allure serve allure_results