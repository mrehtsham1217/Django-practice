from django.urls import path
from . import views
urlpatterns = [
    path("",views.all_chai,name="all_chai"),
    path("<int:chai_id>/",views.chai_detail,name="Chai_detail"),
    path("chai_forms/",views.chai_forms,name="chai_forms")


]
