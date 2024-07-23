We suppose you have already installed python and django from the official sites.

CREATE A PROJECT IN DJANGO
--------------------------
django-admin startproject projectname

CREATE AN APP
-------------
python manage.py startapp appname

RUN SERVER
----------
python manage.py runserver


After creating an app you have to include it in the main app folder inside settings.py in 
INSTALLED_APPS = [
    'myapp'
]

Don't forget to also include 'rest_framework' to be able to visualize your endpoints in rest framework
INSTALLED_APPS = [
    'rest_framework'
]


DATABASE
--------
Let us set up our Mysql database inside settings.py under DATABASES
 'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crud_django',
        'USER': 'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306'
    }




