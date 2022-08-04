from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from myapi.models import Hero
from myapi.serializers import HeroSerializer

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('fullname')
    serializer_class = HeroSerializer
    pass