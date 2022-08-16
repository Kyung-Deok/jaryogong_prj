from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import django
from time import time
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, Avg,Q
from .models import AvgQuantityVoucher, BikeStopInformation, Event, OntimeRentalInfo, RentalPerYear, RentalRecordPerHour, SumQuantityPerHourStop, TransportationBus, Population, Building
import datetime
from secrets import choice
import json
import plotly.express as px
from plotly.offline import plot
from pprint import pprint
import pandas as pd
import plotly.graph_objects as go

def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

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


def years_of_user(request):
    # 기준년도에 맞춰서 연도 별 대여량 합계 표시 for문으 q로할수 없나?
    try :
        datas={}
        if request.method == "GET":
            datas["total_2019"] = RentalPerYear.objects.filter(year='2019').aggregate(sum_years=Sum('use_count'))
            datas["total_2020"] = RentalPerYear.objects.filter(year='2020').aggregate(sum_years=Sum('use_count'))
            datas["total_2021"] = RentalPerYear.objects.filter(year='2021').aggregate(sum_years=Sum('use_count'))
            print(datas)
            # return JsonResponse(datas, json_dumps_params={'ensure_ascii': False}, status=200)
            return render(request, 'home/index.html', datas)
            # html_template = loader.get_template('home/index.html')
            # return HttpResponse(html_template.render(datas, request))
    except django.db.utils.OperationalError:
        return JsonResponse({'err':"테이블 없음"}, status=400)
    except Exception as err :
        return JsonResponse({'err': str(err) },json_dumps_params={'ensure_ascii': False}, status=400)
    
def vouchers(request):
    try:
        days_of_weeks= ['Mon','Tue', 'Wen', 'Thu','Fri','Sat','Sun']
        if request.method=="POST" :
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
            context={}
            choice_days_t = datetime.datetime.today().weekday()
            choice_day_week = days_of_weeks[choice_days_t]
            context['choice_day_week'] = choice_day_week
            #  일일권/정기권/비회원 여부
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
            d_avg_morning = d_morning_vouchers.aggregate(sum_data=Sum('avg_voucher_quantity'))
            d_avg_evenning = d_evenning_vouchers.aggregate(sum_data=Sum('avg_voucher_quantity'))
            r_avg_morning = r_morning_vouchers.aggregate(sum_data=Sum('avg_voucher_quantity'))
            r_avg_evenning = r_evenning_vouchers.aggregate(sum_data=Sum('avg_voucher_quantity'))
            n_avg_morning = n_morning_vouchers.aggregate(sum_data=Sum('avg_voucher_quantity'))
            n_avg_evenning = n_evenning_vouchers.aggregate(sum_data=Sum('avg_voucher_quantity'))
            
            
            context['d_avg_morning'] = d_avg_morning
            context['d_avg_evenning'] = d_avg_evenning
            context['r_avg_morning'] = r_avg_morning
            context['r_avg_evenning'] = r_avg_evenning
            context['n_avg_morning'] = n_avg_morning
            context['n_avg_evenning'] = n_avg_evenning
            # 'days_' : list(days_tickets),
            
            return render(request,'home/index.html',context)
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
            days_of_weeks= ['Mon','Tue', 'Wed', 'Thu','Fri','Sat','Sun']
            choice_days = request.POST.get('choicedays',None)
            if choice_days is None :
                choice_days_t = datetime.datetime.today().weekday()
                choice_day_week = days_of_weeks[choice_days_t]
            choice_daysf = datetime.datetime.strptime(choice_days,'%Y-%m-%d').weekday()
            choice_day_week = days_of_weeks[choice_daysf]
            
            print(choice_day_week)
            # 대여소id, 기준요일을 가져온다, 해당요일에 해당하는, 옆에 Sum
            data={}
            # 기준일에 대한 요일에 따른 데이터를 집어온다 : x요일에 대여소 별로 시간 별로 찍힌것
            select_of_days = SumQuantityPerHourStop.objects.filter(day_of_week=choice_day_week).values('time','sum_quantity')
            print(len(list(select_of_days))) #65000여개
            # 집계한다. 시간대별 총 데이터
            select_times_list=[]
            for i in range(0,24):
                # 요일마다 시간별
                select_times = select_of_days.filter(time=i).aggregate(sum_data=Sum('sum_quantity'))
                select_times_list.append(select_times)
                # top 5
                top_bike_stops=select_of_days.filter(time=i).order_by('-sum_quantity').values('bike_stop_id')[0:5]
            data['select_times_list']=list(select_times_list)
            data['top_bike_stops']=list(top_bike_stops)
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, status=200) 
        else :
            return JsonResponse({"data":"test"}, status = 200)
            
    except django.db.utils.OperationalError:
        return JsonResponse({'err':"테이블 없음"}, status=400)
    except Exception as err :
        return JsonResponse({ "err" : str(err) },status=400)

def events(request):
    try:
        if request.method == 'GET':
            # 이벤트 정보 불러오기 : 2020 -2022년도 까지
            date_event_datas = Event.objects.filter(year__in=['2020','2021','2022']).values('year','month','date')
            cate_event_datas = Event.objects.filter(year__in=['2020','2021','2022']).values('event_category')
            name_event_datas = Event.objects.filter(year__in=['2020','2021','2022']).values('event_name')
            addr_event_datas = Event.objects.filter(year__in=['2020','2021','2022']).values('event_addr')
            res_data = {
                'date_event_datas' : list(date_event_datas),
                'cate_event_datas' : list(cate_event_datas),
                'name_event_datas' : list(name_event_datas),
                'addr_event_datas' : list(addr_event_datas),
            }
            print(len(date_event_datas), len(cate_event_datas), len(name_event_datas), len(addr_event_datas))
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
            # if choice_date | choice_cate | choice_name | choice_addr is None :
            #     return JsonResponse({"err": "선택 필수"}, status=400)
            # 날짜 가지고 요일 뽑아내기
            event_date = datetime.datetime.strptime(choice_date,"%Y-%m-%d").weekday()
            event_day_of_week = days_of_weeks[event_date] # 이벤트가 있었던 날의 요일

            # 이벤트가 있었던 일자에 평소 사용량
            sum_usual_dates = SumQuantityPerHourStop.objects.filter(day_of_week=event_day_of_week).values("sum_quantity")
            # 이벤트가 있었던 일자에 시간대 별 사용량
            sum_event_dates = "대여소/일자별/시간대".objects.filter(days_of_week=event_day_of_week).aggregate(sum_events=Sum("sum_quantity"))

            res_data ={
                'sum_usual_datas' : sum_usual_dates,
                'sum_event_datas' : sum_event_dates,
            }

            return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, status=200) 
    except django.db.utils.OperationalError:
        return JsonResponse({'err':"테이블 없음"}, status=400)
    except Exception as err:
        return JsonResponse({'err': str(err)},status=400)
    
def trans_traffic(request):
    try:
        # 화면 먼저 렌더 해야 한다.
        if request.method == 'GET' :
            return JsonResponse({"data": "일단 render해야 함"}, status=200, json_dumps_params={'ensure_ascii': False})
        else :
            #요일별 
            days_of_weeks= ['Mon','Tue', 'Wen', 'Thu','Fri','Sat','Sun']
            choice_days = request.POST.get('choicedays',None)
            if choice_days is None :
                choice_days_t = datetime.datetime.today().weekday()
                choice_day_week = days_of_weeks[choice_days_t]
            choice_daysf = datetime.datetime.strptime(choice_days,'%Y-%m-%d').weekday()
            choice_day_week = days_of_weeks[choice_daysf]
            
            print(choice_day_week)
            # 대여소id, 기준요일을 가져온다, 해당요일에 해당하는, 옆에 Sum
            data={}
            # 기준일에 대한 요일에 따른 데이터를 집어온다 : x요일에 대여소 별로 시간 별로 찍힌것
            select_of_days = TransportationBus.objects.filter(day_of_week=choice_day_week).values('time','passenger')
            print(len(list(select_of_days))) #65000여개
            # 집계한다. 시간대별 총 데이터
            select_times_list=[]
            for i in range(0,24):
                # 요일마다 시간별
                select_times = select_of_days.filter(time=i).aggregate(sum_data=Sum('passenger'))
                select_times_list.append(select_times)
                # top 5
                top_bike_stops=select_of_days.filter(time=i).order_by('-sum_quantity').values('transportatin_bus_id')[0:5]
            data['select_times_list']=list(select_times_list)
            data['top_bus_stops']=list(top_bike_stops)
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, status=200) 

    except django.db.utils.OperationalError:
        return JsonResponse({'err':"테이블 없음"}, status=400)
    except Exception as err:
        return JsonResponse({'err': str(err)}, status=400)


def plotly_mapbox(request):

    weeksort = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    choice_days_t = datetime.datetime.today().weekday()
    choice_day_week = weeksort[choice_days_t]
    
    px.set_mapbox_access_token('pk.eyJ1IjoibHVuaXZlOTgiLCJhIjoiY2w2bjk3Z2Q2MHRvYjNrbjB0bGx3bGo3MSJ9.03OSIuFEfJj_ko78H0YZ2A')
    seoulgeo = json.load(open('apps/static/assets/json/seoulhjd.geojson', encoding='utf-8'))

    # 인구분포도 지도
    pm = Population.objects.all().filter(day_of_week=choice_day_week)

    pm_data = [
        {
            '행정동ID': x.hangjungdong_id,
            '요일': x.day_of_week,
            '시간': x.ref_time,
            '요일+시간': x.day_of_week + x.ref_time,
            '10세미만': x.number_0_9,
            '10대': x.number_10_19,
            '20대': x.number_20_29,
            '30대': x.number_30_39,
            '40대': x.number_40_49,
            '50대': x.number_50_59,
            '60대': x.number_60_69,
            '70세이상': x.number_70_field,
            '총 인구수': x.number_0_9 +  x.number_10_19 + x.number_20_29 + x.number_30_39 + x.number_40_49 + x.number_50_59 + x.number_60_69 + x.number_70_field
        } for x in pm
    ]

    population_df = pd.DataFrame(pm_data) 
    population_df['요일'] = pd.Categorical(population_df['요일'], categories=weeksort, ordered=True)
    population_df = population_df.sort_values(by=['요일', '시간'], ascending=True)

    for i in list(seoulgeo['features']) :
        adm_cd2 = i['properties']['adm_cd2']
        fin = adm_cd2[0:8]
        i['properties']['fin'] = fin
        
    fig1 = px.choropleth(population_df, geojson=seoulgeo, locations=population_df.행정동ID, featureidkey='properties.fin', 
        center={'lat': 37.565, 'lon': 126.986}, color='총 인구수', color_continuous_scale='tealgrn', animation_frame='요일+시간',
        hover_data=['10세미만', '10대', '20대', '30대', '40대', '50대', '60대', '70세이상'])

    fig1.update_geos(fitbounds="locations", visible=False)
    
    population_map = plot(fig1, output_type='div')


    # 주거구분 지도
    bm = Building.objects.all()

    bm_data = [
        {
            '주거/직장': x.building_category,
            '상세구분':  x.building_detail,
            '행정동': x.hangjungdong,
            '구군': x.gugun,
            '구군행정동': x.gugun + ' ' + x.hangjungdong,
            '건축물 수': x.building_count
        } for x in bm
    ]
    building_df = pd.DataFrame(bm_data)
    
    fig2 = px.choropleth_mapbox(building_df, geojson=seoulgeo, locations=building_df.구군, featureidkey='properties.sggnm', center={'lat': 37.565, 'lon': 126.986}, color=building_df.상세구분)
    
    fig2.update_geos(fitbounds='locations', visible=False)

    building_map = plot(fig2, output_type='div')
    
    return render(request, 'home/plotly_mapbox.html', 
    {'population_map': population_map, 'building_map' : building_map})
