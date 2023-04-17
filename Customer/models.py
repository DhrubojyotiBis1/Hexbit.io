from django.db import models
from django.utils import timezone

# Create your models here.
class CustomerManager(models.Manager):
    """Manager for Customer"""

    def create_customer(self, order_id, name, billing_address ,billing_city ,billing_postal_code, billing_state, ship_address, ship_city ,ship_postal_code ,ship_state,phone,email, date_entered):
        
        customer = self.model(order_id=order_id, name=name, billing_address=billing_address ,billing_city=billing_city,billing_postal_code=billing_postal_code, billing_state=billing_state, ship_address=ship_address, ship_city=ship_city,ship_postal_code=ship_postal_code, ship_state=ship_state, phone=phone, email=email, date_entered=date_entered)

        self.save(customer=customer)
    
    def save(self, customer):
        customer.save(using=self._db)

class Customer(models.Model):
    order_id = models.BigIntegerField('order id', unique=True, null=False)
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
    date_entered = models.DateField('date', default=timezone.now) 

    object = CustomerManager()

    def __str__(self):
        return self.name