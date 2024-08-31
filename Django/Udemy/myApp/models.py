from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.


class Topics(models.Model):
    topic_name=models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.topic_name
    
class Webpage(models.Model):
    topic=models.ForeignKey(Topics,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,unique=True)
    url=models.URLField(unique=True)
    
    def __str__(self) -> str:
        return self.name
    
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
     
    def __str__(self)->datetime.date:
        return f"{self.date.strftime('%Y-%m-%d')}"
    
    
class UsersModel(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.firstname}-{self.lastname}"
    
    

class UserProfileModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site=models.URLField(blank=True)
    profile_picture=models.ImageField(upload_to="profiles")
    
    def __str__(self) -> str:
        return self.user.username
    
    
   
