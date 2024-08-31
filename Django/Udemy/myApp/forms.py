from django import forms
from django.core import validators
from django.contrib.auth.models import User
from .models import UserProfileModel
from django.contrib.auth.forms import UserCreationForm

class FirstForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label='verify email')
    text_box=forms.CharField(widget=forms.Textarea(),
                             validators=[validators.MaxLengthValidator(10)])
    # botcatcher=forms.CharField(required=False,
    #                            widget=forms.HiddenInput,
    #                            validators=[validators.MaxLengthValidator(0)])
    
    # creating self validators self validators
    """
    def clean_botcatcher(self):
        botcatcher=self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            raise forms.ValidationError("Validation error")
        return botcatcher
    """
    
    # custom validation for email
    def clean_verify_email(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vemail=all_clean_data['verify_email']
        
        if email!=vemail:
            raise forms.ValidationError("Email should be match")
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserPortfolioForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ('portfolio_site', 'profile_picture')


class UserRegisterForm(UserCreationForm):
        email=forms.EmailField()
        class Meta:
            model=User
            fields=['username','email','password1','password2']