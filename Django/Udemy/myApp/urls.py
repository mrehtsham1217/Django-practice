from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('users/',views.Users,name='users'),
    path("forms/",views.MyFirstForm,name="forms"),
    path("register/",views.register,name='register')
]