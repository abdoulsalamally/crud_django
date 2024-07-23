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
INSTALLED APPS

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
