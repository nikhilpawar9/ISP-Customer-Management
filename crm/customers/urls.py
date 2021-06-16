from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.signin),
    path('', include("django.contrib.auth.urls")),
    path('customers', views.customers_list,name="cust"),
    path('addcustomer', views.addcustomer),
    path("customers/<customername>", views.customerQuickView),
    path('sign_up', views.sign_up , name='sign_up'),
    path('dashboard', views.dashboard),
    path('signout', views.signout),
    path('export_csv', views.export_csv , name='export-csv'),
] 