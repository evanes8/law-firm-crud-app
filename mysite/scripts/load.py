#import model
#import pandas
#access my pickel file 
import pandas as pd
from lion4.models import Record


def run():
    no_na= pd.read_pickle("no_na.pkl")
    no_na.fillna('', inplace=True)
    for index, row in no_na.iterrows():
        my_record= Record()
        my_record.matter_ref = row['matter_ref']
        my_record.code= row['code']
        my_record.matter_no = row['matter_no']
        my_record.county = row['county']
        my_record.staff = row['staff']
        my_record.buyer= row['buyer']
        my_record.buyer_firm= row['buyer_firm']
        my_record.buyer_phone= row['buyer_phone']
        my_record.seller=row['seller']
        my_record.seller_firm = row['seller_firm']
        my_record.seller_phone= row['seller_phone']
        my_record.client= row['client']
        my_record.property= row['property']
        my_record.lot_no= row['lot_no']
        my_record.purchase= row['purchase']
        my_record.downpay= row['downpay']
        my_record.attorney= row['attorney']
        my_record.attorney_firm= row['attorney_firm']
        my_record.attorney_phone= row['attorney_phone']
        my_record.lender = row['lender']
        my_record.loan_office= row['loan_office']
        my_record.lender_phone= row['lender_phone']
        my_record.broker= row['broker']
        my_record.broker_firm = row['broker_firm']
        my_record.broker_phone= row['broker_phone']
        my_record.save()







