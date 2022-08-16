from pyspark.sql.types import *
from pyspark.sql.functions import to_date, col, year, count
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("yarn").getOrCreate()

user="root"
password="1234"
url = "jdbc:mysql://localhost:3306/ubuntu"
driver = "com.mysql.cj.jdbc.Driver"
dbtable="RENTAL_PER_YEAR"

# 컬럼명, 타입 지정
eng_columns = StructType([
		StructField('bike_num', IntegerType(), True),
		StructField('rental_date_time', StringType(), True),
		StructField('rental_stop_id', IntegerType(), True),
		StructField('rental_stop_name', StringType(), True),
		StructField('del', StringType(), True),
		StructField('return_date_time', StringType(), True),
		StructField('return_stop_id', IntegerType(), True),
		StructField('return_stop_name', StringType(), True),
		StructField('del2', StringType(), True),
		StructField('usetime', IntegerType(), True),
		StructField('distance', IntegerType(), True)
])

# 합쳐줄 빈 DF 생성
## 스키마 생성
example = spark.read.option('header', 'true').schema(eng_columns).csv('hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_대여이력_정보_2206.csv')
example_schema = example.schema

## 빈 DF 생성
union_df = spark.createDataFrame([], example_schema)


# 파일 모두 불러오기
## 2022 (01-06월)
for m in range(1, 7): 
	files = spark.read.option('header', 'true').schema(eng_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_대여이력_정보_220{m}.csv')
	union_df = union_df.union(files)


## 2021
for m in range(1, 13): 
	if m >= 10 :
		files = files = spark.read.option('header', 'true').schema(eng_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_대여이력_정보_21{m}.csv')
		union_df = union_df.union(files)
	else :
		files = spark.read.option('header', 'true').schema(eng_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_대여이력_정보_210{m}.csv')
		union_df = union_df.union(files)


## 2020 (01-12월 / 7, 8월은 합쳐서 작성되어 있음 - 07_08)
### check) 각 월 데이터 잘 들어가있는지 추후 확인해보기
for m in range(1, 13): 
	if m == 7 :
		files = spark.read.option('header', 'true').schema(eng_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_대여이력_정보_2007_08.csv')
		union_df = union_df.union(files)
	elif m == 8 :
		pass
	else :
		if m >= 10 :
			files = files = spark.read.option('header', 'true').schema(eng_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_대여이력_정보_20{m}.csv')
			union_df = union_df.union(files)
		else :
			files = spark.read.option('header', 'true').schema(eng_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_대여이력_정보_200{m}.csv')
			union_df = union_df.union(files)

## 2019 (06-12월 / 06~10월 : _1, 2, 3 / 11월 : _1, 2 / 12월 : X)
### check) 각 월 데이터 잘 들어가있는지 추후 확인해보기
for m in range(6, 13): 
	if m <= 10 :
		for i in range(1, 4) :
			if m == 10 :
				files = spark.read.option('header', 'true').schema(eng_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_대여이력_정보_19{m}_{i}.csv')
				union_df = union_df.union(files)

			else :
				files = spark.read.option('header', 'true').schema(eng_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_대여이력_정보_190{m}_{i}.csv')
				union_df = union_df.union(files)
	elif m == 11 :
		for i in range(1, 3) :
			files = spark.read.option('header', 'true').schema(eng_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_대여이력_정보_19{m}_{i}.csv')
			union_df = union_df.union(files)
	else :
		files = spark.read.option('header', 'true').schema(eng_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/서울특별시_공공자전거_대여이력_정보_19{m}.csv')
		union_df = union_df.union(files)




# 필요한 열만 선택하여 새로운 DF 생성
rental_per_year = union_df.select(union_df.rental_date_time, union_df.rental_stop_id)


# 날짜로 데이터타입 변경하여, 연도만 추출
rental_per_year = rental_per_year.select(to_date(col("rental_date_time")).alias("date"), col("rental_stop_id"))

rental_per_year = rental_per_year.select(year(col("date")).alias("year"), col("rental_stop_id"))

# 연도별 카운트
rental_per_year = rental_per_year.groupBy("year").count()

# count column rename
rental_per_year = rental_per_year.withColumnRenamed("count", "use_count")

# 저장
rental_per_year.write.jdbc(url, dbtable, "append", properties={"driver":driver, "user": user, "password": password})