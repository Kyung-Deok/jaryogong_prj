from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import to_date, col, date_format, avg

spark = SparkSession.builder.master("yarn").appName("pyspark").getOrCreate()

user="root"
password="1234"
url = "jdbc:mysql://localhost:3306/ubuntu"
driver = "com.mysql.cj.jdbc.Driver"
dbtable="avg_quantity_voucher"

# 컬럼 지정 (voucher 이후 컬럼들은 불필요했으므로 별도 지정하지 않고 가져오지 않음)
columns = StructType([
    StructField('date', StringType(), True),
    StructField('time', IntegerType(), True),
    StructField('bike_stop_id', IntegerType(), False),
    StructField('bike_stop_name', StringType(), True),
    StructField('voucher', StringType(), True)
])

# 지정한 컬럼명과 타입으로 불러와서, sample_df 생성
sample_df = spark.read.option('header', 'true').schema(columns).csv('hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_1701.csv')

# template sample 스키마 
sample_schema = sample_df.schema

voucher_df = spark.createDataFrame([], sample_schema)

# 파일 불러오기
# 17 ~ 22년 (22년 이전은 1~12월, 22년은 1~6월)
for j in range(17, 23):
    if j not in (21, 22):
       for i in range(1, 13):
            if i < 10:
                tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}0{i}.csv')
                voucher_df = voucher_df.union(tmp)
            else:
                tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}{i}.csv')
                voucher_df = voucher_df.union(tmp)

    elif j == 21:
       for i in range(1, 13):
            if i == 1:
                tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}0{i}.csv')
                voucher_df = voucher_df.union(tmp)
            elif i in range(4, 10): 
                tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}0{i}.csv')
                voucher_df = voucher_df.union(tmp)
            elif i > 10:
                tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}{i}.csv')
                voucher_df = voucher_df.union(tmp)

    elif j == 22:
        for i in range(1, 7):
            tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}0{i}.csv')
            voucher_df = voucher_df.union(tmp)

# 필요없는 컬럼 삭제
voucher_df = voucher_df.drop(voucher_df.bike_stop_id)
voucher_df = voucher_df.drop(voucher_df.bike_stop_name)

# StringType을 날짜 포맷으로 변환
voucher_df = voucher_df.withColumn('date', to_date(col('date'), 'yyyy-MM-dd')).withColumn("day_of_week", date_format(col('date'), "E"))

# 요일별 > 시간별 > 정기권 별 count
voucher_df = voucher_df.groupBy("day_of_week", "time", "voucher").count().sort("day_of_week", "time", "voucher")

# 요일별/시간별/이용권별 사용자 평균 내기
voucher_df = voucher_df.groupBy("day_of_week", "time", "voucher").agg(avg(col('count')).alias('avg_voucher_quantity')).sort("day_of_week", "time", "voucher")


# DB 저장
voucher_df.write.jdbc(url, dbtable, "append", properties={"driver":driver, "user": user, "password": password})

#spark session 종료
spark.stop()