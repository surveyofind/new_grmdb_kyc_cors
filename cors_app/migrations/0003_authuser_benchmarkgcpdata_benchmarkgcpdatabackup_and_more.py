# Generated by Django 5.0.7 on 2024-11-22 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cors_app', '0002_plotappdistrict_plotappplotdata_plotappsitedata_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BenchmarkGcpdata',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('gcp_name', models.CharField(blank=True, max_length=200, null=True)),
                ('pamphlet_no', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('district', models.CharField(blank=True, max_length=200, null=True)),
                ('tahsil', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.CharField(blank=True, max_length=200, null=True)),
                ('longitude', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.CharField(blank=True, max_length=200, null=True)),
                ('gcp_on_pillar', models.CharField(blank=True, max_length=500, null=True)),
                ('sketch', models.ImageField(upload_to='media')),
                ('unid', models.CharField(blank=True, max_length=200, null=True)),
                ('old_description', models.TextField(blank=True, null=True)),
                ('revised_description', models.TextField(blank=True, null=True)),
                ('conduction_of_gcp', models.CharField(blank=True, max_length=500, null=True)),
                ('authorised_person_name_and_designation', models.CharField(blank=True, max_length=500, null=True)),
                ('authorised_person_contactno', models.CharField(blank=True, max_length=500, null=True)),
                ('last_date_of_vist', models.CharField(blank=True, max_length=500, null=True)),
                ('inspection_remark', models.TextField(blank=True, null=True)),
                ('gdc_username', models.TextField(blank=True, null=True)),
                ('ellipsoidheight', models.CharField(blank=True, max_length=200, null=True)),
                ('pid', models.CharField(blank=True, max_length=500, null=True)),
                ('image_east', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_west', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_north', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_south', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('closeup_image', models.FileField(blank=True, null=True, upload_to='image/')),
                ('keyid', models.CharField(blank=True, max_length=200, null=True)),
                ('updatetime', models.CharField(blank=True, max_length=500, null=True)),
                ('gravityvalue', models.CharField(blank=True, max_length=200, null=True)),
                ('orthometrichight', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(default='unverified', max_length=20)),
                ('lastupdateby', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'benchmark_gcpdata',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BenchmarkGcpdataBackup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyid', models.CharField(blank=True, max_length=200, null=True)),
                ('gcp_name', models.CharField(blank=True, max_length=200, null=True)),
                ('pamphlet_no', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('district', models.CharField(blank=True, max_length=200, null=True)),
                ('tahsil', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.CharField(blank=True, max_length=200, null=True)),
                ('longitude', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.CharField(blank=True, max_length=200, null=True)),
                ('ellipsoidheight', models.CharField(blank=True, max_length=200, null=True)),
                ('orthometrichight', models.CharField(blank=True, max_length=200, null=True)),
                ('gravityvalue', models.CharField(blank=True, max_length=200, null=True)),
                ('gcp_on_pillar', models.CharField(blank=True, max_length=500, null=True)),
                ('old_description', models.TextField(blank=True, null=True)),
                ('revised_description', models.TextField(blank=True, null=True)),
                ('conduction_of_gcp', models.CharField(blank=True, max_length=500, null=True)),
                ('image_east', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_west', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_north', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_south', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('closeup_image', models.FileField(blank=True, null=True, upload_to='image/')),
                ('authorised_person_name_and_designation', models.CharField(blank=True, max_length=500, null=True)),
                ('authorised_person_contactno', models.CharField(blank=True, max_length=500, null=True)),
                ('last_date_of_vist', models.CharField(blank=True, max_length=500, null=True)),
                ('inspection_remark', models.TextField(blank=True, null=True)),
                ('updatetime', models.CharField(blank=True, max_length=500, null=True)),
                ('gdc_username', models.TextField(blank=True, null=True)),
                ('pid', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('lastupdateby', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'benchmark_gcpdata_backup',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BenchmarkGtstation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('gtstation_name', models.CharField(blank=True, max_length=200, null=True)),
                ('pamphlet_no', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('district', models.CharField(blank=True, max_length=200, null=True)),
                ('tahsil', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.CharField(blank=True, max_length=200, null=True)),
                ('longitude', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.CharField(blank=True, max_length=200, null=True)),
                ('gt_station_inscription', models.CharField(blank=True, max_length=200, null=True)),
                ('ellipsoidheight', models.CharField(blank=True, max_length=200, null=True)),
                ('old_description', models.TextField(blank=True, null=True)),
                ('revised_description', models.TextField(blank=True, null=True)),
                ('conduction_of_gtstation', models.CharField(blank=True, max_length=500, null=True)),
                ('authorised_person_name_and_designation', models.CharField(blank=True, max_length=500, null=True)),
                ('authorised_person_contactno', models.CharField(blank=True, max_length=500, null=True)),
                ('last_date_of_vist', models.CharField(blank=True, max_length=500, null=True)),
                ('inspection_remark', models.TextField(blank=True, null=True)),
                ('gdc_username', models.TextField(blank=True, null=True)),
                ('image_east', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_west', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_north', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_south', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('closeup_image', models.FileField(blank=True, null=True, upload_to='image/')),
                ('keyid', models.CharField(blank=True, max_length=200, null=True)),
                ('updatetime', models.CharField(blank=True, max_length=500, null=True)),
                ('gravityvalue', models.CharField(blank=True, max_length=200, null=True)),
                ('orthometrichight', models.CharField(blank=True, max_length=200, null=True)),
                ('triangulatedheight', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(default='unverified', max_length=20)),
                ('lastupdateby', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'benchmark_gtstation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BenchmarkGtstationBackup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyid', models.CharField(blank=True, max_length=200, null=True)),
                ('gtstation_name', models.CharField(blank=True, max_length=200, null=True)),
                ('pamphlet_no', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('ellipsoidheight', models.CharField(blank=True, max_length=200, null=True)),
                ('triangulatedheight', models.CharField(blank=True, max_length=200, null=True)),
                ('orthometrichight', models.CharField(blank=True, max_length=200, null=True)),
                ('gravityvalue', models.CharField(blank=True, max_length=200, null=True)),
                ('district', models.CharField(blank=True, max_length=200, null=True)),
                ('tahsil', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.CharField(blank=True, max_length=200, null=True)),
                ('longitude', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.CharField(blank=True, max_length=200, null=True)),
                ('gt_station_inscription', models.CharField(blank=True, max_length=200, null=True)),
                ('old_description', models.TextField(blank=True, null=True)),
                ('revised_description', models.TextField(blank=True, null=True)),
                ('conduction_of_gtstation', models.CharField(blank=True, max_length=500, null=True)),
                ('image_east', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_west', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_north', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_south', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('closeup_image', models.FileField(blank=True, null=True, upload_to='image/')),
                ('authorised_person_name_and_designation', models.CharField(blank=True, max_length=500, null=True)),
                ('authorised_person_contactno', models.CharField(blank=True, max_length=500, null=True)),
                ('last_date_of_vist', models.CharField(blank=True, max_length=500, null=True)),
                ('inspection_remark', models.TextField(blank=True, null=True)),
                ('updatetime', models.CharField(blank=True, max_length=500, null=True)),
                ('gdc_username', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('lastupdateby', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'benchmark_gtstation_backup',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BenchmarkSbmdata',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sbm_type', models.CharField(blank=True, max_length=200, null=True)),
                ('pamphlet_no', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('district', models.CharField(blank=True, max_length=200, null=True)),
                ('tahsil', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.CharField(blank=True, max_length=200, null=True)),
                ('longitude', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.CharField(blank=True, max_length=200, null=True)),
                ('sbm_inscription', models.TextField(blank=True, null=True)),
                ('old_description', models.TextField(blank=True, null=True)),
                ('revised_description', models.TextField(blank=True, null=True)),
                ('conduction_of_sbm', models.CharField(blank=True, max_length=500, null=True)),
                ('conduction_of_reference_pillar', models.CharField(blank=True, max_length=500, null=True)),
                ('authorised_person_name_and_designation', models.CharField(blank=True, max_length=500, null=True)),
                ('authorised_person_contactno', models.CharField(blank=True, max_length=500, null=True)),
                ('last_date_of_vist', models.CharField(blank=True, max_length=500, null=True)),
                ('inspection_remark', models.TextField(blank=True, null=True)),
                ('gdc_username', models.TextField(blank=True, null=True)),
                ('gravityvalue', models.CharField(blank=True, max_length=200, null=True)),
                ('image_east', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_west', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_north', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_south', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('closeup_image', models.FileField(blank=True, null=True, upload_to='image/')),
                ('keyid', models.CharField(blank=True, max_length=200, null=True)),
                ('updatetime', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(default='unverified', max_length=20)),
                ('lastupdateby', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'benchmark_sbmdata',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BenchmarkSbmdataBackup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyid', models.CharField(blank=True, max_length=200, null=True)),
                ('sbm_type', models.CharField(blank=True, max_length=200, null=True)),
                ('pamphlet_no', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('district', models.CharField(blank=True, max_length=200, null=True)),
                ('tahsil', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.CharField(blank=True, max_length=200, null=True)),
                ('longitude', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.CharField(blank=True, max_length=200, null=True)),
                ('sbm_inscription', models.TextField(blank=True, null=True)),
                ('old_description', models.TextField(blank=True, null=True)),
                ('revised_description', models.TextField(blank=True, null=True)),
                ('conduction_of_sbm', models.CharField(blank=True, max_length=500, null=True)),
                ('conduction_of_reference_pillar', models.CharField(blank=True, max_length=500, null=True)),
                ('image_east', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_west', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_north', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_south', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('closeup_image', models.FileField(blank=True, null=True, upload_to='image/')),
                ('authorised_person_name_and_designation', models.CharField(blank=True, max_length=500, null=True)),
                ('authorised_person_contactno', models.CharField(blank=True, max_length=500, null=True)),
                ('last_date_of_vist', models.CharField(blank=True, max_length=500, null=True)),
                ('inspection_remark', models.TextField(blank=True, null=True)),
                ('updatetime', models.CharField(blank=True, max_length=500, null=True)),
                ('gravityvalue', models.CharField(blank=True, max_length=200, null=True)),
                ('gdc_username', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('lastupdateby', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'benchmark_sbmdata_backup',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='cors_inventory_for_other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentname', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.CharField(blank=True, max_length=200, null=True)),
                ('longitude', models.CharField(blank=True, max_length=200, null=True)),
                ('premise_address', models.CharField(blank=True, max_length=250, null=True)),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('district', models.CharField(blank=True, max_length=250, null=True)),
                ('state', models.CharField(blank=True, max_length=250, null=True)),
                ('monument_type', models.CharField(blank=True, max_length=250, null=True)),
                ('monument_stability', models.CharField(blank=True, max_length=250, null=True)),
                ('gnss_receiver_make_and_model', models.CharField(blank=True, max_length=250, null=True)),
                ('gnss_antenna_make_and_model', models.CharField(blank=True, max_length=250, null=True)),
                ('obstructions_to_antenna', models.TextField(blank=True, null=True)),
                ('image_east', models.FileField(blank=True, null=True, upload_to='otherimg/')),
                ('image_west', models.FileField(blank=True, null=True, upload_to='otherimg/')),
                ('image_north', models.FileField(blank=True, null=True, upload_to='otherimg/')),
                ('image_south', models.FileField(blank=True, null=True, upload_to='otherimg/')),
                ('pdf_form', models.FileField(blank=True, null=True, upload_to='otherimg/')),
                ('persion_contact_no', models.CharField(blank=True, max_length=250, null=True)),
                ('persion_name', models.CharField(blank=True, max_length=250, null=True)),
                ('power', models.CharField(blank=True, max_length=250, null=True)),
                ('probable_multipath_and_electro_megnetic_interference', models.CharField(blank=True, max_length=250, null=True)),
                ('probablemultipath', models.CharField(blank=True, max_length=250, null=True)),
                ('data_transmission', models.CharField(blank=True, max_length=250, null=True)),
                ('online_transmission', models.CharField(blank=True, max_length=250, null=True)),
                ('availability_of_gsm_4g_connection', models.CharField(blank=True, max_length=250, null=True)),
                ('availability_of_broadband_connection', models.CharField(blank=True, max_length=250, null=True)),
                ('availability_of_electric_surge_or_lightening_conductors', models.CharField(blank=True, max_length=250, null=True)),
                ('access_control', models.CharField(blank=True, max_length=250, null=True)),
                ('operation_and_maintenance', models.CharField(blank=True, max_length=250, null=True)),
                ('gdc_username', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
