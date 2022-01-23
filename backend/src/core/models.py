from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100,blank = True)
    email = models.CharField(max_length=100,blank = True)
    primary_mobile = models.IntegerField( default=0 , blank = True)
    alternate_mobile = models.IntegerField( default=0 ,blank = True)
    address = models.CharField(max_length=400, default="Jejuri")
    city = models.CharField(max_length=10, default="Jejuri")
    state = models.CharField(max_length=15, default="Maharashtra")
    zipcode = models.IntegerField (default=0, blank=True)
    connection_type = models.CharField(max_length=10,blank=True)

    #wireless
    cat_cable_length = models.IntegerField(default=0,blank = True)
    p2p_device_price = models.IntegerField(default=0)
    wireless_router_price = models.IntegerField(default=0)


    #ftth
    ftth_fiber_length = models.IntegerField(default=0)
    closer_box  = models.IntegerField(default=0)
    patch_cord = models.IntegerField(default=0)
    ftth_router_price = models.IntegerField(default=0)

    installation_charges = models.IntegerField(default=0)

    username = models.CharField(max_length=400, default="user")
    password = models.CharField(max_length=400, default="pass")

    # def nameFile(instance, filename):
    #  return 'images/{filename}'.format(filename=filename)


    cust_photo = models.ImageField(upload_to="media", blank=True)
    kyc_doc = models.ImageField(upload_to="media", blank=True)




    
    

    def __str__(self):
        return self.name

