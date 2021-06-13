from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('', include("django.contrib.auth.urls")),
    path('customers', views.customers_list),
    path('addcustomer', views.addcustomer),
    path("customers/<customername>", views.customerQuickView),
    path('signin', views.signin),
    path('logout', views.logout),
    path('signup', views.signup),


] 