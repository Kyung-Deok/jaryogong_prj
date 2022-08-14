import django
from sqlite3 import OperationalError
from time import time
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, Avg,Q
from .models import AvgQuantityVoucher, OntimeRentalInfo, RentalPerYear, RentalRecordPerHour, SumQuantityPerHourStop
import datetime
# Create your views here.

# rental_per_year : 연도별 대여량
# 기준 년도(ref_year_date) 맞춰서 연도 별 대여량(rental_amount_year) 합계
# 정거장 별 기준은 상관이 없다. station id 구분 없이 끌고 오자

def home(request) :
    return JsonResponse({"h" : "hello world"})


def stream_keyword(request) :
    try : 
        # 오늘의 따릉이 대여건수, 가장 많이 빌려진 대여소, 자전거 거치율100% 이상 대여소 주소, 자전거 거치율 50% 미만 대여소 주소
        rent_total = OntimeRentalInfo.objects.aggregate(rent_total=Sum('parking_amount')-Sum('holder_amount'))
        rent_top5 = OntimeRentalInfo.objects.all().order_by('-parking_amount')[0:5]
        parking_higher = OntimeRentalInfo.objects.filter(parking_rate__gt=100)
        parking_lower= OntimeRentalInfo.objects.filter(parking_rate__lt=50)
        
        data = {'rent_total' : rent_total,
                'rent_top5': rent_top5,
                'parking_higher' : parking_higher,
                'parking_lower' : parking_lower
                }
    except django.db.utils.OperationalError:
        return JsonResponse({'err':"테이블 없음"}, status=400)
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, status=200)


def change_user(request):
    # 기준년도에 맞춰서 연도 별 대여량 합계 표시 for문으로할수 없나?
    try :
        data = {
        'total_2018' : RentalPerYear.objects.filter(ref_year='2018').aggregate(Sum('rental_amount_year')),
        'total_2019' : RentalPerYear.objects.filter(ref_year='2019').aggregate(Sum('rental_amount_year')),
        'total_2020' : RentalPerYear.objects.filter(ref_year='2020').aggregate(Sum('rental_amount_year')),
        'total_2021' : RentalPerYear.objects.filter(ref_year='2021').aggregate(Sum('rental_amount_year')),
        }
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, status=200)
    except django.db.utils.OperationalError:
        return JsonResponse({'err':"테이블 없음"}, status=400)
    # except :
    #     return JsonResponse({'err':"err"}, status=400)
    
    
    
# 오전 시간대 오후 시간대의 이용권 형태를 원 그래프로 표현 가능 
# ⇒ 출근, 퇴근 그래프 하나 씩, 대여소 총 집계한 데이터로, 
# 날짜 필터?
def vouchers(request):
    try:
        if request.method=="POST" :
            choice_date = request.POST.get('choice_data',None)
            if choice_date is None:
                choice_date = datetime.datetime.now()
            # 오전 시간대 (:11) 대여소 총 집계한 일일권 사용자
            # 오전 구분(원하는 날짜만, 그중 기준시간 데이터만,오전시간만 집계)``
            
            # 일일권/정기권 여부
            days_tickets =AvgQuantityVoucher.objects.filter(day_of_week='일일권')
            regular_tickets = AvgQuantityVoucher.objects.filter(day_of_week='정기권')
            noauth_tickets =  AvgQuantityVoucher.objects.filter(day_of_week='일일권(비회원)')
            
            # 출퇴근시간 구분
            d_morning_vouchers = days_tickets.filter(Q(time='7') | Q(time='8') | Q(time='9'))
            d_evenning_vouchers = days_tickets.filter(Q(time='18') | Q(time='19') | Q(time='20'))
            r_morning_vouchers = regular_tickets.filter(Q(time='7') | Q(time='8') | Q(time='9'))
            r_evenning_vouchers = regular_tickets.filter(Q(time='18') | Q(time='19') | Q(time='20'))
            n_morning_vouchers = noauth_tickets.filter(Q(time='7') | Q(time='8') | Q(time='9'))
            n_evenning_vouchers = noauth_tickets.filter(Q(time='18') | Q(time='19') | Q(time='20'))
            
            # 출근집계, 퇴근집계
            d_avg_morning = d_morning_vouchers.aggregate(Sum('avg_voucher_quantity'))
            d_avg_evenning = d_evenning_vouchers.aggregate(Sum('avg_voucher_quantity'))
            r_avg_morning = r_morning_vouchers.aggregate(Sum('avg_voucher_quantity'))
            r_avg_evenning = r_evenning_vouchers.aggregate(Sum('avg_voucher_quantity'))
            n_avg_morning = n_morning_vouchers.aggregate(Sum('avg_voucher_quantity'))
            n_avg_evenning = n_evenning_vouchers.aggregate(Sum('avg_voucher_quantity'))
            
            data = {
                'd_avg_morning' : d_avg_morning,
                'd_avg_evenning' : d_avg_evenning,
                'r_avg_morning' : r_avg_morning,
                'r_avg_evenning' : r_avg_evenning,
                'n_avg_morning' : n_avg_morning,
                'n_avg_evenning' : n_avg_evenning,
            }
        
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, status=200) 
        else : 
            return JsonResponse({'data' : 'test'}, status=200)
    except django.db.utils.OperationalError:
        return JsonResponse({'err':"테이블 없음"}, status=400)
    except :
        return JsonResponse({'err':'err'},status=400)   


# 시간대 별 대여소 별 대여량
# 날짜 필터 걸고, 요일 별 필터
# 요일별 시간대로 쪼개진 사용량 : 대여량 top5 => 손대면 표시 
def rent_tops(request):
    try:
        if request.method == "POST":
            #요일별 
            choice_days = request.POST.get('choice_days', None) # YYYY MM DD 이런 형식으로!
            days_of_weeks= ['월','화', '수', '목','금','토','일']
            if choice_days is None :
                choice_day = datetime.datetime.today().weekday()
                choice_day_week = days_of_weeks[choice_day]
            else :
                choice_day = datetime.datetime.date(choice_days)
                choice_day_week = days_of_weeks[choice_day]
            
            # 대여소id, 기준요일을 가져온다, 해당요일에 해당하는, 옆에 Sum
            data={}
            # 기준일에 대한 요일에 따른 데이터를 집어온다.
            select_of_days = SumQuantityPerHourStop.objects.filter(day_of_week=choice_day_week)
            
            # 집계한다. 시간대별 총 데이터
            for i in range(0,25):
                # 요일마다 시간별.
                select_times = select_of_days.filter(time=i)
                data[f'select_{i}_times'] = select_times
                # 정해진 시간 별로 합계
                sum_times = select_times.aggregate(sums=Sum(i))
                data[f'sum_{i}_times'] = sum_times
            data['rent_top5'] = select_times.order_by('sum_quantity')[0:5]
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, status=200) 
        else :
            return JsonResponse({"data":"test"}, status = 200)
            
            # bike_stop = datas_of_days.bike_stop_name
    except django.db.utils.OperationalError:
        return JsonResponse({'err':"테이블 없음"}, status=400)
    except :
        return JsonResponse({"err" :"err"},status=400)



# event TABLE에는 day_of_week column 없음, 요일데이터 X
# 근처장소 날짜 시간, 월~일 요일별 데이터
# 요일필터안 시간대 데이터
def events(request):
    try:
        if request.method == 'POST':
            days_of_weeks= ['월','화', '수', '목','금','토','일']
            seoul_gu = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', 
                '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', 
                '용산구', '은평구', '종로구', '중구', '중랑구']
            
            # 이벤트 날짜 선택
            choice_day = request.POST.get('event_ref_date', None)
            # 만약 없으면 오늘 날짜로 찾아준다.
            if choice_day is None :
                choice_day = datetime.datetime.today() 
                event_date = choice_day.weekday()
                event_day_of_week = days_of_weeks[event_date] # 이벤트 있었던 날의 요일을 오늘 요일로 대체
            else :
                event_date = datetime.datetime.date(choice_day).weekday()
                event_day_of_week = days_of_weeks[event_date] # 이벤트가 있었던 날의 요일

            # 이벤트가 있었던 일자 선택 
            event_dates = RentalRecordPerHour.objects.filter(ref_date=choice_day)
            # 이벤트가 있었던 시간대 이용량 집계
            event_times = event_dates.filter(Q(ref_time='22') | Q(ref_time='23'))
            # 이벤트가 있었던 장소
            event_loc = event_times.filter(event_addr__in=seoul_gu)
            # 이벤트를 갯수
            event_counts = event_loc.aggregate(event_counts=('rental_record_per_hour_id').count())

            data = {
                'event_dates': event_dates, # 이벤트 날짜
                'event_times': event_times, # 이벤트 시간
                'event_loc': event_loc, # 이벤트 장소
                'event_counts': event_counts # 이벤트 숫자
            }
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, status=200) 
        else:
            return JsonResponse({"data":"test"}, json_dumps_params={'ensure_ascii': False}, status=200) 
    except ValueError:
        return JsonResponse({'err':'value error'},status=400)   