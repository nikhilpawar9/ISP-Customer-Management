from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('', include("django.contrib.auth.urls")),
    path('customers', views.customers_list,name="cust"),
    path('addcustomer', views.addcustomer),
    path("customers/<customername>", views.customerQuickView),
    path('sign_up', views.sign_up , name='sign_up'),
    path('signin', views.signin),
    path('signout', views.signout),
    path('export_csv', views.export_csv , name='export-csv'),



] 