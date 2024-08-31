from django.db import models
from django.contrib.auth.models import User
# from datetime import timezone

# Create your models here.
class Tweet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    tweet_text=models.TextField(max_length=300)
    photo=models.ImageField(upload_to='tweetPhotos/')
    # auto_now_add-->Save time when when tweet add
    # time saves when tweet update
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.user.username}-{self.tweet_text[:10]}"