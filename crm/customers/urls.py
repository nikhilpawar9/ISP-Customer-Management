from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('', include("django.contrib.auth.urls")),
    path('customers', views.customers),
    path('addcustomer', views.addcustomer),

    path('signin', views.signin),
    path('logout', views.logout),
    path('signup', views.signup),


] 