#onk dhoronew serializer
from django.shortcuts import render
#viewset ta import kore nilam
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers

class ContactusViewset(viewsets.ModelViewSet):
    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer