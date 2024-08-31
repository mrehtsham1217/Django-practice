from . import views
from django.urls import path
urlpatterns = [
    path('',views.get_all_tweets,name="tweet_list"),
    path('create/',views.tweet_create,name="tweet_create"),
    path('<int:tweet_id>/edit/',views.tweet_edit,name="tweet_edit"),
    path('<int:tweet_id>/delete/',views.tweet_delete,name="tweet_delete"),
    path("register/",views.register,name='register'),
    # urls.py
    path('<str:username>/profile', views.user_profile, name='user_profile'),
    path('search/', views.search_user, name='search_users'),


]