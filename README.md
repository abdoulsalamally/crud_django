
Nous supposons que vous avez déjà installé Python et Django depuis les sites officiels.

CRÉER UN PROJET À DJANGO
--------------------------
django-admin startproject projectname

CRÉER UNE APPLICATION
-------------
python manage.py startapp appname

EXÉCUTER LE SERVEUR
----------
python manage.py runserver


Après avoir créé une application, vous devez l'inclure dans le dossier principal de l'application dans settings.py dans 
INSTALLED_APPS = [
    'monapplication'
]

N'oubliez pas d'inclure également 'rest_framework' pour pouvoir visualiser vos points de terminaison dans le framework rest
INSTALLED_APPS = [
    'rest_framework'
]


BASE DE DONNÉES
---------
Configurons notre base de données Mysql dans settings.py sous DATABASES
 'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crud_django',
        'USER': 'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306'
    }

MIGRATION
---------
Après la création de la base de données, vous devez effectuer la migration afin que tous les modèles créés créent automatiquement les tables dans la base de données.

Exécutez les commandes suivantes :

1. python manage.py makemigrations
2. python manage.py migrate







