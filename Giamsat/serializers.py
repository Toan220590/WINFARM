from rest_framework import serializers
from .models import Tru_gio, Data

class Tru_gioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tru_gio
        fields = ('id','ngay_tao', 'ten','cong_suat','lat','long')

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
