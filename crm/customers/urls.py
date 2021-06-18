from django.urls import path,include
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.signin),
    path('', include("django.contrib.auth.urls")),
    path('customers', views.customersList),
    path('addcustomer', views.addCustomer),
    path("customers/<customername>", views.customerQuickView),
    path('signin', views.signin),
    path('logout', views.logout),
    # path('signup', views.signup),
    
    
    path('sign_up', views.sign_up , name='sign_up'),
    path('dashboard', views.dashboard),
    path('signout', views.signout),
    path('export_csv', views.export_csv , name='export-csv')
] +  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



