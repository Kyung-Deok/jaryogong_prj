from kafka import KafkaConsumer
from json import loads
import time

# topic, broker list
consumer = KafkaConsumer(
    'stream_bikes',
     bootstrap_servers=['ubuntu:9091', 'ubuntu:9092', 'ubuntu:9093'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     value_deserializer=lambda x: loads(x.decode('utf-8')),
     consumer_timeout_ms=1000
)

# consumer list를 가져온다
print('[begin] get consumer list')
for message in consumer:
    time.sleep(60)
    print("Topic: %s, Partition: %d, Offset: %d, Key: %s" % (
        message.topic, message.partition, message.offset, message.key, 
    ))
print('[end] get consumer list')
