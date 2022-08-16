from pyspark.sql import SparkSession
from pyspark.sql import functions
from pyspark.sql.types import *

spark = SparkSession.builder.master("yarn").getOrCreate()

#mysql 연결
user="root"
password="1234"
url = "jdbc:mysql://localhost:3306/ubuntu"
driver = "com.mysql.cj.jdbc.Driver"
dbtable="bike_stop_info"


# 따릉이 마스터 정보.csv : df1 - 3096
df1_columns = StructType([
		StructField('bike_stop_code', StringType(), True),
		StructField('address1', StringType(), True),
		StructField('address2', StringType(), True),
		StructField('bike_stop_lat', DecimalType(10,7), True),
		StructField('bike_stop_lot', DecimalType(10,7), True),
])

df1 = spark.read.format('csv').option('header', 'true').schema(df1_columns).load("hdfs://localhost:9000/home/ubuntu/file_data/csv/서울시_따릉이_대여소_마스터정보.csv")

# 공공 자전거 대여소 정보.csv : df2 - 2696

df2_columns = StructType([
		StructField('bike_stop_id', StringType(), True),
		StructField('name', StringType(), True),
		StructField('gu', StringType(), True),
		StructField('address', StringType(), True),
		StructField('bike_stop_lat', DecimalType(10,7), True),
		StructField('bike_stop_lot', DecimalType(10,7), True)
])

# 해당 파일이 문제있을 경우, bike_stop_info_2112로 변경
df2 = spark.read.format('csv').option('header', 'true').schema(df2_columns).load('hdfs://localhost:9000/home/ubuntu/file_data/csv/bike_stop_info_2206.csv')

# 불필요한 column 삭제
df1 = df1.drop(df1.address1)
df1 = df1.drop(df1.address2)

df2 = df2.drop(df2.name)
df2 = df2.drop(df2.gu)
df2 = df2.drop(df2.address)

# join : lat + lot으로 매칭
bike_stop_info_df = df1.join(df2, ['bike_stop_lat', 'bike_stop_lot'], 'inner')

# mysql 저장
bike_stop_info_df.write.jdbc(url, dbtable, "append", properties={"driver":driver, "user": user, "password": password})

#spark session 
spark.stop()