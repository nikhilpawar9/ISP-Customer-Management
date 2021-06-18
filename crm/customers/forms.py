from django import forms
from .models import *

class CustomerSearchForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields= ['name' , 'primary_mobile']
        
