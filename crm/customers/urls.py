from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('', include("django.contrib.auth.urls")),
    path('customers', views.customers),
    path('addcustomer', views.addcustomer),
    path('login', views.login),
    path('logout', views.logout),
    
   

] 