from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render (request, 'customers/dashboard.html')

def customers(request):
    return render (request, 'customers/customers.html')