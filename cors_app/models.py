from django.db import models
import os
from django.utils.text import slugify
from django.core.files.storage import default_storage
from django.utils import timezone

# Create your models here.


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    controlcentre = models.BooleanField('control centre', default=False)
    vendor = models.BooleanField('vendor', default=False)
    gdc = models.BooleanField('gdc', default=False)
    mobileno = models.CharField(max_length=10)
    is_approved = models.BooleanField(default=False)  # Add this field
   

class CorsAppVendorData(models.Model):
    vendorid = models.AutoField(primary_key=True)
    corsid = models.CharField(max_length=100, blank=True, null=True)
    state_name = models.CharField(max_length=100, blank=True, null=True)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    last_date_of_site_visit = models.CharField(max_length=100, blank=True, null=True)
    date_of_installation = models.CharField(max_length=100, blank=True, null=True)
    date_of_monumentation = models.CharField(max_length=100, blank=True, null=True)
    station_status = models.CharField(max_length=100, blank=True, null=True)
    dimension_of_pillar = models.CharField(max_length=100, blank=True, null=True)
    height_of_bottom_of_antenna_from_base_of_pillar = models.CharField(max_length=100, blank=True, null=True)
    height_of_bottom_of_antenna_from_top_of_base_plate = models.CharField(max_length=100, blank=True, null=True)
    height_of_bottom_of_antenna_from_solar_panel_lower_angle_bottom = models.CharField(max_length=100, blank=True, null=True)
    dimension_of_pedestal = models.CharField(max_length=100, blank=True, null=True)
    electricity_provider = models.CharField(max_length=100, blank=True, null=True)
    electricity_meter_no = models.CharField(max_length=100, blank=True, null=True)
    twonumber_of_solar_panels = models.CharField(max_length=100, blank=True, null=True)
    capacity_of_solar_panel = models.CharField(max_length=100, blank=True, null=True)
    serial_no_of_solar_panels1and2 = models.CharField(max_length=100, blank=True, null=True)
    batteries_12v_2 = models.CharField(max_length=100, blank=True, null=True)
    company_name_and_no_of_batteries = models.CharField(max_length=100, blank=True, null=True)
    company_name_of_sim1 = models.CharField(max_length=100, blank=True, null=True)
    sim1_plan_validity_and_sim1_no = models.CharField(max_length=100, blank=True, null=True)
    company_name_of_sim2 = models.CharField(max_length=100, blank=True, null=True)
    sim2_plan_validity_and_sim2_no = models.CharField(max_length=100, blank=True, null=True)
    company_name_and_no_of_broadband = models.CharField(max_length=100, blank=True, null=True)
    broadband_plan_validity = models.CharField(max_length=100, blank=True, null=True)
    antenna_type_and_serial_no = models.CharField(max_length=100, blank=True, null=True)
    date_of_installation_of_antenna = models.CharField(max_length=100, blank=True, null=True)
    offset_parameter_of_antenna = models.FileField(upload_to ='image/',blank=True, null=True)
    receiver_model_name_and_serial_no = models.CharField(max_length=100, blank=True, null=True)
    date_of_installation_of_receiver_and_firmware = models.CharField(max_length=100, blank=True, null=True)
    date_of_installation_of_radome_and_serial_no = models.CharField(max_length=100, blank=True, null=True)
    serial_no_of_meteorological_sensor = models.CharField(max_length=100, blank=True, null=True)
    date_of_installation_of_meteorological_sensor = models.CharField(max_length=100, blank=True, null=True)
    meteorological_sensor_type_and_firmware = models.CharField(max_length=100, blank=True, null=True)
    logging_interval_of_gnss_data = models.CharField(max_length=100, blank=True, null=True)
    gnss_data_frequencies = models.CharField(max_length=500, blank=True, null=True)
    vendor_time = models.TextField(db_column='vendor_time', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    image_east = models.FileField(upload_to ='image/',blank=True, null=True)
    image_west = models.FileField(upload_to ='image/',blank=True, null=True)
    image_north = models.FileField(upload_to ='image/',blank=True, null=True)
    image_south = models.FileField(upload_to ='image/',blank=True, null=True)
    operationmaintainanceremark = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=45, default='Unverified')
    id = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cors_app_vendor_data'


    

class CorsAppGdcData(models.Model):
    gdcid = models.AutoField(primary_key=True)
    corsid = models.CharField(max_length=100, blank=True, null=True)
    site_name = models.TextField(blank=True, null=True)
    state_name = models.TextField(blank=True, null=True)
    dist_name = models.TextField(blank=True, null=True)
    tahsil_name = models.TextField(blank=True, null=True)
    corson = models.CharField(max_length=250, blank=True, null=True)
    verticality_of_antenna = models.CharField(max_length=250, blank=True, null=True)
    pin_code = models.CharField(max_length=100, blank=True, null=True)
    gdc_name = models.TextField(blank=True, null=True)
    person_of_gdc = models.TextField(blank=True, null=True)
    contact_no_of_gdc = models.TextField(blank=True, null=True)
    last_date_of_gdc_visit = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    image_east = models.FileField(upload_to ='image/',blank=True, null=True)
    image_west = models.FileField(upload_to ='image/',blank=True, null=True)
    image_north = models.FileField(upload_to ='image/',blank=True, null=True)
    image_south = models.FileField(upload_to ='image/',blank=True, null=True)
    closeup_image = models.FileField(upload_to ='uploads/',blank=True, null=True)
    id = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, default='Unverified')
    updatetime = models.CharField(max_length=100, blank=True, null=True)
    lastupdateby = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cors_app_gdc_data'

class CorsAppCentreData(models.Model):
    id = models.BigAutoField(primary_key=True)
    corsid = models.CharField(max_length=100, blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    site_name = models.TextField(blank=True, null=True)
    site_code = models.TextField(blank=True, null=True)
    coordinates_of_sites_dms_lat = models.TextField(blank=True, null=True)
    coordinates_of_sites_dms_long = models.TextField(blank=True, null=True)
    coordinates_of_sites_dms_elp_height = models.TextField(blank=True, null=True)
    digi_wr21_ip_dns_gateway_of_alloy_field = models.TextField(blank=True, null=True)
    digi_username_password = models.TextField(blank=True, null=True)
    alloy_cc_network_ip = models.TextField(blank=True, null=True)
    alloy_netmask = models.TextField(blank=True, null=True)
    alloy_local_wifi_ip = models.TextField(blank=True, null=True)
    alloy_username_and_password = models.TextField(blank=True, null=True)
    vendor_username = models.TextField(blank=True, null=True)
    gdc_username = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=45, default='Unverified')
    updatetime = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cors_app_centre_data'


    def __str__(Self):
        return Self.corsid





class CorsAppCentreDataBackup(models.Model):
    corsid = models.CharField(max_length=100, blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    site_name = models.TextField(blank=True, null=True)
    site_code = models.TextField(blank=True, null=True)
    coordinates_of_sites_dms_lat = models.TextField(blank=True, null=True)
    coordinates_of_sites_dms_long = models.TextField(blank=True, null=True)
    coordinates_of_sites_dms_elp_height = models.TextField(blank=True, null=True)
    digi_wr21_ip_dns_gateway_of_alloy_field = models.TextField(blank=True, null=True)
    digi_username_password = models.TextField(blank=True, null=True)
    alloy_cc_network_ip = models.TextField(blank=True, null=True)
    alloy_netmask = models.TextField(blank=True, null=True)
    alloy_local_wifi_ip = models.TextField(blank=True, null=True)
    alloy_username_and_password = models.TextField(blank=True, null=True)
    vendor_username = models.TextField(blank=True, null=True)
    gdc_username = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    updatetime = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cors_app_centre_data_backup'


class CorsAppGdcDataBackup(models.Model):
    corsid = models.CharField(max_length=100, blank=True, null=True)
    site_name = models.TextField(blank=True, null=True)
    state_name = models.TextField(blank=True, null=True)
    dist_name = models.TextField(blank=True, null=True)
    tahsil_name = models.TextField(blank=True, null=True)
    corson = models.CharField(max_length=250, blank=True, null=True)
    verticality_of_antenna = models.CharField(max_length=250, blank=True, null=True)
    pin_code = models.CharField(max_length=100, blank=True, null=True)
    gdc_name = models.TextField(blank=True, null=True)
    person_of_gdc = models.TextField(blank=True, null=True)
    contact_no_of_gdc = models.TextField(blank=True, null=True)
    last_date_of_gdc_visit = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    image_east = models.FileField(upload_to ='uploads/',blank=True, null=True)
    image_west = models.FileField(upload_to ='uploads/',blank=True, null=True)
    image_north = models.FileField(upload_to ='uploads/',blank=True, null=True)
    image_south = models.FileField(upload_to ='uploads/',blank=True, null=True)
    closeup_image = models.FileField(upload_to ='uploads/',blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    lastupdateby = models.CharField(max_length=200, blank=True, null=True)
    updatetime = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cors_app_gdc_data_backup'


class CorsAppVendorDataBackup(models.Model):
    vendorid = models.IntegerField(blank=True, null=True)
    corsid = models.CharField(max_length=100, blank=True, null=True)
    state_name = models.CharField(max_length=100, blank=True, null=True)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    last_date_of_site_visit = models.CharField(max_length=100, blank=True, null=True)
    date_of_installation = models.CharField(max_length=100, blank=True, null=True)
    date_of_monumentation = models.CharField(max_length=100, blank=True, null=True)
    station_status = models.CharField(max_length=100, blank=True, null=True)
    dimension_of_pillar = models.CharField(max_length=100, blank=True, null=True)
    height_of_bottom_of_antenna_from_base_of_pillar = models.CharField(max_length=100, blank=True, null=True)
    height_of_bottom_of_antenna_from_top_of_base_plate = models.CharField(max_length=100, blank=True, null=True)
    height_of_bottom_of_antenna_from_solar_panel_lower_angle_bottom = models.CharField(max_length=100, blank=True, null=True)
    dimension_of_pedestal = models.CharField(max_length=100, blank=True, null=True)
    electricity_provider = models.CharField(max_length=100, blank=True, null=True)
    electricity_meter_no = models.CharField(max_length=100, blank=True, null=True)
    twonumber_of_solar_panels = models.CharField(max_length=100, blank=True, null=True)
    capacity_of_solar_panel = models.CharField(max_length=100, blank=True, null=True)
    serial_no_of_solar_panels1and2 = models.CharField(max_length=100, blank=True, null=True)
    batteries_12v_2 = models.CharField(max_length=100, blank=True, null=True)
    company_name_and_no_of_batteries = models.CharField(max_length=100, blank=True, null=True)
    company_name_of_sim1 = models.CharField(max_length=100, blank=True, null=True)
    sim1_plan_validity_and_sim1_no = models.CharField(max_length=100, blank=True, null=True)
    company_name_of_sim2 = models.CharField(max_length=100, blank=True, null=True)
    sim2_plan_validity_and_sim2_no = models.CharField(max_length=100, blank=True, null=True)
    company_name_and_no_of_broadband = models.CharField(max_length=100, blank=True, null=True)
    broadband_plan_validity = models.CharField(max_length=100, blank=True, null=True)
    antenna_type_and_serial_no = models.CharField(max_length=100, blank=True, null=True)
    date_of_installation_of_antenna = models.CharField(max_length=100, blank=True, null=True)
    offset_parameter_of_antenna = models.CharField(max_length=100, blank=True, null=True)
    receiver_model_name_and_serial_no = models.CharField(max_length=100, blank=True, null=True)
    date_of_installation_of_receiver_and_firmware = models.CharField(max_length=100, blank=True, null=True)
    date_of_installation_of_radome_and_serial_no = models.CharField(max_length=100, blank=True, null=True)
    serial_no_of_meteorological_sensor = models.CharField(max_length=100, blank=True, null=True)
    date_of_installation_of_meteorological_sensor = models.CharField(max_length=100, blank=True, null=True)
    meteorological_sensor_type_and_firmware = models.CharField(max_length=100, blank=True, null=True)
    logging_interval_of_gnss_data = models.CharField(max_length=100, blank=True, null=True)
    gnss_data_frequencies = models.CharField(max_length=100, blank=True, null=True)
    vendor_time = models.TextField(db_column='vendor_time', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    image_east = models.FileField(upload_to ='uploads/',blank=True, null=True)
    image_west = models.FileField(upload_to ='uploads/',blank=True, null=True)
    image_north = models.FileField(upload_to ='uploads/',blank=True, null=True)
    image_south = models.FileField(upload_to ='uploads/',blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    operationmaintainanceremark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cors_app_vendor_data_backup'







class CorsAppCorsInventoryForOther(models.Model):
    id = models.BigAutoField(primary_key=True)
    departmentname = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    premise_address = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    district = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=250, blank=True, null=True)
    monument_type = models.CharField(max_length=250, blank=True, null=True)
    monument_stability = models.CharField(max_length=250, blank=True, null=True)
    gnss_receiver_make_and_model = models.CharField(max_length=250, blank=True, null=True)
    gnss_antenna_make_and_model = models.CharField(max_length=250, blank=True, null=True)
    obstructions_to_antenna = models.TextField(blank=True, null=True)
    image_east = models.FileField(upload_to ='otherimg/',blank=True, null=True)
    image_west = models.FileField(upload_to ='otherimg/',blank=True, null=True)
    image_north = models.FileField(upload_to ='otherimg/',blank=True, null=True)
    image_south = models.FileField(upload_to ='otherimg/',blank=True, null=True)
    pdf_form = models.FileField(upload_to ='otherimg/',blank=True, null=True)
    persion_contact_no = models.CharField(max_length=250, blank=True, null=True)
    persion_name = models.CharField(max_length=250, blank=True, null=True)
    power = models.CharField(max_length=250, blank=True, null=True)
    probable_multipath_and_electro_megnetic_interference = models.CharField(max_length=250, blank=True, null=True)
    data_transmission = models.CharField(max_length=250, blank=True, null=True)
    online_transmission = models.CharField(max_length=250, blank=True, null=True)
    availability_of_gsm_4g_connection = models.CharField(max_length=250, blank=True, null=True)
    availability_of_broadband_connection = models.CharField(max_length=250, blank=True, null=True)
    availability_of_electric_surge_or_lightening_conductors = models.CharField(max_length=250, blank=True, null=True)
    access_control = models.CharField(max_length=250, blank=True, null=True)
    operation_and_maintenance = models.CharField(max_length=250, blank=True, null=True)
    gdc_username = models.CharField(max_length=250, blank=True, null=True)
    probablemultipath = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cors_app_cors_inventory_for_other'


class PlotAppDistrict(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    state = models.ForeignKey('PlotAppState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'plot_app_district'


class PlotAppPlotData(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    site_name = models.TextField(blank=True, null=True)
    site_code = models.TextField(blank=True, null=True)
    image_Cycle_Slip_PLOT = models.ImageField(upload_to='media')
    image_MP_PLOT = models.ImageField(upload_to='media')
    image_Percentage_Observation = models.ImageField(upload_to='media')
    image_TS_PLOT = models.ImageField(upload_to='media')
    coordinates = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plot_app_plot_data'


class PlotAppSitedata(models.Model):
    id = models.BigAutoField(primary_key=True)
    corsid = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    site_name = models.CharField(max_length=100)
    site_code = models.CharField(max_length=10)
    coordinates_of_sites_dms_lat = models.CharField(max_length=50)
    coordinates_of_sites_dms_long = models.CharField(max_length=50)
    coordinates_of_sites_dms_elp_height = models.FloatField()

    class Meta:
        managed = False
        db_table = 'plot_app_sitedata'


class PlotAppState(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'plot_app_state'




######################################################################### GRMDB #####################################################



    
class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


# class gtstation(models.Model):
#     keyid = models.CharField(max_length=200,blank=True, null=True)
#     gtstation_name = models.CharField(max_length=200,blank=True, null=True)
#     pamphlet_no = models.CharField(max_length=200,blank=True, null=True)
#     state = models.CharField(max_length=200,blank=True, null=True)
#     ellipsoidheight = models.CharField(max_length=200,blank=True, null=True)
#     triangulatedheight = models.CharField(max_length=200,blank=True, null=True)
#     orthometrichight = models.CharField(max_length=200,blank=True, null=True)
#     gravityvalue = models.CharField(max_length=200,blank=True, null=True)
#     district = models.CharField(max_length=200,blank=True, null=True)
#     tahsil = models.CharField(max_length=200,blank=True, null=True)
#     pincode = models.CharField(max_length=200,blank=True, null=True)
#     longitude = models.CharField(max_length=200,blank=True, null=True)
#     latitude = models.CharField(max_length=200,blank=True, null=True)
#     gt_station_inscription = models.CharField(max_length=200,blank=True, null=True)
#     old_description = models.TextField(blank=True, null=True)
#     revised_description = models.TextField(blank=True, null=True)
#     conduction_of_gtstation = models.CharField(max_length=500,blank=True, null=True)
#     image_east = models.ImageField(upload_to ='image/',blank=True, null=True)
#     image_west = models.ImageField(upload_to ='image/',blank=True, null=True)
#     image_north = models.ImageField(upload_to ='image/',blank=True, null=True)
#     image_south = models.ImageField(upload_to ='image/',blank=True, null=True)
#     authorised_person_name_and_designation = models.CharField(max_length=500,blank=True, null=True)
#     authorised_person_contactno = models.CharField(max_length=500,blank=True, null=True) 
#     last_date_of_vist = models.CharField(max_length=500,blank=True, null=True)
#     inspection_remark = models.CharField(max_length=500,blank=True, null=True)
#     updatetime = models.CharField(max_length=500,blank=True, null=True)
#     gdc_username = models.TextField(blank=True, null=True)

   


class BenchmarkGtstation(models.Model):
    id = models.BigAutoField(primary_key=True)
    gtstation_name = models.CharField(max_length=200, blank=True, null=True)
    pamphlet_no = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    district = models.CharField(max_length=200, blank=True, null=True)
    tahsil = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    gt_station_inscription = models.CharField(max_length=200, blank=True, null=True)
    ellipsoidheight = models.CharField(max_length=200, blank=True, null=True)
    old_description = models.TextField(blank=True, null=True)
    revised_description = models.TextField(blank=True, null=True)
    conduction_of_gtstation = models.CharField(max_length=500, blank=True, null=True)
    image_east = models.CharField(max_length=100, blank=True, null=True)
    authorised_person_name_and_designation = models.CharField(max_length=500, blank=True, null=True)
    authorised_person_contactno = models.CharField(max_length=500, blank=True, null=True)
    last_date_of_vist = models.CharField(max_length=500, blank=True, null=True)
    inspection_remark = models.TextField(blank=True, null=True)
    gdc_username = models.TextField(blank=True, null=True)
    image_east = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_west = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_north = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_south = models.ImageField(upload_to ='image/',blank=True, null=True)
    closeup_image = models.FileField(upload_to ='image/',blank=True, null=True)
    keyid = models.CharField(max_length=200, blank=True, null=True)
    updatetime = models.CharField(max_length=500, blank=True, null=True)
    gravityvalue = models.CharField(max_length=200, blank=True, null=True)
    orthometrichight = models.CharField(max_length=200, blank=True, null=True)
    triangulatedheight = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, default='unverified')
    lastupdateby = models.CharField(max_length=200, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'benchmark_gtstation' 

    def save(self, *args, **kwargs):
        if not self.keyid:
            last_entry = BenchmarkGtstation.objects.using("database3").all().order_by('id').last()
            if last_entry:
                last_keyid = last_entry.keyid
                new_keyid = int(last_keyid[3:]) + 1
                self.keyid = 'GTS' + str(new_keyid).zfill(4)
            else:
                self.keyid = 'GTS0001'
        super(BenchmarkGtstation, self).save(*args, **kwargs)

      

# class gcpdata(models.Model):
#     keyid = models.CharField(max_length=200,blank=True, null=True)
#     gcp_name = models.CharField(max_length=200,blank=True, null=True)
#     pamphlet_no = models.CharField(max_length=200,blank=True, null=True)
#     state = models.CharField(max_length=200,blank=True, null=True)
#     district = models.CharField(max_length=200,blank=True, null=True)
#     tahsil = models.CharField(max_length=200,blank=True, null=True)
#     pincode = models.CharField(max_length=200,blank=True, null=True)
#     longitude = models.CharField(max_length=200,blank=True, null=True)
#     latitude = models.CharField(max_length=200,blank=True, null=True)
#     ellipsoidheight = models.CharField(max_length=200,blank=True, null=True)
#     orthometrichight = models.CharField(max_length=200,blank=True, null=True)
#     gravityvalue = models.CharField(max_length=200,blank=True, null=True)
#     gcp_on_pillar =  models.CharField(max_length=500,blank=True, null=True)
#     old_description = models.TextField(blank=True, null=True)
#     revised_description = models.TextField(blank=True, null=True)
#     conduction_of_gcp = models.CharField(max_length=500,blank=True, null=True)
#     image_east = models.ImageField(upload_to ='image/',blank=True, null=True)
#     image_west = models.ImageField(upload_to ='image/',blank=True, null=True)
#     image_north = models.ImageField(upload_to ='image/',blank=True, null=True)
#     image_south = models.ImageField(upload_to ='image/',blank=True, null=True)
#     authorised_person_name_and_designation = models.CharField(max_length=500,blank=True, null=True)
#     authorised_person_contactno = models.CharField(max_length=500,blank=True, null=True) 
#     last_date_of_vist = models.CharField(max_length=500,blank=True, null=True)
#     inspection_remark = models.CharField(max_length=500,blank=True, null=True)
#     updatetime = models.CharField(max_length=500,blank=True, null=True)
#     gdc_username = models.TextField(blank=True, null=True)
#     pid = models.CharField(max_length=500,blank=True, null=True)


class BenchmarkGcpdata(models.Model):
    id = models.BigAutoField(primary_key=True)
    gcp_name = models.CharField(max_length=200, blank=True, null=True)
    pamphlet_no = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    district = models.CharField(max_length=200, blank=True, null=True)
    tahsil = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    gcp_on_pillar = models.CharField(max_length=500, blank=True, null=True)
    sketch = models.ImageField(upload_to='media')
    unid = models.CharField(max_length=200,blank=True, null=True)
    old_description = models.TextField(blank=True, null=True)
    revised_description = models.TextField(blank=True, null=True)
    conduction_of_gcp = models.CharField(max_length=500, blank=True, null=True)
    authorised_person_name_and_designation = models.CharField(max_length=500, blank=True, null=True)
    authorised_person_contactno = models.CharField(max_length=500, blank=True, null=True)
    last_date_of_vist = models.CharField(max_length=500, blank=True, null=True)
    inspection_remark = models.TextField(blank=True, null=True)
    gdc_username = models.TextField(blank=True, null=True)
    ellipsoidheight = models.CharField(max_length=200, blank=True, null=True)
    pid = models.CharField(max_length=500, blank=True, null=True)
    image_east = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_west = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_north = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_south = models.ImageField(upload_to ='image/',blank=True, null=True)
    closeup_image = models.FileField(upload_to ='image/',blank=True, null=True)
    keyid = models.CharField(max_length=200, blank=True, null=True)
    updatetime = models.CharField(max_length=500, blank=True, null=True)
    gravityvalue = models.CharField(max_length=200, blank=True, null=True)
    orthometrichight = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, default='unverified')
    lastupdateby = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'benchmark_gcpdata'

# class sbmdata(models.Model):
#     keyid = models.CharField(max_length=200,blank=True, null=True)
#     sbm_type = models.CharField(max_length=200,blank=True, null=True)
#     pamphlet_no = models.CharField(max_length=200,blank=True, null=True)
#     state = models.CharField(max_length=200,blank=True, null=True)
#     district = models.CharField(max_length=200,blank=True, null=True)
#     tahsil = models.CharField(max_length=200,blank=True, null=True)
#     pincode = models.CharField(max_length=200,blank=True, null=True)
#     longitude = models.CharField(max_length=200,blank=True, null=True)
#     latitude = models.CharField(max_length=200,blank=True, null=True)
#     sbm_inscription =  models.CharField(max_length=500,blank=True, null=True)
#     old_description = models.CharField(max_length=500,blank=True, null=True)
#     revised_description = models.CharField(max_length=500,blank=True, null=True)
#     conduction_of_sbm = models.CharField(max_length=500,blank=True, null=True)
#     conduction_of_reference_pillar = models.CharField(max_length=500,blank=True, null=True)
#     image_east = models.ImageField(upload_to ='image/',blank=True, null=True)
#     image_west = models.ImageField(upload_to ='image/',blank=True, null=True)
#     image_north = models.ImageField(upload_to ='image/',blank=True, null=True)
#     image_south = models.ImageField(upload_to ='image/',blank=True, null=True)
#     authorised_person_name_and_designation = models.CharField(max_length=500,blank=True, null=True)
#     authorised_person_contactno = models.CharField(max_length=500,blank=True, null=True) 
#     last_date_of_vist = models.CharField(max_length=500,blank=True, null=True)
#     inspection_remark = models.CharField(max_length=500,blank=True, null=True)
#     updatetime = models.CharField(max_length=500,blank=True, null=True)
#     gdc_username = models.TextField(blank=True, null=True)
 

class BenchmarkSbmdata(models.Model):
    id = models.BigAutoField(primary_key=True)
    sbm_type = models.CharField(max_length=200, blank=True, null=True)
    pamphlet_no = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    district = models.CharField(max_length=200, blank=True, null=True)
    tahsil = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    sbm_inscription = models.TextField(blank=True, null=True)
    old_description = models.TextField(blank=True, null=True)
    revised_description = models.TextField(blank=True, null=True)
    conduction_of_sbm = models.CharField(max_length=500, blank=True, null=True)
    conduction_of_reference_pillar = models.CharField(max_length=500, blank=True, null=True)
    authorised_person_name_and_designation = models.CharField(max_length=500, blank=True, null=True)
    authorised_person_contactno = models.CharField(max_length=500, blank=True, null=True)
    last_date_of_vist = models.CharField(max_length=500, blank=True, null=True)
    inspection_remark = models.TextField(blank=True, null=True)
    gdc_username = models.TextField(blank=True, null=True)
    gravityvalue = models.CharField(max_length=200, blank=True, null=True)
    image_east = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_west = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_north = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_south = models.ImageField(upload_to ='image/',blank=True, null=True)
    closeup_image = models.FileField(upload_to ='image/',blank=True, null=True)
    keyid = models.CharField(max_length=200, blank=True, null=True)
    updatetime = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=20, default='unverified')
    lastupdateby = models.CharField(max_length=200, blank=True, null=True)

    
    

    def save(self, *args, **kwargs):
        if not self.keyid:
            last_entry = BenchmarkSbmdata.objects.using("database3").all().order_by('id').last()
            if last_entry:
                last_keyid = last_entry.keyid
                new_keyid = int(last_keyid[3:]) + 1
                self.keyid = 'SBM' + str(new_keyid).zfill(4)
            else:
                self.keyid = 'SBM0001'

        # Get the formatted date from last_date_of_vist
        formatted_date = timezone.now().strftime("%Y-%m-%d")
        
        
        if self.pk:  # Check if this is an existing record
            existing_entry = BenchmarkSbmdata.objects.using("database3").get(pk=self.pk)
            
            # Handle existing images
            if self.image_east and self.image_east != existing_entry.image_east:
                self._rename_image(self.image_east, "east", formatted_date)
            elif not self.image_east:
                self.image_east = existing_entry.image_east

            if self.image_west and self.image_west != existing_entry.image_west:
                self._rename_image(self.image_west, "west", formatted_date)
            elif not self.image_west:
                self.image_west = existing_entry.image_west

            if self.image_north and self.image_north != existing_entry.image_north:
                self._rename_image(self.image_north, "north", formatted_date)
            elif not self.image_north:
                self.image_north = existing_entry.image_north

            if self.image_south and self.image_south != existing_entry.image_south:
                self._rename_image(self.image_south, "south", formatted_date)
            elif not self.image_south:
                self.image_south = existing_entry.image_south

            if self.closeup_image and self.closeup_image != existing_entry.closeup_image:
                self._rename_image(self.closeup_image, "closeup_image", formatted_date)
            elif not self.closeup_image:
                self.closeup_image = existing_entry.closeup_image    

        super(BenchmarkSbmdata, self).save(*args, **kwargs)

    def _rename_image(self, image_field, direction, formatted_date):
        if image_field:
            ext = os.path.splitext(image_field.name)[-1]
            new_name = f"{self.keyid}_{direction}_{formatted_date}{ext}"
            image_field.name = os.path.join('image', new_name)
            # Remove old file if it exists
            if default_storage.exists(image_field.path):
                default_storage.delete(image_field.path)

    class Meta:
        managed = False
        db_table = 'benchmark_sbmdata'

    # def save(self, *args, **kwargs):
    #     if not self.keyid:
    #         last_entry = BenchmarkSbmdata.objects.using("database3").all().order_by('id').last()
    #         if last_entry:
    #             last_keyid = last_entry.keyid
    #             new_keyid = int(last_keyid[3:]) + 1
    #             self.keyid = 'SBM' + str(new_keyid).zfill(4)
    #         else:
    #             self.keyid = 'SBM0001'
    #     super(BenchmarkSbmdata, self).save(*args, **kwargs) 

    # class Meta:
    #     managed = False
    #     db_table = 'benchmark_sbmdata'


       

    

class BenchmarkSbmdataBackup(models.Model):
    keyid = models.CharField(max_length=200, blank=True, null=True)
    sbm_type = models.CharField(max_length=200, blank=True, null=True)
    pamphlet_no = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    district = models.CharField(max_length=200, blank=True, null=True)
    tahsil = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    sbm_inscription = models.TextField(blank=True, null=True)
    old_description = models.TextField(blank=True, null=True)
    revised_description = models.TextField(blank=True, null=True)
    conduction_of_sbm = models.CharField(max_length=500, blank=True, null=True)
    conduction_of_reference_pillar = models.CharField(max_length=500, blank=True, null=True)
    image_east = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_west = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_north = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_south = models.ImageField(upload_to ='image/',blank=True, null=True)
    closeup_image = models.FileField(upload_to ='image/',blank=True, null=True)
    authorised_person_name_and_designation = models.CharField(max_length=500, blank=True, null=True)
    authorised_person_contactno = models.CharField(max_length=500, blank=True, null=True)
    last_date_of_vist = models.CharField(max_length=500, blank=True, null=True)
    inspection_remark = models.TextField(blank=True, null=True)
    updatetime = models.CharField(max_length=500, blank=True, null=True)
    gravityvalue = models.CharField(max_length=200, blank=True, null=True)
    gdc_username = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    lastupdateby = models.CharField(max_length=200, blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'benchmark_sbmdata_backup'


class BenchmarkGcpdataBackup(models.Model):
    keyid = models.CharField(max_length=200, blank=True, null=True)
    gcp_name = models.CharField(max_length=200, blank=True, null=True)
    pamphlet_no = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    district = models.CharField(max_length=200, blank=True, null=True)
    tahsil = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    ellipsoidheight = models.CharField(max_length=200, blank=True, null=True)
    orthometrichight = models.CharField(max_length=200, blank=True, null=True)
    gravityvalue = models.CharField(max_length=200, blank=True, null=True)
    gcp_on_pillar = models.CharField(max_length=500, blank=True, null=True)
    old_description = models.TextField(blank=True, null=True)
    revised_description = models.TextField(blank=True, null=True)
    conduction_of_gcp = models.CharField(max_length=500, blank=True, null=True)
    image_east = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_west = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_north = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_south = models.ImageField(upload_to ='image/',blank=True, null=True)
    closeup_image = models.FileField(upload_to ='image/',blank=True, null=True)
    authorised_person_name_and_designation = models.CharField(max_length=500, blank=True, null=True)
    authorised_person_contactno = models.CharField(max_length=500, blank=True, null=True)
    last_date_of_vist = models.CharField(max_length=500, blank=True, null=True)
    inspection_remark = models.TextField(blank=True, null=True)
    updatetime = models.CharField(max_length=500, blank=True, null=True)
    gdc_username = models.TextField(blank=True, null=True)
    pid = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    lastupdateby = models.CharField(max_length=200, blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'benchmark_gcpdata_backup'


class BenchmarkGtstationBackup(models.Model):
    keyid = models.CharField(max_length=200, blank=True, null=True)
    gtstation_name = models.CharField(max_length=200, blank=True, null=True)
    pamphlet_no = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    ellipsoidheight = models.CharField(max_length=200, blank=True, null=True)
    triangulatedheight = models.CharField(max_length=200, blank=True, null=True)
    orthometrichight = models.CharField(max_length=200, blank=True, null=True)
    gravityvalue = models.CharField(max_length=200, blank=True, null=True)
    district = models.CharField(max_length=200, blank=True, null=True)
    tahsil = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    gt_station_inscription = models.CharField(max_length=200, blank=True, null=True)
    old_description = models.TextField(blank=True, null=True)
    revised_description = models.TextField(blank=True, null=True)
    conduction_of_gtstation = models.CharField(max_length=500, blank=True, null=True)
    image_east = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_west = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_north = models.ImageField(upload_to ='image/',blank=True, null=True)
    image_south = models.ImageField(upload_to ='image/',blank=True, null=True)
    closeup_image = models.FileField(upload_to ='image/',blank=True, null=True)
    authorised_person_name_and_designation = models.CharField(max_length=500, blank=True, null=True)
    authorised_person_contactno = models.CharField(max_length=500, blank=True, null=True)
    last_date_of_vist = models.CharField(max_length=500, blank=True, null=True)
    inspection_remark = models.TextField(blank=True, null=True)
    updatetime = models.CharField(max_length=500, blank=True, null=True)
    gdc_username = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    lastupdateby = models.CharField(max_length=200, blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'benchmark_gtstation_backup'



