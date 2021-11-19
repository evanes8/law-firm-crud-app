
from django import forms

class InputForm(forms.Form):
    matter_no=forms.CharField(label='File Number', max_length=100, required=False)
    matter_ref= forms.CharField(label='File Name', max_length=100, required=False)
    code= forms.CharField(label='Code', max_length=100, required=False)
    county=forms.CharField(label='County', max_length=100, required=False)
    staff=forms.CharField(label='Staff', max_length=100, required=False)
    client=forms.CharField(label='Client', max_length=100, required=False)
    buyer=forms.CharField(label='Buyer', max_length=100, required=False)
    buyer_firm=forms.CharField(label='Buyers Firm', max_length=100, required=False)
    buyer_phone=forms.CharField(label='Buyer Phone', max_length=100, required=False)
    seller=forms.CharField(label='Seller', max_length=100, required=False)
    seller_firm= forms.CharField(label='Seller Firm', max_length=100, required=False)
    seller_phone=forms.CharField(label='Seller Phone', max_length=100, required=False)
    property=forms.CharField(label='Property Address', max_length=100, required=False)
    lot_no=forms.CharField(label='Lot No.', max_length=100, required=False)
    purchase=forms.CharField(label='Purchase Price', max_length=100, required=False)
    downpay=forms.CharField(label='Down Payment', max_length=100, required=False)
    attorney=forms.CharField(label='Attorney', max_length=100, required=False)
    attorney_firm=forms.CharField(label='Attorney Firm', max_length=100, required=False)
    attorney_phone=forms.CharField(label='Attorney Phone', max_length=100, required=False)
    lender=forms.CharField(label='Lender', max_length=100, required=False)
    loan_office=forms.CharField(label='Loan Office', max_length=100, required=False)
    lender_phone=forms.CharField(label='Lender Phone', max_length=100, required=False)
    broker=forms.CharField(label='Broker', max_length=100, required=False)
    broker_firm=forms.CharField(label='Broker Firm', max_length=100, required=False)
    broker_phone=forms.CharField(label='Broker Phone', max_length=100, required=False)

















