from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home),
    path('customers', views.customers),
    path('addcustomer', views.addcustomer),
    path('login', views.login),
    path('logout', views.logout),
    path('signup', views.signup),
   
] 