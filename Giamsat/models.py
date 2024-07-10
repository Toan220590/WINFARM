from django.db import models

# Create your models here.

class Tru_gio(models.Model):
    # ngay_tao = models.DateTimeField(auto_now_add = True)
    ngay_tao = models.CharField(max_length=250)
    ten = models.CharField(max_length=250)
    cong_suat = models.FloatField(default = 0)
    lat = models.FloatField(default = 0)
    long = models.FloatField(default = 0)
    def __str__(self):
        return self.ten

class Data(models.Model):
    tru_gio = models.ForeignKey(Tru_gio, related_name='data', on_delete=models.CASCADE)
    Date = models.CharField(max_length=255, null=True, blank=True)
    Most_restrictive_WTG_Status_10M = models.FloatField(default=0)
    WTG_nacelle_position_corrected_Average_10M = models.FloatField(default=0)
    Active_power_Std_Dev_10M = models.FloatField(default=0)
    Ambient_Temperature_Std_Dev_10M = models.FloatField(default=0)
    Average_Active_Power_10M = models.FloatField(default=0)
    Average_Ambient_Temperature_10M = models.FloatField(default=0)
    Average_Generator_Speed_10M = models.FloatField(default=0)
    Average_Grid_Voltage_10M = models.FloatField(default=0)
    Average_Nacelle_Position_10M = models.FloatField(default=0)
    Average_Pitch_Angle_10M = models.FloatField(default=0)
    Average_Reactive_Power_10M = models.FloatField(default=0)
    Average_Rotor_Speed_10M = models.FloatField(default=0)
    Average_Stator_Active_Power_10M = models.FloatField(default=0)
    Average_Wind_Speed_10M = models.FloatField(default=0)
    Bearing_DE_Temperature_10M = models.FloatField(default=0)
    Bearing_DE_Temperature_dv_10M = models.FloatField(default=0)
    Bearing_DE_Temperature_max_10M = models.FloatField(default=0)
    Bearing_DE_Temperature_min_10M = models.FloatField(default=0)
    Bearing_NDE_Temperature_10M = models.FloatField(default=0)
    Bearing_NDE_Temperature_dv_10M = models.FloatField(default=0)
    Bearing_NDE_Temperature_max_10M = models.FloatField(default=0)
    Bearing_NDE_Temperature_min_10M = models.FloatField(default=0)
    Wind_farm_active_power_dv_10M = models.FloatField(default=0)
    Wind_farm_active_power_max_10M = models.FloatField(default=0)
    Wind_farm_active_power_min_10M = models.FloatField(default=0)

    # Tiếp tục thêm các trường khác tùy theo tên biến của bạn

    def __str__(self):
        return f"{self.Date}"