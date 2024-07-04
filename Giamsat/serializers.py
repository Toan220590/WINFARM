from rest_framework import serializers
from .models import Tru_gio, Thong_so

class Tru_gioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tru_gio
        fields = ('id','ngay_tao', 'ten','cong_suat','lat','long')

class Thong_soSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thong_so
        fields = ('id','ngay_tao', 'Most_restrictive_WTG_Status','Average_Active_Power','WG')