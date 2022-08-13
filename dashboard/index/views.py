from datetime import date
from functools import total_ordering
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
from models import *
# Create your views here.

# rental_per_year : 연도별 대여량
# 기준 년도(ref_year_date) 맞춰서 연도 별 대여량(rental_amount_year) 합계
# 정거장 별 기준은 상관이 없다. station id 구분 없이 끌고 오자

def home(request) :    
    return JsonResponse({"h" : "hello world"})

# 기준년도에 맞춰서 연도 별 대여량 합계
def change_user(request):
    data = {}
    try :
        data['total_2018'] = Rental_per_year.objects.filter(ref_year='2018').aggregate(Sum('rent_amount_year'))
        data['total_2019'] = Rental_per_year.objects.filter(ref_year='2019').aggregate(Sum('rent_amount_year'))
        data['total_2020'] = Rental_per_year.objects.filter(ref_year='2020').aggregate(Sum('rent_amount_year'))
        data['total_2021'] = Rental_per_year.objects.filter(ref_year='2021').aggregate(Sum('rent_amount_year'))
    
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, status=200)
    except ValueError :
        return JsonResponse({'err':"err"}, status=400)
# rental_record_per_hour : 시간대 별 대여량 as rrph
# bike_rental : 대여 정보(시간대 별 대여소 별 이용량) as br

# 기준 시간(ref_time_date)의 
# :11(오전), 12:(오후)

#오전 시간대 오후 시간대의 이용권 형태를 원 그래프로 표현 가능 
# ⇒ 오전, 오후 그래프 하나 씩, 대여소 총 집계한 데이터로, 
# 날짜 필터?
def vouchers(request):
    try:
        if request.method=="POST" : 
            data={}
            choice_date = json.load(request.body)
            if choice_date is None:
                choice_date = date.now()
            # 오전 시간대 (:11) 대여소 총 집계한 일일권 사용자
            #오전 구분(원하는 날짜만, 그중 기준시간 데이터만,오전시간만 집계)``
            morning = Rental_record_per_hour.objects\
                .filter(ref_date=choice_date)\
                .annotate(Sum('17'),Sum('18'),Sum('19'),Sum('20')) # 00-24까지 컬럼이 존재
            evenning = Rental_record_per_hour.objects\
                .filter(ref_date=choice_date)\
                .annotate(Sum('17'),Sum('18'),Sum('19'),Sum('20'))
        
            data['morning'] = morning
            data['evenning'] = evenning
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, status=200) 
        else : 
            return JsonResponse(data, status=200)
    except ValueError:
        return JsonResponse({'err':'value error'},status=400)   
    
def rent_tops(request):
    pass

def events(request):
    pass
