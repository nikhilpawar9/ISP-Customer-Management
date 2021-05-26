from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('', include("django.contrib.auth.urls")),
    path('customers', views.customers),
    path('addcustomer', views.addcustomer),
    path('sign_up', views.sign_up , name='sign_up'),
    path('signin', views.signin),
    path('profile', views.user_profile),
  
    
   

] 