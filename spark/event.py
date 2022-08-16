from pyspark.sql import SparkSession
from pyspark.sql import functions
from pyspark.sql.types import *

#sparksession 드라이버 프로세스 얻기
spark = SparkSession.builder.master("yarn").getOrCreate()

#mysql 연결
user="root"
password="1234"
url = "jdbc:mysql://localhost:3306/ubuntu"
driver = "com.mysql.cj.jdbc.Driver"
dbtable="metro_station"


eng_columns = StructType([
                StructField('metro_station_id', IntegerType(), True),
                StructField('metro_station_name', StringType(), True),
                StructField('metro_station_category', StringType(), True),
                StructField('metro_station_lat', DecimalType(10,7), True),
                StructField('metro_station_lot', DecimalType(10,7), True),
])

metro_station_df = spark.read.format('csv').option('header', 'true').schema(eng_columns).load('hdfs://localhost:9000/home/ubuntu/file_data/csv/metro_station_master.csv')

# mysql 저장
metro_station_df.write.jdbc(url, dbtable, "append", properties={"driver":driver, "user": user, "password": password})

# spark 종료
spark.stop()