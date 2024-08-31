from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Chaivariety(models.Model):
    CHAI_CHOICES=[
        ('DP','DoodhPatti'),
        ('ST','StrongChai'),
        ('GC','GingerChai'),
        ('EL','ElachiChai')
    ]
    name=models.CharField(max_length=20)
    images=models.ImageField(upload_to="chaiFolder/")
    chaiTypes=models.CharField(max_length=2,choices=CHAI_CHOICES,)
    description=models.TextField(default=" ")
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.name
    
    
# Relationships in Database
# Foreignkey means Relationship is one to many
class ChaiReviews(models.Model):
    chai=models.ForeignKey(Chaivariety,on_delete=models.CASCADE,related_name="reviews")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comments=models.TextField()
    date_time=models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return f"{self.user.username} has reviewed for {self.chai.name}"
    
# many to many field
class Store(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=100)
    chai_variets=models.ManyToManyField(Chaivariety,related_name="stores")
    
    def __str__(self) -> str:
        return self.name
    
    
# one to one field
class ChaiCertificate(models.Model):
    chai=models.OneToOneField(Chaivariety,on_delete=models.CASCADE,related_name="certificates")
    certificate_no=models.CharField(max_length=100)
    issue_date=models.DateTimeField(default=timezone.now)
    valid_date=models.DateTimeField()
    
    
    def __str__(self) -> str:
        return f"Certificate for {self.chai.name }"
    
    
