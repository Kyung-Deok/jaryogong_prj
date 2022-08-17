from pprint import pprint
import django
from time import time
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, Avg,Q
from .models import AvgQuantityVoucher, BikeStopInformation, Event, OntimeRentalInfo, RentalPerYear, RentalRecordPerHour, SumQuantityBikeStop, SumQuantityPerHourStop, TransportationBus, Population, Building, TransportationMetro
import datetime
import json
import plotly.express as px
from plotly.offline import plot
from pprint import pprint
import pandas as pd
import plotly.graph_objects as go


def index(request):
    if request.method=="GET":
        # 뒤에 있는 놈들 값 다 받아오기
        index_dict={}
        index_dict['stream_keyword'] = stream_keyword()
        index_dict['years_of_user'] = years_of_user()

        index_dict['vouchers'] = vouchers()
        index_dict['rent_tops'] = rent_tops()
        index_dict['events'] = events()
        # index_dict['trans_traffic']=trans_traffic()

        return render(request, 'home/index.html', {'data': index_dict})
    else : 
        context={}
        # 응답 받는다. 그 데이터를 쌓는다 
        choice_result = request.POST.get('choice_one')
        print(choice_result)
        context['choice_result'] = choice_result

        context['vouchers'] = vouchers(choice_days=choice_result)
        pprint(context['vouchers'])
        context['rent_tops'] = rent_tops(choice_days=choice_result)
        context['events'] = events(choice_days=choice_result)
        # context['trans_traffic'] = trans_traffic(choice_days=choice_result)
        print(context)
        # return JsonResponse(context)
        return render(request, 'home/index.html', {'context': context})

        
def stream_keyword() :
        # 오늘의 따릉이 대여건수, 가장 많이 빌려진 대여소, 자전거 거치율100% 이상 대여소 주소, 자전거 거치율 50% 미만 대여소 주소
        rent_total = OntimeRentalInfo.objects.aggregate(sum_data=Sum('parking_amount')-Sum('holder_amount'))
        rent_top5 = OntimeRentalInfo.objects.all().order_by('-parking_amount')[0:5]
        parking_higher = OntimeRentalInfo.objects.filter(parking_rate__gt=100)
        parking_lower= OntimeRentalInfo.objects.filter(parking_rate__lt=50)
        
        data = {'rent_total' : rent_total,
                'rent_top5': list(rent_top5),
                'parking_higher' : int(len(parking_higher)),
                'parking_lower' : int(len(parking_lower))
        }
        return data

def years_of_user():
    datas={}

    datas["total_2019"] = RentalPerYear.objects.filter(year='2019').aggregate(sum_years=Sum('use_count'))
    datas["total_2020"] = RentalPerYear.objects.filter(year='2020').aggregate(sum_years=Sum('use_count'))
    datas["total_2021"] = RentalPerYear.objects.filter(year='2021').aggregate(sum_years=Sum('use_count'))
    
    return datas


    
def vouchers(choice_days=datetime.datetime.today().strftime('%Y-%m-%d')):
    #choice_days :  YYYY-MM-DD
    days_of_weeks= ['Mon','Tue', 'Wed', 'Thu','Fri','Sat','Sun']

    if choice_days is None :
        choice_days_t = datetime.datetime.today().weekday()
        choice_day_week = days_of_weeks[choice_days_t]
    choice_daysf = datetime.datetime.strptime(choice_days,'%Y-%m-%d').weekday()
    choice_day_week = days_of_weeks[choice_daysf]

    print("choice_days : ",choice_days, "날짜 : ",choice_day_week)
    # 오전 시간대 (:11) 대여소 총 집계한 일일권 사용자
    # 오전 구분(원하는 날짜만, 그중 기준시간 데이터만,오전시간만 집계)``
 
    data={}

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

    # 출근집계, 퇴근집계
    d_avg_morning = d_morning_vouchers.aggregate(sum_data=Sum('avg_voucher_quantity'))
    d_avg_evenning = d_evenning_vouchers.aggregate(sum_data=Sum('avg_voucher_quantity'))
    r_avg_morning = r_morning_vouchers.aggregate(sum_data=Sum('avg_voucher_quantity'))
    r_avg_evenning = r_evenning_vouchers.aggregate(sum_data=Sum('avg_voucher_quantity'))
    n_avg_morning = n_morning_vouchers.aggregate(sum_data=Sum('avg_voucher_quantity'))
    n_avg_evenning = n_evenning_vouchers.aggregate(sum_data=Sum('avg_voucher_quantity'))
    
    data['d_avg_morning'] = d_avg_morning
    data['d_avg_evenning'] = d_avg_evenning
    data['r_avg_morning'] = r_avg_morning
    data['r_avg_evenning'] = r_avg_evenning
    data['n_avg_morning'] = n_avg_morning
    data['n_avg_evenning'] = n_avg_evenning
    return data

# 시간대 별 대여소 별 대여량, 날짜 필터 걸고, 요일 별 필터
# 요일별 시간대로 쪼개진 사용량 : 대여량 top5 => 손대면 표시 
def rent_tops(choice_days=datetime.datetime.today().strftime('%Y-%m-%d')):
    #요일별 
    days_of_weeks= ['Mon','Tue', 'Wed', 'Thu','Fri','Sat','Sun']
    if choice_days is None :
        choice_days_t = datetime.datetime.today().weekday()
        choice_day_week = days_of_weeks[choice_days_t]
    choice_daysf = datetime.datetime.strptime(choice_days,'%Y-%m-%d').weekday()
    choice_day_week = days_of_weeks[choice_daysf]
    
    print("요일숫자",choice_day_week)
    # 대여소id, 기준요일을 가져온다, 해당요일에 해당하는, 옆에 Sum
    data={}
    # 기준일에 대한 요일에 따른 데이터를 집어온다 : x요일에 대여소 별로 시간 별로 찍힌것
    select_of_days = SumQuantityPerHourStop.objects.filter(day_of_week=choice_day_week).values('time','sum_quantity')
    print("해당 요일별 대여소 별로 시간기준 찍힌것 :", len(list(select_of_days))) #65000여개
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
    return data


    
def events(choice_days=datetime.datetime.today().strftime('%Y-%m-%d')):
    data = {}
    split_date = datetime.datetime.strptime(choice_days,'%Y-%m-%d')
    days_of_weeks= ['Mon','Tue', 'Wed', 'Thu','Fri','Sat','Sun']
    if choice_days is None :
        choice_days_t = datetime.datetime.today().weekday()
        choice_day_week = days_of_weeks[choice_days_t]
    choice_daysf = datetime.datetime.strptime(choice_days,'%Y-%m-%d').weekday()
    choice_day_week = days_of_weeks[choice_daysf]

    # 이벤트 정보 불러오기 : 2020 -2022년도 까지
    date_event_datas = Event.objects.filter(Q(year__in=['2020','2021','2022']) & Q(year=split_date.year)& Q(month=split_date.month) & Q(date=split_date.day)).values('year','month','date')[:1000]
    data['date_event_datas'] = list(date_event_datas)

    if data['date_event_datas'] is None :
        data['message'] = "값이 없습니다."

    
        # req.body 불러오기 : 날짜, 카테고리, 이름, 주소
        # choice_cate = request.POST.get('cate_event_datas', None)
        # choice_name = request.POST.get('name_event_datas', None)
        # choice_addr = request.POST.get('addr_event_datas', None)
        

    # 이벤트가 있었던 일자에 평소 사용량
    # 이벤트가 있었던 일자에 시간대 별 사용량

    select_times_list=[]
    select_event_times_list=[]
    for i in range(0,24):
        sum_usual_dates = SumQuantityPerHourStop.objects.filter(Q(day_of_week=choice_day_week)& Q(time=i)).values("sum_quantity")[:1000].aggregate(sum_data=Sum('sum_quantity'))
        sum_event_dates = SumQuantityBikeStop.objects.filter(Q(date=choice_days)& Q(time=i)).values("sum_quantity")[:1000].aggregate(sum_data=Sum('sum_quantity'))
        
        select_times_list.append(sum_usual_dates)
        select_event_times_list.append(sum_event_dates)
    data['sum_usual_datas']=list(select_times_list)
    data['sum_events_datas']=list(select_event_times_list)


    return data
    
def trans_traffic(choice_days=datetime.datetime.today().strftime('%Y-%m-%d')):
    # 지하철과 따릉이만 비교
    #요일별 
    days_of_weeks= ['Mon','Tue', 'Wed', 'Thu','Fri','Sat','Sun']
    if choice_days is None :
        choice_days_t = datetime.datetime.today().weekday()
        choice_day_week = days_of_weeks[choice_days_t]
    choice_daysf = datetime.datetime.strptime(choice_days,'%Y-%m-%d').weekday()
    choice_day_week = days_of_weeks[choice_daysf]
    
    
    # 대여소id, 기준요일을 가져온다, 해당요일에 해당하는, 옆에 Sum
    data={}
    # 기준일에 대한 요일에 따른 데이터를 집어온다 : x요일에 대여소 별로 시간 별로 찍힌것
    select_of_days = TransportationMetro.objects.filter(day_of_week=choice_day_week).values('time','passenger')
    
    print(len(select_of_days))
    # 집계한다. 시간대별 총 데이터
    select_times_list=[]
    for i in range(0,24):
        # 요일마다 시간별
        select_times = select_of_days.filter(time=i).aggregate(sum_data=Sum('passenger'))
        select_times_list.append(select_times)
        # top 5
        top_bike_stops=select_of_days.filter(time=i).order_by('-passenger').values('transportation_metro_id')[0:5]
    data['select_times_list_b']=list(select_times_list)
    data['top_metro_stops']=list(top_bike_stops)

    return data

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