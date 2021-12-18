

# Create your models here.

from django.db import models
from django.utils.translation import gettext_lazy as _


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


class Record(models.Model):
    my_default=''
    matter_ref = models.TextField(blank=True, default = my_default)
    code = models.TextField(blank=True, default = my_default)
    matter_no = models.IntegerField(blank=True, default = my_default)
    county = models.TextField(blank=True, default = my_default)
    staff = models.TextField(blank=True, default = my_default)
    property = models.TextField(blank=True, default = my_default)
    lot_no = models.TextField(blank=True, default = my_default)
    purchase = models.TextField(blank=True, default = my_default)
    downpay = models.TextField(blank=True, default = my_default)
    def client_name_set(self):
        clients=[record_contact.contact.name for record_contact in self.record_contact_set.all() if record_contact.is_client]
        return clients


class Contact(models.Model):
    my_default=''
    name=models.TextField(blank=True, default = my_default)
    firm=models.TextField(blank=True, default = my_default)
    phone=models.TextField(blank=True, default = my_default)
    fax=models.TextField(blank=True, default = my_default)
    email=models.TextField(blank=True, default = my_default)

class Record_Contact(models.Model):
    record=models.ForeignKey(Record, on_delete=models.CASCADE)
    contact=models.ForeignKey(Contact, on_delete=models.CASCADE)
    is_client=models.BooleanField(default=0)
    class Role(models.TextChoices):
        BUYER = 'BY', _('Buyer')
        SELLER = 'SL', _('Seller')
        ATTORNEY = 'AT', _('Attorney')
        LENDER = 'LN', _('Lender')
        BROKER= 'BR', _('Broker')
        OTHER= 'OT', _('Other')
    role = models.CharField(
        max_length=2,
        choices=Role.choices,
    )


#helper functions


