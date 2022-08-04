import requests
from kafka import KafkaProducer
from json import dumps

# pip install kafka-python

service_key = ''
url = '{service_key}'

# pagination
url_list = []

ontime_datas = []

# kafka는 messaging protocol처럼 움직이는 것처럼 보일뿐, 그렇지는 않다.
# acks all(-1; 모두 신호), 0 (신호 아예 X), 1 (처리때마다 신호)
producer = KafkaProducer(
    bootstrap_servers=['ubuntu:9091,ubuntu:9092,ubuntu:9093'],
    value_serializer=lambda v: dumps(v).encode('utf-8'),
    acks=0
    )

for i in range(len(ontime_datas)):
    ontime_data={}
    producer.send()
    producer.flush()
