from rest_framework import serializers
from .models import Tru_gio, Thong_so

class Tru_gioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tru_gio
        fields = ('id','ngay_tao', 'ten','cong_suat','lat','long')

class Thong_soSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thong_so
        fields = ('id','ngay_tao','WG','Most_restrictive_WTG_Status','Average_Active_Power','Average_Ambient_Temperature','Average_Generator_Speed','Average_Nacelle_Position','Average_Rotor_Speed','Average_Stator_Active_Power','Average_Wind_Speed','Bearing_D_E_Temperature','Bearing_D_E_Temperature_max','Bearing_N_D_E_Temperature','Bearing_N_D_E_Temperature_max','Gearbox_bearing_temperature','Gearbox_bearing_temperature_max','Gearbox_oil_temperature','Gearbox_oil_temperaturemax','Generator_windings_temperature_1','Generator_windings_temperature_1_max','Generator_windings_temperature_2','Generator_windings_temperature_2_max','Generator_windings_temperature_3','Generator_windings_temperature_3_max','Generators_sliprings_temperature','Generators_sliprings_temperature_max','Hidraulic_group_pressure','Mean_theoretical_power_last_10_minutes','Nacelle_Misalignment_and_Average_Wind_Direction','Trafo_1_winding_temperature','Trafo_1_winding_temperature_max','Trafo_2_winding_temperature','Trafo_2_winding_temperature_max','Trafo_3_winding_temperature','Trafo_3_winding_temperature_max')