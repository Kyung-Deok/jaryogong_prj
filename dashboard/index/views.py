from datetime import date
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, Avg
from .models import OntimeRentalInfo, RentalPerYear, SumQuantityPerHourStop
import datetime
# Create your views here.

# rental_per_year : 연도별 대여량
# 기준 년도(ref_year_date) 맞춰서 연도 별 대여량(rental_amount_year) 합계
# 정거장 별 기준은 상관이 없다. station id 구분 없이 끌고 오자

def home(request) :    
    return JsonResponse({"h" : "hello world"})


def stream_keyword(request) :
    # 오늘의 따릉이 대여건수, 가장 많이 빌려진 대여소, 자전거 거치율100% 이상 대여소 주소, 자전거 거치율 50% 미만 대여소 주소
    rent_total = OntimeRentalInfo.objects.aggregate(rent_total=Sum('parking_amount')-Sum('holder_amount'))
    rent_top5 = OntimeRentalInfo.objects.all().order_by('-parking_amount')[0:5]
    parking_higher = OntimeRentalInfo.objects.filter(parking_rate__gt=100)
    parking_lower= OntimeRentalInfo.objects.filter(parking_rate__lt=50)
    
    
# 기준년도에 맞춰서 연도 별 대여량 합계
def change_user(request):
    try :
        data = {
        'total_2018' : RentalPerYear.objects.filter(ref_year='2018').aggregate(Sum('rental_amount_year')),
        'total_2019' : RentalPerYear.objects.filter(ref_year='2019').aggregate(Sum('rental_amount_year')),
        'total_2020' : RentalPerYear.objects.filter(ref_year='2020').aggregate(Sum('rental_amount_year')),
        'total_2021' : RentalPerYear.objects.filter(ref_year='2021').aggregate(Sum('rental_amount_year')),
        }
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, status=200)
    except ValueError :
        return JsonResponse({'err':"err"}, status=400)
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
            morning = RentalPerYear.objects\
                .filter(ref_date=choice_date)\
                .annotate(morn = Sum('17')+Sum('18')+Sum('19')+Sum('20')) # 00-24까지 컬럼이 존재
            evenning = RentalPerYear.objects\
                .filter(ref_date=choice_date)\
                .annotate(even = Sum('17')+Sum('18')+Sum('19')+Sum('20'))
        
            data['morning'] = morning
            data['evenning'] = evenning
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, status=200) 
        else : 
            return JsonResponse(data, status=200)
    except ValueError:
        return JsonResponse({'err':'value error'},status=400)   


# 시간대 별 대여소 별 대여량
# 날짜 필터 걸고, 요일 별 필터
# 요일별 시간대로 쪼개진 사용량 : 대여량 top5 => 손대면 표시 
def rent_tops(request):
    try:
        if request.method == "POST":
            #요일별 
            choice_days = json.load(request.body)
            if choice_days is None :
                days_of_weeks= ['월','화', '수', '목','금','토','일']
                choice_today = datetime.datetime.today().weekday()
                choice_days = days_of_weeks[choice_today]
            # 대여소id, 기준요일을 가져온다, 해당요일에 해당하는, 옆에 Sum
            datas_of_days = SumQuantityPerHourStop.objects.get("bike_stop_id", "ref_time").filter(ref_time=choice_days)\
                .annotate(Sum("0"),Sum("1"),Sum("2"),Sum("3"),Sum("4"),Sum("5"),Sum("6"),Sum("7"),Sum("8"),Sum("9"),Sum("10"),Sum("11"),Sum("12"),Sum("13"),Sum("14"),Sum("15"),Sum("16"),Sum("17"),Sum("18"),Sum("19"),Sum("20"),Sum("21"),Sum("22"),Sum("23"),Sum("24"))
            
            # bike_stop = datas_of_days.bike_stop_name
            data = {"datas_of_days":datas_of_days, "bike_stop_name" : "bike_stop"}
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, status=200) 
    except :
        return JsonResponse({"err" :"err"},status=400)
def events(request):
    pass
