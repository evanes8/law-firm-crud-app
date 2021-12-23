from django.contrib.auth.models import User, Group
from rest_framework import serializers
from lion4.models import Record, Contact, Record_Contact


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Record
        fields=['matter_ref', 'code', 'matter_no', 'county', 'staff', 'property', 
                'lot_no', 'purchase', 'downpay']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=['name', 'firm', 'phone', 'fax', 'email']



class RelationshipSerializer(serializers.ModelSerializer):
    record=RecordSerializer()
    contact=ContactSerializer()

    class Meta:
        model = Record_Contact
        fields = ['record', 'contact', 'is_client', 'role']

#This works but record and contact need to be previusly created and unique based on their 
#non primary key data. need to make it so on post, primary keys for the record and contact
#are passed instead of all the other data
    def create(self, validated_data): 
        record_data = validated_data.pop('record')
        contact_data=validated_data.pop('contact')
        record = Record.objects.get(**record_data)
        contact = Contact.objects.get(**contact_data)
        relationship=Record_Contact.objects.create(record=record, contact=contact, **validated_data)
        return relationship

