from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world,Home page")
    return render(request,'website/index.html')
def about(request):
    return HttpResponse("Hello world,About page")

def cotact(request):
    return HttpResponse("Hello world,Contact page")