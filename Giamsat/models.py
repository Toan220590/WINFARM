from django.db import models

# Create your models here.

class Tru_gio(models.Model):
    ngay_tao = models.DateTimeField(auto_now_add = True)
    ten = models.CharField(max_length=250)
    cong_suat = models.FloatField(default = 0)
    lat = models.FloatField(default = 0)
    long = models.FloatField(default = 0)

class Thong_so(models.Model):
    ngay_tao = models.DateTimeField(auto_now_add = True)
    Most_restrictive_WTG_Status=models.FloatField(default=0)
    Average_Active_Power=models.FloatField(default=0)
    WG = models.ForeignKey(Tru_gio, on_delete = models.CASCADE)

