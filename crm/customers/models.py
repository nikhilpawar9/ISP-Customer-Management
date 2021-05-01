from django.db import models


PLAN = (
    ('plan1','plan1'),
    ('plan2','plan2'),
    ('plan3','plan3'),
)
CONNECTION_TYPE = (
    ('connectiontype1','connectiontype1'),
    ('connectiontype2','connectiontype2'),
    ('connectiontype3','connectiontype3'),
)
ROUTER_MODEL = (
    ('router1','router1'),
    ('router2','router2'),
    ('router3','router3'),
)
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100, primary_key = True)
    address = models.CharField(max_length=400)
    connection_type = models.CharField(max_length=20, choices=CONNECTION_TYPE)
    router = models.CharField(max_length=20, choices=ROUTER_MODEL)
    plan = models.CharField(max_length=20, choices=PLAN)
    primary_mobile = models.IntegerField(max_length=10)
    alternate_mobile = models.IntegerField(max_length=10, null=True)
    #image= models.ImageField(upload_to="customers/images",default="")
    def __str__(self):
        return self.name