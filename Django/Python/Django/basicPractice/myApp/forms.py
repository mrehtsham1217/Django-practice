from django import forms
from .models import Chaivariety

class ChaiVarietyForms(forms.Form):
    chai_variety=forms.ModelChoiceField(queryset=Chaivariety.objects.all(),label="Select Chai variety")