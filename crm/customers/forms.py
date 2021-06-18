from django import forms
from .models import *


class CustomerSearchForm(forms.ModelForm):
    # export_to_CSV = forms.BooleanField(required = False)
    class Meta:
        model = Customer
        fields= ['name' ]
