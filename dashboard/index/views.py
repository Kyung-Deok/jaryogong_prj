import json
import django
from time import time
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, Avg,Q
from .models import AvgQuantityVoucher, BikeStopInformation, Event, OntimeRentalInfo, RentalPerYear, RentalRecordPerHour, SumQuantityPerHourStop
import datetime
# Create your views here.

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
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, status=200)
    except django.db.utils.OperationalError:
        return JsonResponse({'err':"테이블 없음"}, status=400)
    except Exception as err:
        return JsonResponse({"err": err})

# 연도별 사용량
def years_of_user(request):
    # 기준년도에 맞춰서 연도 별 대여량 합계 표시 for문으로할수 없나?
    try :
        data = {
        "total_2019" : RentalPerYear.objects.filter(year='2019').aggregate(sum_years=Sum('use_count')),
        "total_2020" : RentalPerYear.objects.filter(year='2020').aggregate(sum_years=Sum('use_count')),
        "total_2021" : RentalPerYear.objects.filter(year='2021').aggregate(sum_years=Sum('use_count')),
        }
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, status=200)
    except django.db.utils.OperationalError:
        return JsonResponse({'err':"테이블 없음"}, status=400)
    except Exception as err :
        return JsonResponse({'err': str(err) },json_dumps_params={'ensure_ascii': False}, status=400)
    
def vouchers(request):
    try:
        if request.method=="POST" :
            days_of_weeks= ['Mon','Tue', 'Wen', 'Thu','Fri','Sat','Sun']
            choice_days = request.POST.get('choicedays',None)
            # print(choice_days)
            if choice_days is None :
                choice_days_t = datetime.datetime.today().weekday()
                choice_day_week = days_of_weeks[choice_days_t]
            choice_daysf = datetime.datetime.strptime(choice_days,'%Y-%m-%d').weekday()
            choice_day_week = days_of_weeks[choice_daysf]

            print(choice_days, choice_day_week)
            # 오전 시간대 (:11) 대여소 총 집계한 일일권 사용자
            # 오전 구분(원하는 날짜만, 그중 기준시간 데이터만,오전시간만 집계)``
            

            # 일일권/정기권/비회원 여부
            days_tickets = AvgQuantityVoucher.objects.filter(Q(voucher='일일권') & Q(day_of_week=choice_day_week)).values()
            regular_tickets = AvgQuantityVoucher.objects.filter(Q(voucher='정기권') & Q(day_of_week=choice_day_week)).values()
            noauth_tickets =  AvgQuantityVoucher.objects.filter(Q(voucher='일일권(비회원)') & Q(day_of_week=choice_day_week)).values()
            # 출퇴근시간 구분
            d_morning_vouchers = days_tickets.filter(Q(time='7') | Q(time='8') | Q(time='9')).values()
            d_evenning_vouchers = days_tickets.filter(Q(time='18') | Q(time='19') | Q(time='20')).values()
            r_morning_vouchers = regular_tickets.filter(Q(time='7') | Q(time='8') | Q(time='9')).values()
            r_evenning_vouchers = regular_tickets.filter(Q(time='18') | Q(time='19') | Q(time='20')).values()
            n_morning_vouchers = noauth_tickets.filter(Q(time='7') | Q(time='8') | Q(time='9')).values()
            n_evenning_vouchers = noauth_tickets.filter(Q(time='18') | Q(time='19') | Q(time='20')).values()
            
            # print(days_tickets)

            # 출근집계, 퇴근집계
            d_avg_morning = d_morning_vouchers.aggregate(Sum('avg_voucher_quantity'))
            d_avg_evenning = d_evenning_vouchers.aggregate(Sum('avg_voucher_quantity'))
            r_avg_morning = r_morning_vouchers.aggregate(Sum('avg_voucher_quantity'))
            r_avg_evenning = r_evenning_vouchers.aggregate(Sum('avg_voucher_quantity'))
            n_avg_morning = n_morning_vouchers.aggregate(Sum('avg_voucher_quantity'))
            n_avg_evenning = n_evenning_vouchers.aggregate(Sum('avg_voucher_quantity'))
            
            res_data = {
            'd_avg_morning' : d_avg_morning,
            'd_avg_evenning' : d_avg_evenning,
            'r_avg_morning' : r_avg_morning,
            'r_avg_evenning' : r_avg_evenning,
            'n_avg_morning' : n_avg_morning,
            'n_avg_evenning' : n_avg_evenning,
            # 'days_' : list(days_tickets),
            }
            return JsonResponse(res_data, safe=False, json_dumps_params={'ensure_ascii': False}, status=200) 
        else :  
            return JsonResponse({'data' : 'test'}, status=200)
    except django.db.utils.OperationalError:
        return JsonResponse({'err':"테이블 없음"}, status=400)
    except Exception as err:
        return JsonResponse({ 'err' : str(err) }, status=400)   


# 시간대 별 대여소 별 대여량, 날짜 필터 걸고, 요일 별 필터
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
            select_of_days = SumQuantityPerHourStop.objects.get("sum_quantity").filter(day_of_week=choice_day)
            
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
    except Exception as err :
        return JsonResponse({ "err" : err },status=400)


def events(request):
    try:
        if request.method == 'GET':
            # 이벤트 정보 불러오기 : 2020 -2022년도 까지
            date_event_datas = Event.objects.filter(year__in=['2020','2021','2022']).values('year','month','date')
            cate_event_datas = Event.objects.filter(year__in=['2020','2021','2022']).values('event_category')
            name_event_datas = Event.objects.filter(year__in=['2020','2021','2022']).values('event_name')
            addr_event_datas = Event.objects.filter(year__in=['2020','2021','2022']).values('event_addr')
            res_data = {
                'date_event_datas' : date_event_datas,
                'cate_event_datas' : cate_event_datas,
                'name_event_datas' : name_event_datas,
                'addr_event_datas' : addr_event_datas,
            }
            return JsonResponse(res_data, json_dumps_params={'ensure_ascii': False},status=200)

        else :
            days_of_weeks= ['월','화', '수', '목','금','토','일']
            # seoul_gu = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', 
            #     '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', 
            #     '용산구', '은평구', '종로구', '중구', '중랑구']
            data={}
            
            # req.body 불러오기 : 날짜, 카테고리, 이름, 주소
            choice_date = request.POST.get('date_event_datas', None)
            choice_cate = request.POST.get('cate_event_datas', None)
            choice_name = request.POST.get('name_event_datas', None)
            choice_addr = request.POST.get('addr_event_datas', None)
            
            # 값 없다면 일단 에러로 표시
            if choice_date | choice_cate | choice_name | choice_addr is None :
                return JsonResponse({"err": "선택 필수"}, status=400)
            # 날짜 가지고 요일 뽑아내기
            event_date = datetime.datetime.date(choice_date).weekday()
            event_day_of_week = days_of_weeks[event_date] # 이벤트가 있었던 날의 요일

            # 이벤트가 있었던 일자에 평소 사용량
            sum_usual_dates = SumQuantityPerHourStop.objects.filter(days_of_weeks=event_day_of_week).values("sum_quantity")
            # 이벤트가 있었던 일자에 시간대 별 사용량
            sum_event_dates = "대여소/일자별/시간대".objects.filter(days_of_weeks=event_day_of_week).aggregate(sum_events=Sum("sum_quantity"))

            res_data ={
                'sum_usual_datas' : sum_usual_dates,
                'sum_event_datas' : sum_event_dates,
            }

            return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, status=200) 
    except django.db.utils.OperationalError:
        return JsonResponse({'err':"테이블 없음"}, status=400)
    except Exception as err:
        return JsonResponse({'err': err},status=400)
    
def trans_traffic(request):
    pass
