from django.db import models


class PaymentManager(models.Manager):
    
    def create_payment(self, ondcTransactionId: str, paymentType: int, amount: int, upi='', bankAccount='', accountNumber='', buyerAppFinderFee=0):

        payment = self.model(ondcTransactionId=ondcTransactionId, paymentType=paymentType, amount=amount, upi=upi, bankAccount=bankAccount, accountNumber=accountNumber, buyerAppFinderFee=buyerAppFinderFee)
        self.save(payment=payment)

        return payment

    def save(self, payment):
        payment.save(using=self._db)


class Payment(models.Model):

    ondcTransactionId = models.CharField(max_length=255, null=False) #ONDC Transaction Id  from ONDC network
    orderId = models.CharField(max_length=100, unique=True) #Bank Order Id, could be Null
    referenceId = models.CharField(max_length=100, unique=True) #Bank Reference Id, could be Null

    paymentType = models.BigIntegerField(null=False)
    upi = models.CharField(max_length=200)
    bankAccount = models.CharField(max_length=100)
    accountNumber = models.CharField(max_length=17)
    date = models.DateField(auto_now_add=True)
    timestamp =  models.TimeField(auto_now_add=True)
    amount = models.BigIntegerField(max_length=200, null=False)
    buyerAppFinderFee = models.BigIntegerField(max_length=200, default=0)
    returned = models.BooleanField(default=False)
