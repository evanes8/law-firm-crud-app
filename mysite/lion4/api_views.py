from .models import Record, Contact, Record_Contact
from .serializers import RecordSerializer, ContactSerializer, RelationshipSerializer, NoRecordRelationshipSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RecordList(APIView):
    """
    List all Records, or create a new Record.
    """
    def get(self, request, format=None):
        records = Record.objects.all()
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecordDetail(APIView):
    """
    Retrieve, update or delete a record instance.
    """
    def get_object(self, pk):
        try:
            return Record.objects.get(pk=pk)
        except Record.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        record = self.get_object(pk)
        serializer = RecordSerializer(record)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        record = self.get_object(pk)
        serializer = RecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        record = self.get_object(pk)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class ContactList(APIView):
    """
    List all Records, or create a new Record.
    """
    def get(self, request, format=None):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class RelationshipList(APIView):
    """
    List all Relationships
    """
    def get(self, request, format=None):
        relationships = Record_Contact.objects.all()
        serializer = RelationshipSerializer(relationships, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RelationshipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RelatedContactList(APIView):
    def get_object(self, pk):
        try:
            return Record.objects.get(pk=pk)
        except Record.DoesNotExist:
            raise Http404
   
    def get(self, request, pk, format=None):
        record = self.get_object(pk)
        relationships=record.record_contact_set.all()
        serializer = NoRecordRelationshipSerializer(relationships, many=True)
        return Response(serializer.data)

