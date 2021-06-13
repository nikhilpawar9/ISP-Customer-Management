from django import forms
from customers.models import Customer

class CustomerSearchForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields= ['name' , 'primary_mobile']