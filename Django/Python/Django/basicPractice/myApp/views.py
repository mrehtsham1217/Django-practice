from django.shortcuts import render
from .models import Chaivariety,Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForms

# Create your views here.
def all_chai(request):
    chais=Chaivariety.objects.all()
    return render(request,"myApp/myindex.html",{"chais":chais})

def chai_detail(request,chai_id):
    chai=get_object_or_404(Chaivariety,pk=chai_id)
    return render(request,'myApp/chai_detail.html',{"chai":chai})

def chai_forms(request):
    stores=None
    if request.method=='POST':
        form=ChaiVarietyForms(request.POST)
        if form.is_valid():
            chai_variety=form.cleaned_data['chai_variety']
            stores=Store.objects.filter(chai_variets=chai_variety)
    else:
        form=ChaiVarietyForms()
    return render(request,'myApp/chai_forms.html',{"stores":stores,"form":form})
    