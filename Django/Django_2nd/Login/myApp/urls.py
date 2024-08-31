from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index' ),
    path('',views.IndexView.as_view(),name='index'),
    path('register/',views.register,name='register'),
    path('list/',views.SchoolListView.as_view(),name='list'),
    path('schools/', views.SchoolListView.as_view(), name='school_list'),
    path('schools/<int:pk>/', views.SchoolDetailView.as_view(), name='school_detail'),


]