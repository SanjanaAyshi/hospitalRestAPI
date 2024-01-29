#onk dhoronew serializer
from django.shortcuts import render
#viewset ta import kore nilam
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers

class ServicesViewset(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServicesSerializer