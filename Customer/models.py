from django.db import models
from .utils import unique_order_id_generator
from django.db.models.signals import pre_save
import datetime

# Create your models here.
class Customer(models.Model):
    order_id = models.CharField('order id', max_length=120, blank=True)
    name = models.CharField('name', max_length=150, blank=False)
    billing_address = models.CharField('billing address', max_length=500, blank=False, default=None)
    billing_city = models.CharField('billing city', max_length=120, blank=False, default=None)
    billing_postal_code = models.CharField('billing postal code', max_length=15, blank=False, default=None)
    billing_state = models.CharField('billing state', max_length=20, blank=False, default=None)
    ship_address = models.CharField('shipping address', max_length=500, blank=False, default=None)
    ship_city = models.CharField('shipping city', max_length=120, blank=False, default=None)
    ship_postal_code = models.CharField('shipping postal code ', max_length=15, blank=False, default=None)
    ship_state = models.CharField('shipping state', max_length=20, blank=False, default=None)
    phone = models.PositiveBigIntegerField('mobile',null=True,blank=True)
    email = models.EmailField('email', unique=True,max_length=255,blank=False)
    date_entered = models.DateField('date', default=datetime.datetime.now) 

    def __str__(self):
        return self.name

def pre_save_order_id(sender, instance, *args, **kwargs):
        if not instance.order_id:
             instance.order_id = unique_order_id_generator(instance)
 
pre_save.connect(pre_save_order_id, sender=Customer)