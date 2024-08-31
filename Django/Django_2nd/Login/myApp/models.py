from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.user.username


class School(models.Model):
    name=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    
    def __str__(self) -> str:
        return self.name 
