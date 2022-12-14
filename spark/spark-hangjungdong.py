from pyspark.sql.types import *
from pyspark.sql import SparkSession
import sys

spark = SparkSession.builder.getOrCreate()

user="root"
password="1234"
url = "jdbc:mysql://localhost:3306/ubuntu"
driver = "com.mysql.cj.jdbc.Driver"
dbtable="hangjungdong"

# 컬럼명, 타입 지정
hjd_columns = StructType([
	StructField('del_id', StringType() ,True),
	StructField('hangjungdong_id', IntegerType() ,True),
	StructField('del_city', StringType() ,True),
	StructField('gugun', StringType() ,True),
	StructField('hangjungdong', StringType() ,True),
])

# 지정한 컬럼명과 타입으로 불러오기
hjd = spark.read.format('csv').option('header', 'true').schema(hjd_columns).load('hdfs://localhost:9000/home/ubuntu/file_data/csv/행정동코드_매핑정보_행정동코드.csv')

# 1행 삭제
hjd = hjd.na.drop()

# 1열 삭제
hjd = hjd.drop(hjd[0])

# 2열 삭제
hjd = hjd.drop(hjd[1])

# 저장
hjd.write.jdbc(url, dbtable, "append", properties={"driver":driver, "user": user, "password": password})

# spark 종료
spark.stop()