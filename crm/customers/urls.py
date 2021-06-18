from django.urls import path,include
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home),
    path('', include("django.contrib.auth.urls")),
    path('customers', views.customersList),
    path('addcustomer', views.addCustomer),
    path("customers/<customername>", views.customerQuickView),
    path('signin', views.signin),
    path('logout', views.logout),
    path('signup', views.signup),
] +  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)