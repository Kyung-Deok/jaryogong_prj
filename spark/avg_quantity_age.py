from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import to_date, col, date_format, avg

spark = SparkSession.builder.master("yarn").appName("pyspark").getOrCreate()

user="root"
password="1234"
url = "jdbc:mysql://localhost:3306/ubuntu"
driver = "com.mysql.cj.jdbc.Driver"
dbtable="avg_quantity_age"

# 컬럼 지정 (voucher 이후 컬럼들은 불필요했으므로 별도 지정하지 않고 가져오지 않음)
columns = StructType([
    StructField('date', StringType(), True),
    StructField('time', IntegerType(), True),
    StructField('bike_stop_id', IntegerType(), False),
    StructField('bike_stop_name', StringType(), True),
    StructField('voucher', StringType(), True),
    StructField('gender', StringType(), True),
    StructField('age_category', StringType(), True)
])

# 지정한 컬럼명과 타입으로 불러와서, sample_df 생성
sample_df = spark.read.option('header', 'true').schema(columns).csv('hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_1701.csv')

# template sample 스키마 
sample_schema = sample_df.schema

age_df = spark.createDataFrame([], sample_schema)

# 파일 불러오기
# 17 ~ 22년 (22년 이전은 1~12월, 22년은 1~6월)
for j in range(17, 23):
    if j not in (21, 22):
       for i in range(1, 13):
            if i < 10:
                tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}0{i}.csv')
                age_df = age_df .union(tmp)
            else:
                tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}{i}.csv')
                age_df = age_df .union(tmp)

    elif j == 21:
       for i in range(1, 13):
            if i == 1:
                tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}0{i}.csv')
                age_df = age_df .union(tmp)
            elif i in range(4, 10): 
                tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}0{i}.csv')
                age_df = age_df .union(tmp)
            elif i > 10:
                tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}{i}.csv')
                age_df = age_df .union(tmp)

    elif j == 22:
        for i in range(1, 7):
            tmp = spark.read.option('header', 'true').schema(columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_이용정보_시간대별_{j}0{i}.csv')
            age_df = age_df .union(tmp)


# 필요없는 컬럼 삭제
age_df = age_df.drop(age_df.bike_stop_id)
age_df = age_df.drop(age_df.bike_stop_name)
age_df = age_df.drop(age_df.voucher)
age_df = age_df.drop(age_df.gender)

# StringType을 날짜 포맷으로 변환
age_df = age_df.withColumn('date', to_date(col('date'), 'yyyy-MM-dd')).withColumn("day_of_week", date_format(col('date'), "E"))

# 정렬을 위해 텍스트값 수정
age_df = age_df.na.replace('~10대', '0~10대')

# 요일별 > 시간별 > 연령대 별 count
age_df = age_df.groupBy("day_of_week", "time", "age_category").count().sort("day_of_week", "time", "age_category")

# 요일별/시간별/이용권별 사용자 평균 내기
age_df = age_df.groupBy("day_of_week", "time", "age_category").agg(avg(col('count')).alias('avg_age_quantity')).sort("day_of_week", "time", "age_category")

# DB 저장
age_df.write.jdbc(url, dbtable, "append", properties={"driver":driver, "user": user, "password": password})

#spark session 종료
spark.stop()