from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class userRegisterForm(UserCreationForm):
    email=forms.EmailField()
    profile_picture=forms.ImageField(required=False)
    class Meta:
        model=User
        fields=['username','email','password1','password2','profile_picture']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Save the profile picture if provided
            if 'profile_picture' in self.files:
                UserProfile.objects.create(user=user, profile_picture=self.files['profile_picture'])
        return user