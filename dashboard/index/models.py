from django.db import models

from .views import vouchers

# Create your models here.

# DB 자동 연동
# python manage.py inspectdb > index/models.py
# 이후 makemigration 수행 ->migrate 실행 


# rental_per_year : 연도별 대여량
class Rental_per_year(models.Model):
    rental_per_year_id = models.AutoField(primary_key=True)
    bike_stop_id = models.IntegerField(max_length=50, null=False)
    ref_year = models.DateField()
    
# rental_record_per_hour : 시간대 별 대여량 as rrph
class Rental_record_per_hour(models.Model):
    rental_per_hour_id = models.AutoField(primary_key=True)
    bike_stop_id = models.IntegerField(max_length=50, null=False)
    ref_date = models.DateField()
    ref_time = models.TimeField()
    voucher = models.CharField(max_length=20)
    age_distribution = models.CharField(max_length=100)
    
    
# bike_rental : 대여 정보(시간대 별 대여소 별 이용량) as br



# bike_rental : 대여 정보(팩트 테이블)

