from django.shortcuts import render
from rest_framework import viewsets

from .models import Tru_gio, Thong_so
from .serializers import Tru_gioSerializer, Thong_soSerializer

# Create your views here.
class Tru_gioviewSet(viewsets.ModelViewSet):
    queryset = Tru_gio.objects.all()
    serializer_class = Tru_gioSerializer

class Thong_soviewSet(viewsets.ModelViewSet):
    queryset = Thong_so.objects.all()
    serializer_class = Thong_soSerializer