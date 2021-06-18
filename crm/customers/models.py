from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, primary_key = True)
    email = models.CharField(max_length=100, default= "admin@ithreesystem.com")
    primary_mobile = models.IntegerField( default=0)
    alternate_mobile = models.IntegerField( default=0 )
    address = models.CharField(max_length=400, default="Jejuri")
    city = models.CharField(max_length=10, default="Jejuri")
    state = models.CharField(max_length=15, default="Maharashtra")
    zipcode = models.IntegerField (default=0, blank=True)
    
    connection_type = models.CharField( max_length=20 ,default="not selected")
    
    # wrieless
    cat_6_cable_length= models.IntegerField( )
    p2p_device_price= models.IntegerField( )
    wireless_router_price= models.IntegerField( )
    
    # ftth
    ftth_fiber_length= models.IntegerField( )
    closer_box = models.CharField(max_length=5 )
    patch_cord= models.IntegerField( )
    ftth_router_price= models.IntegerField()

    
    installation_charges= models.IntegerField( default=0)
    username= models.CharField(max_length=10, default="username")
    password= models.CharField(max_length=10, default="password")
    
    customer_photo= models.ImageField(upload_to="media", blank=True)
    kYC_document= models.ImageField(upload_to="media", blank=True)
    def __str__(self):
        return self.name

