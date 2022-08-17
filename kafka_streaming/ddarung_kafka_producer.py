
import time
import requests
from kafka import KafkaProducer
from json import dumps
import json
import re
from pprint import pprint
# kafka는 messaging protocol처럼 움직이는 것처럼 보일뿐, 그렇지는 않다.
# acks all(-1; 모두 신호), 0 (신호 아예 X), 1 (처리때마다 신호)

service_key = '5a4d53625467686535365477586f46'

producer = KafkaProducer(
    bootstrap_servers=['ubuntu:9091','ubuntu:9092','ubuntu:9093'],
    value_serializer=lambda v: dumps(v,ensure_ascii=False).encode('utf-8'),
    acks=0
    )


# parkingBikeTotCnt: 거치된 자전거 수
# rackTotCnt : 거치대 수
# share : 거치율
# stationId : 대여소 id
# stationName : 이름
# lat,lot : 위도, 경도

url_list=[f'http://openapi.seoul.go.kr:8088/{service_key}/json/bikeList/1/1000',f'http://openapi.seoul.go.kr:8088/{service_key}/json/bikeList/1001/2000', f'http://openapi.seoul.go.kr:8088/{service_key}/json/bikeList/2001/3000']
print(url_list)

# ontime_datas = {}

while True:
    '''
    for i in range(len(url_list)):
        res = requests.get(url_list[i])
        parse_data = res.json()['rentBikeStatus']['row']
        ontime_datas.append(a)
    '''
    res1 = requests.get(url_list[0])
    res2 = requests.get(url_list[1])
    res3 = requests.get(url_list[2])
    parse_data1= res1.json()['rentBikeStatus']['row']
    parse_data2=res2.json()['rentBikeStatus']['row']
    parse_data3=res3.json()['rentBikeStatus']['row']
    
    # time_stamps = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
    
    ontime_datas = parse_data1 + parse_data2 + parse_data3
    
    time.sleep(30)
    
    producer.send('stream_bikes2',value=ontime_datas)
    producer.flush()
    
    print('success')
    # 종료는 sys.exit() 구상중 
# 2649 갱신
