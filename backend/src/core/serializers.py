from dataclasses import fields
from rest_framework import serializers

from .models import Customer



class CustomerSerializer (serializers.ModelSerializer):
    class Meta:
        model = Customer
        # fields=[
        #     'name',
        #     'email',
        #     'primary_mobile',
        #     'alternate_mobile',
        #     'address',
        #     'city',
        #     'state',
        #     'zipcode'
        # ]
        fields='__all__'
        