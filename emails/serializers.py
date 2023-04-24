from rest_framework import serializers
from . import models

class ContactFormSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = models.ContactForm

class BillingSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = models.Billing