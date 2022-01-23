from dataclasses import fields
from django.http import request
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


        def get_photo_url(self,obj):
            request = self.context.get('request')
            photo_url = obj.fingerprint.url
            return request.build_absolute_url(photo_url)
        