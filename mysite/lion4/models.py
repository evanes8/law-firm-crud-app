from django.db import models

# Create your models here.

from django.db import models

class Record(models.Model):
    my_default=''
    matter_ref = models.TextField(blank=True, default = my_default)
    code = models.TextField(blank=True, default = my_default)
    matter_no = models.TextField(blank=True, default = my_default)
    county = models.TextField(blank=True, default = my_default)
    staff = models.TextField(blank=True, default = my_default)
    buyer = models.TextField(blank=True, default = my_default)
    buyer_firm = models.TextField(blank=True, default = my_default)
    buyer_phone = models.TextField(blank=True, default = my_default)
    seller = models.TextField(blank=True, default = my_default)
    seller_firm = models.TextField(blank=True, default = my_default)
    seller_phone = models.TextField(blank=True, default = my_default)
    client = models.TextField(blank=True, default = my_default)
    property = models.TextField(blank=True, default = my_default)
    lot_no = models.TextField(blank=True, default = my_default)
    purchase = models.TextField(blank=True, default = my_default)
    downpay = models.TextField(blank=True, default = my_default)
    attorney = models.TextField(blank=True, default = my_default)
    attorney_firm = models.TextField(blank=True, default = my_default)
    attorney_phone = models.TextField(blank=True, default = my_default)
    lender = models.TextField(blank=True, default = my_default)
    loan_office = models.TextField(blank=True, default = my_default)
    lender_phone = models.TextField(blank=True, default = my_default)
    broker = models.TextField(blank=True, default = my_default)
    broker_firm = models.TextField(blank=True, default = my_default)
    broker_phone = models.TextField(blank=True, default = my_default)

class Standard_Record(models.Model):
    my_default=''
    matter_ref = models.TextField(blank=True, default = my_default)
    code = models.TextField(blank=True, default = my_default)
    matter_no = models.IntegerField(blank=True, default = my_default)
    county = models.TextField(blank=True, default = my_default)
    staff = models.TextField(blank=True, default = my_default)
    buyer = models.TextField(blank=True, default = my_default)
    buyer_firm = models.TextField(blank=True, default = my_default)
    buyer_phone = models.TextField(blank=True, default = my_default)
    buyer_email= models.TextField(blank=True, default = my_default)
    seller = models.TextField(blank=True, default = my_default)
    seller_firm = models.TextField(blank=True, default = my_default)
    seller_phone = models.TextField(blank=True, default = my_default)
    seller_email= models.TextField(blank=True, default = my_default)
    client = models.TextField(blank=True, default = my_default)
    property = models.TextField(blank=True, default = my_default)
    lot_no = models.TextField(blank=True, default = my_default)
    purchase = models.TextField(blank=True, default = my_default)
    downpay = models.TextField(blank=True, default = my_default)
    attorney = models.TextField(blank=True, default = my_default)
    attorney_firm = models.TextField(blank=True, default = my_default)
    attorney_phone = models.TextField(blank=True, default = my_default)
    attorney_email= models.TextField(blank=True, default = my_default)
    lender = models.TextField(blank=True, default = my_default)
    loan_office = models.TextField(blank=True, default = my_default)
    lender_phone = models.TextField(blank=True, default = my_default)
    lender_email= models.TextField(blank=True, default = my_default)
    broker = models.TextField(blank=True, default = my_default)
    broker_firm = models.TextField(blank=True, default = my_default)
    broker_phone = models.TextField(blank=True, default = my_default)
    broker_email= models.TextField(blank=True, default = my_default)



