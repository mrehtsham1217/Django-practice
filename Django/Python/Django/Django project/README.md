# Complete Flow of Django Project

## Create Virtual environment
```
Pip3 install uv (uv is build in rust language. It is very fast)
    1. uv .venv (alternate method)
    2. python -m venv myvenv
    3. source myvenv/bin/activate
```
## Install Django
```
    1. uv pip install django (Remove uv if   you are not created Environment using uv)
    2. uv pip freeze > requirements.txt
```
## Create and run project project 
```
    1. django-admin startproject myproject
    2. cd myproject-→python manage.py runserver
```
## makemigrations and migrate
```
    1. python manage.py makemigrations
    2. python manage.py migrate
```
## Create Super User in Django
```
    1. python manage.py createsuperuser (username,email,password)
```
## Handling images in database (setting)
```
 python -m pip install Pillow
 uv pip install Pillow (if using uv)
 MEDIA_URL='/media/'
 MEDIA_ROOT=os.path.join(BASE_DIR,'media/)
```
## Handling Static Files
```
STATIC_URL='static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ....
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

```
## Creating app in project
```
python manage.py startapp myapp
```
## addding app in installed Project
```
tweet-->settings.py
path('tweet/',include('tweet.urls'))-->project urls.py


# Django shell
```
python manage.py shell --->To make an object and save directly in database
```

```
mrehtsham
mrehtsham615688##
```
