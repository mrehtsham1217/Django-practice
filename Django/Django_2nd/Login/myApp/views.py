from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth import login
from django.views.generic import View,TemplateView,ListView,DetailView

class IndexView(TemplateView):
    template_name='website/index.html'
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['injectme']="Basic Injection"
        return context

# Create your views here.
def index(request):
    return render(request,'website/index.html')

def register(request):
    if request.method == 'POST':
        form = forms.userRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Ensure field name matches
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = forms.userRegisterForm()
    
    return render(request, 'registration/register.html', {"form": form})


class SchoolListView(ListView):
    context_object_name="schools"
    model=models.School
    template_name = 'website/school_list.html'
    
class SchoolDetailView(DetailView):
    context_object_name="school_detail"
    model=models.School
    template_name='webiste/school_detail.html'