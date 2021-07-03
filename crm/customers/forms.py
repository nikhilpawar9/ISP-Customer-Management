from django import forms
from .models import Customer


class CustomerSearchForm(forms.ModelForm):
    # export_to_CSV = forms.BooleanField(required = False)
    class Meta:
        model = Customer
        fields = ['name']


# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ['name', 'email']
