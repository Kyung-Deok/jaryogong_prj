from pyspark.sql import SparkSession
from pyspark.sql.types import *

#sparksession 드라이버 프로세스 얻기
spark = SparkSession.builder.master("yarn").getOrCreate()

#mysql 연결
user="root"
password="1234"
url = "jdbc:mysql://localhost:3306/ubuntu"
driver = "com.mysql.cj.jdbc.Driver"
dbtable="bus_stop"

# 스키마 설정
eng_columns = StructType([
                StructField('bus_stop_id', IntegerType(), True),
                StructField('bus_stop_name', StringType(), True),
                StructField('category', StringType(), True),
                StructField('bus_stop_number', StringType(), True),
                StructField('bus_stop_lat', DecimalType(10,7), True),
                StructField('bus_stop_lot', DecimalType(10,7), True),
                StructField('bus_info', StringType(), True)
])

# 불러오기
bus_stop = spark.read.format('csv').option('header', 'true').schema(eng_columns).load('hdfs://localhost:9000/home/ubuntu/file_data/csv/서울시_정류장마스터_정보.csv')

# 불필요한 column 삭제
bus_stop = bus_stop.drop(bus_stop.category)
bus_stop = bus_stop.drop(bus_stop.bus_stop_number)
bus_stop = bus_stop.drop(bus_stop.bus_info)

# mysql 저장
bus_stop.write.jdbc(url, dbtable, "append", properties={"driver":driver, "user": user, "password": password})

#spark session 종료
spark.stop()