from distutils.log import error
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response 
from rest_framework.views import APIView
from .serializers import CustomerSerializer
from .models import Customer
# Create your views here.



class CustomerView(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            cust = Customer.objects.get(id=id)
            serializer = CustomerSerializer(cust)
            return Response(serializer.data)

        cust = Customer.objects.all()
        serializer = CustomerSerializer(cust, many =True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)

    
    def put(self,request,pk,format=None):
        id = pk
        cust = Customer.objects.get(pk=id)
        serializer = CustomerSerializer(cust,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Updated'})
        return Response(serializer.errors)


    def delete(self,request,pk,format=None):
        id=pk
        cust = Customer.objects.get(pk=id)
        cust.delete()
        return Response({'msg':'deleted data'})
