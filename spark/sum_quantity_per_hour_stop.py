from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import to_date, col, date_format, sum

spark = SparkSession.builder.master("yarn").appName("pyspark").getOrCreate()

user="root"
password="1234"
url = "jdbc:mysql://localhost:3306/ubuntu"
driver = "com.mysql.cj.jdbc.Driver"
dbtable="sum_quantity_per_hour_stop"

# 컬럼 지정
# 데이터에서 row하나당 1번의 사용량으로 볼 수 있으므로, 집계시 각 시간별 row갯수로 진행할 것임
columns = StructType([
    StructField('date', StringType(), True),
    StructField('time', IntegerType(), True),
    StructField('bike_stop_id', IntegerType(), False)
])

# 지정한 컬럼명과 타입으로 불러와서, sample_df 생성
sample_df = spark.read.option('header', 'true').schema(columns).csv('hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_1701.csv')

# template sample 스키마 
sample_schema = sample_df.schema

fact_table_df = spark.createDataFrame([], sample_schema)

# 파일 불러오기
# 17 ~ 22년 (22년 이전은 1~12월, 22년은 1~6월)
for j in range(17, 23):
    if j not in (21, 22):
       for i in range(1, 13):
            if i < 10:
                tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}0{i}.csv')
                fact_table_df = fact_table_df.union(tmp)
            else:
                tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}{i}.csv')
                fact_table_df = fact_table_df.union(tmp)

    elif j == 21:
       for i in range(1, 13):
            if i == 1:
                tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}0{i}.csv')
                fact_table_df = fact_table_df.union(tmp)
            elif i in range(4, 10): 
                tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}0{i}.csv')
                fact_table_df = fact_table_df.union(tmp)
            elif i > 10:
                tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}{i}.csv')
                fact_table_df = fact_table_df.union(tmp)

    elif j == 22:
        for i in range(1, 7):
            tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}0{i}.csv')
            fact_table_df = fact_table_df.union(tmp)

# StringType을 날짜 포맷으로 변환
fact_table_df = fact_table_df.withColumn('date', to_date(col('date'), 'yyyy-MM-dd')).withColumn("day_of_week", date_format(col('date'), "E"))

fact_table_df = fact_table_df.groupBy("bike_stop_id", "day_of_week", "time").count().sort("bike_stop_id", "day_of_week", "time")

# 특정 시간에 사용 이력이 아예 없는 대여소도 있어, avg가 아닌 sum으로 진행하였음.
fact_table_df = fact_table_df.groupBy("bike_stop_id", "day_of_week", "time").agg(sum(col('count')).alias('sum_quantity')).sort("bike_stop_id", "day_of_week", "time")

# DB 저장
fact_table_df.write.jdbc(url, dbtable, "append", properties={"driver":driver, "user": user, "password": password})

#spark session 종료
spark.stop()