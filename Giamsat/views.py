from django.shortcuts import render
from rest_framework import viewsets

from .models import Tru_gio, Data
from .serializers import Tru_gioSerializer, DataSerializer

# Create your views here.
class Tru_gioviewSet(viewsets.ModelViewSet):
    queryset = Tru_gio.objects.all()
    serializer_class = Tru_gioSerializer

class DataviewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer