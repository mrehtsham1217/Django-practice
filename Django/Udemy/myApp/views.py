from django.shortcuts import render
from .models import AccessRecord,UsersModel
from . import forms
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect,HttpResponse
# from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import login

from .forms import UserRegisterForm
from django.shortcuts import redirect


# Create your views here.
def index(request):
    # Fetching AccessRecord entries
    access_record_list = AccessRecord.objects.all().order_by('date')
    return render(request, 'website/index.html', {"access_record_list": access_record_list})

def Users(request):
    user_list=UsersModel.objects.all().order_by("firstname")
    return render(request,"website/all_users.html",{"user_list":user_list})
# creating forms

def MyFirstForm(request):
    form=forms.FirstForm()
    if request.method=='POST':
        form=forms.FirstForm(request.POST)
        if form.is_valid():
            print("validation success...!")
            print("Name:",form.cleaned_data['name'])
            print("Email:",form.cleaned_data['email'])
            print("Email:",form.cleaned_data['verify_email'])
            print("Description:",form.cleaned_data['text_box'])
    return render(request,"website/myForms.html",{"form":form})

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('index')
    else:
        form=UserRegisterForm()
    return render(request,"registration/register.html",{"form":form})
            







    
"""
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserPortfolioForm(data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserPortfolioForm()
    
    return render(request, 'website/registration.html', {
        "registered": registered,
        "user_form": user_form,
        "profile_form": profile_form
    })
    
    
    
def user_login(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account is not active")
        else:
            print("SOmeone login but failed ...")
            print("username {},password:{}".format(username,password))
    else:
        return render(request,'website/login.html')
    """