from django.db import models

# Create your models here.

class Tru_gio(models.Model):
    # ngay_tao = models.DateTimeField(auto_now_add = True)
    ngay_tao = models.CharField(max_length=250)
    ten = models.CharField(max_length=250)
    cong_suat = models.FloatField(default = 0)
    lat = models.FloatField(default = 0)
    long = models.FloatField(default = 0)

class Thong_so(models.Model):
    # ngay_tao = models.DateTimeField(auto_now_add = True)
    ngay_tao = models.CharField(max_length=250)
    WG = models.ForeignKey(Tru_gio, on_delete = models.CASCADE)
    Most_restrictive_WTG_Status=models.FloatField(default=0)
    Average_Active_Power=models.FloatField(default=0)
    Average_Ambient_Temperature=models.FloatField(default=0)
    Average_Generator_Speed=models.FloatField(default=0)
    Average_Nacelle_Position=models.FloatField(default=0)
    Average_Rotor_Speed=models.FloatField(default=0)
    Average_Stator_Active_Power=models.FloatField(default=0)
    Average_Wind_Speed=models.FloatField(default=0)
    Bearing_D_E_Temperature=models.FloatField(default=0)
    Bearing_D_E_Temperature_max=models.FloatField(default=0)
    Bearing_N_D_E_Temperature=models.FloatField(default=0)
    Bearing_N_D_E_Temperature max=models.FloatField(default=0)
    Gearbox_bearing_temperature=models.FloatField(default=0)
    Gearbox_bearing_temperature_max=models.FloatField(default=0)
    Gearbox_oil_temperature=models.FloatField(default=0)
    Gearbox_oil_temperaturemax=models.FloatField(default=0)
    Generator_windings_temperature_1=models.FloatField(default=0)
    Generator_windings_temperature_1_max=models.FloatField(default=0)
    Generator_windings_temperature_2=models.FloatField(default=0)
    Generator_windings_temperature_2_max=models.FloatField(default=0)
    Generator_windings_temperature_3=models.FloatField(default=0)
    Generator_windings_temperature_3_max=models.FloatField(default=0)
    Generators_sliprings_temperature=models.FloatField(default=0)
    Generators_sliprings-temperature_max=models.FloatField(default=0)
    Hidraulic_group_pressure=models.FloatField(default=0)
    Mean_theoretical_power_last_10_minutes=models.FloatField(default=0)
    Nacelle_Misalignment_and_Average_Wind_Direction=models.FloatField(default=0)
    Trafo_1_winding_temperature=models.FloatField(default=0)
    Trafo_1_winding_temperature_max=models.FloatField(default=0)
    Trafo_2_winding_temperature=models.FloatField(default=0)
    Trafo_2_winding_temperature_max=models.FloatField(default=0)
    Trafo_3_winding_temperature=models.FloatField(default=0)
    Trafo_3_winding_temperature_max=models.FloatField(default=0)





