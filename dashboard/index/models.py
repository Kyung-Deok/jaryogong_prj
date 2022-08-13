from django.db import models

# 연간이용량

# 시간당 이용량
class RentalRecordPerHour(models.Model):
    rental_record_per_hour_id = models.AutoField(primary_key=True)
    ref_date = models.DateField(blank=True, null=True)
    ref_time = models.TimeField(blank=True, null=True)
    voucher = models.CharField(max_length=20, blank=True, null=True)
    age_distribution = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RENTAL_RECORD_PER_HOUR'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AvgQuantityAge(models.Model):
    avg_age_id = models.AutoField(primary_key=True)
    day_of_week = models.CharField(max_length=10, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    age_category = models.CharField(max_length=100, blank=True, null=True)
    avg_age_quantity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avg_quantity_age'


class AvgQuantityVoucher(models.Model):
    avg_voucher_id = models.AutoField(primary_key=True)
    day_of_week = models.CharField(max_length=10, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    voucher = models.CharField(max_length=50, blank=True, null=True)
    avg_voucher_quantity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avg_quantity_voucher'


class BikeStopInfo(models.Model):
    bike_stop_id = models.IntegerField(primary_key=True)
    bike_stop_code = models.CharField(unique=True, max_length=20, blank=True, null=True)
    bike_stop_lat = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    bike_stop_lot = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bike_stop_info'


class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    building_category = models.CharField(max_length=200, blank=True, null=True)
    building_detail = models.CharField(max_length=200, blank=True, null=True)
    gugun = models.CharField(max_length=200, blank=True, null=True)
    hangjungdong = models.CharField(max_length=200, blank=True, null=True)
    building_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'building'


class BusStop(models.Model):
    bus_stop_id = models.IntegerField(primary_key=True)
    bus_stop_name = models.CharField(unique=True, max_length=200, blank=True, null=True)
    bus_stop_lat = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    bus_stop_lot = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_stop'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200, blank=True, null=True)
    event_category = models.CharField(max_length=200, blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    event_addr = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'


class Hangjungdong(models.Model):
    hangjungdong_id = models.IntegerField(primary_key=True)
    gugun = models.CharField(max_length=50, blank=True, null=True)
    hangjungdong = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hangjungdong'


class JaryogongDjangoTesthostpitallocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    public_or_privates = models.CharField(max_length=20)
    categories = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    latitude = models.DecimalField(max_digits=15, decimal_places=6)
    longitude = models.DecimalField(max_digits=15, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'jaryogong_django_testhostpitallocation'


class MetroStation(models.Model):
    metro_station_id = models.IntegerField(primary_key=True)
    metro_station_name = models.CharField(max_length=200, blank=True, null=True)
    metro_station_category = models.CharField(max_length=200, blank=True, null=True)
    metro_station_lat = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    metro_station_lot = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metro_station'


class OntimeRentalInfo(models.Model):
    ontime_rental_info_id = models.AutoField(primary_key=True)
    bike_stop_code = models.CharField(max_length=20, blank=True, null=True)
    ontime_timestamp = models.DateTimeField()
    holder_amount = models.IntegerField(blank=True, null=True)
    parking_rate = models.IntegerField(blank=True, null=True)
    parking_amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ontime_rental_info'


class Population(models.Model):
    population_id = models.AutoField(primary_key=True)
    day_of_week = models.CharField(max_length=10, blank=True, null=True)
    ref_time = models.CharField(max_length=5, blank=True, null=True)
    hangjungdong_id = models.IntegerField(blank=True, null=True)
    number_0_9 = models.IntegerField(db_column='0_9', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_10_19 = models.IntegerField(db_column='10_19', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_20_29 = models.IntegerField(db_column='20_29', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_30_39 = models.IntegerField(db_column='30_39', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_40_49 = models.IntegerField(db_column='40_49', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_50_59 = models.IntegerField(db_column='50_59', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_60_69 = models.IntegerField(db_column='60_69', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_70_field = models.IntegerField(db_column='70_', blank=True, null=True)  # Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'population'


class RentalPerYear(models.Model):
    rental_per_year_id = models.AutoField(primary_key=True)
    bike_stop_id = models.IntegerField()
    rental_amount_year = models.IntegerField(blank=True, null=True)
    ref_year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rental_per_year'

# 팩트테이블
class SumQuantityPerHourStop(models.Model):
    sum_quantity_hour_id = models.AutoField(primary_key=True)
    bike_stop_id = models.IntegerField()
    day_of_week = models.CharField(max_length=10, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    sum_quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sum_quantity_per_hour_stop'


class TransportationBus(models.Model):
    transportation_bus_id = models.AutoField(primary_key=True)
    day_of_week = models.CharField(max_length=10, blank=True, null=True)
    depart_bus_stop_id = models.IntegerField(blank=True, null=True)
    arrival_bus_stop_id = models.IntegerField(blank=True, null=True)
    bus_00_01 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_01_02 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_02_03 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_03_04 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_04_05 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_05_06 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_06_07 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_07_08 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_08_09 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_09_10 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_10_11 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_11_12 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_12_13 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_13_14 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_14_15 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_15_16 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_16_17 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_17_18 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_18_19 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_19_20 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_20_21 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_21_22 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_22_23 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bus_23_24 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transportation_bus'


class TransportationMetro(models.Model):
    transportation_metro_id = models.AutoField(primary_key=True)
    day_of_week = models.CharField(max_length=10, blank=True, null=True)
    depart_metro_station_id = models.IntegerField(blank=True, null=True)
    arrival_metro_station_id = models.IntegerField(blank=True, null=True)
    metro_00_01 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_01_02 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_02_03 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_03_04 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_04_05 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_05_06 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_06_07 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_07_08 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_08_09 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_09_10 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_10_11 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_11_12 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_12_13 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_13_14 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_14_15 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_15_16 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_16_17 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_17_18 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_18_19 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_19_20 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_20_21 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_21_22 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_22_23 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    metro_23_24 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transportation_metro'