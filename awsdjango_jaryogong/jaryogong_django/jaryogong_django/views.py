from django.shortcuts import render, redirect
import json
import re
import requests
import pandas as pd
from .models import Population, Building, Hangjungdong, Event, MetroStation, BusStop, TransportationBus, TransportationMetro, RentalRecordPerHour, ViewSumPopDongBuilding, ViewSumPopDongBuildingWithoutStop, ViewPop, ViewDongBuilding
import plotly.express as px
from plotly.offline import plot
from pprint import pprint
import datetime

def main_page(request):
    return render(request, 'main.html')



#병원데이터베이스 저장
def make_dummy_json(request):
    with open('/dummy_json/전국_정신건강관련기관_위치정보.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    # json에서 정보 불러오기
    for i in range(len(json_data['data'])):
        public_or_privates = (json_data['data'][i]['공공/민간'])
        categories = (json_data['data'][i]['기관구분'])
        address = (json_data['data'][i]['주소'])
        latitude = (json_data['data'][i]['위도'])
        longitude = (json_data['data'][i]['경도'])

        result = TestHostpitalLocation.objects.create(public_or_privates=public_or_privates, categories=categories,
                                                      address=address, latitude=latitude, longitude=longitude)
    return redirect('/')


# plotly mapbox test
def plotly_mapbox(request):

    weeksort = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    # choice_days = request.POST.get('choicedays',None)
    # if choice_days is None :
    choice_days_t = datetime.datetime.today().weekday()
    choice_day_week = weeksort[choice_days_t]
    # choice_daysf = datetime.datetime.strptime(choice_days,'%Y-%m-%d').weekday()
    # choice_day_week = weeksort[choice_daysf]
    
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
            '70세이상': x.number_70_field
        } for x in pm
    ]

    seoulgeo = json.load(open('./dummy_json/seoulhjd.geojson', encoding='utf-8'))
    plotly_mapbox_df = pd.DataFrame(pm_data) 
    plotly_mapbox_df['요일'] = pd.Categorical(plotly_mapbox_df['요일'], categories=weeksort, ordered=True)
    plotly_mapbox_df = plotly_mapbox_df.sort_values(by=['요일', '시간'], ascending=True)
    pprint(plotly_mapbox_df)
    px.set_mapbox_access_token('pk.eyJ1IjoibHVuaXZlOTgiLCJhIjoiY2w2bjk3Z2Q2MHRvYjNrbjB0bGx3bGo3MSJ9.03OSIuFEfJj_ko78H0YZ2A')

    for i in list(seoulgeo['features']) :
        adm_cd2 = i['properties']['adm_cd2']
        fin = adm_cd2[0:8]
        i['properties']['fin'] = fin
    
    seoulgeo1 = json.dumps(seoulgeo)
    
    # fig = px.choropleth_mapbox(plotly_mapbox_df, geojson=seoulgeo, featureidkey='properties.fin', 
    #    center={'lat': 37.565, 'lon': 126.986}, locations=plotly_mapbox_df.hangjungdong_id, color='age_0_9', color_continuous_scale='Blues')
    fig = px.choropleth(plotly_mapbox_df, geojson=seoulgeo, locations=plotly_mapbox_df.행정동ID, featureidkey='properties.fin', 
        center={'lat': 37.565, 'lon': 126.986}, color='70세이상', color_continuous_scale='Blues', animation_frame='요일+시간')

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(title_text='인구 분포도', title_font_size=20)
    
    plot_mapbox = plot(fig, output_type='div')

    return render(request, 'plotly_mapbox.html', {'plot_mapbox': plot_mapbox})

# event TABLE에는 day_of_week column 없음, 요일데이터 X
# 근처장소 날짜 시간, 월~일 요일별 데이터
# 요일필터안 시간대 데이터
def event(request):
    try:
        if request.method == 'POST':
            event_ref_date = json.load(request.body)
            days_of_weeks= ['월','화', '수', '목','금','토','일']
            seoul_gu = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', 
                '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', 
                '용산구', '은평구', '종로구', '중구', '중랑구']
            
            if event_ref_date is None :
                event_date = datetime.datetime.today().weekday()
                event_day_of_week = days_of_weeks[event_date]
            else :
                event_date = datetime.datetime.date(event_ref_date)
                event_day_of_week = days_of_weeks[event_date]
            
            dash_event_data = {}

            event_dates = RentalRecordPerHour.objects.filter(ref_date=event_date)
            event_times = event_dates.filter(Q(time='22') | Q(time='23'))
            event_loc = event_times.filter(seoul_gu in event_addr)

            # count
            event_counts = event_loc.aggregate(('rental_record_per_hour_id').count())

            dash_event_data = {
                'event_dates': event_dates,
                'event_times': event_times,
                'event_loc': event_loc,
                'event_counts': event_counts
            }
            return JsonResponse(dash_event_data, json_dumps_params={'ensure_ascii': False}, status=200) 
        else:
            return JsonResponse(dash_event_data, json_dumps_params={'ensure_ascii': False}, status=200) 
    except ValueError:
        return JsonResponse({'err':'value error'},status=400)   

# transportation TABLE에는 day_of_week column 있음, 요일데이터 Fri, Sun 등등 영문 3글자

def transportation(request):
    try:
        if request.method == 'POST':
            transportation_ref_date = json.load(request.body)

            dash_transportation_data = {}

            bus_day_of_week = TransportationBus.objects.filter()
            metro_day_of_week = TransportationMetro.objects.filter()
            bike_day_of_week = RentalRecordPerHour.objects.filter()

            for i in range(25):
                bus_counts = TransportationBus.objects.filter()
                metro_counts = TransportationMetro.objects.filter()
                bike_counts = RentalRecordPerHour.objects.filter()        

            return JsonResponse(dash_transportation_data, json_dumps_params={'ensure_ascii': False}, status=200) 
        else:
            return JsonResponse(dash_transportation_data, json_dumps_params={'ensure_ascii': False}, status=200) 
    except ValueError:
        return JsonResponse({'err':'value error'},status=400)

   