"""
django-admin startproject <project_name> . - создание проекта 

в папке <project_name> в файле settings нужно настроить связь с базой данных (переменная DATABASE)


указать 'rest_framework' в списке INSTALLED_APPS


python3 manage.py runserver [номер порта] - запуск сервера

Миграция - код, который содержит информацию о том, как будут выглядить таблицы в БД
python3 manage.py makemigrations - создание миграций 
python3 manage.py migrate - применение миграций - отправка данных в БД


python3 manage.py createsuperuser - создание суперпользователя(админа)

python3 manage startapp <app_name> - создние приложения 
"""