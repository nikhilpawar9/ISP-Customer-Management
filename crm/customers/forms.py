from django import forms
from customers.models import Customer


class CustomerSearchForm(forms.ModelForm):
    # export_to_CSV = forms.BooleanField(required = False)
    class Meta:
        model = Customer
        fields= ['name' ]