from pyspark.sql.types import *
from pyspark.sql.functions import bround, col, expr, to_date, date_format, substring, sort, orderBy, asc

from pyspark import SparkContext
from pyspark.sql import SparkSession
import sys



# sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

sc = SparkContext()
spark = SparkSession.builder.getOrCreate()

user="root"
password="1234"
url = "jdbc:mysql://localhost:3306/ubuntu"
driver = "com.mysql.cj.jdbc.Driver"
dbtable="population"

# 컬럼명, 타입 지정
set_columns = StructType([
	StructField('del_date', StringType() ,True),
	StructField('ref_time', StringType() ,True),
	StructField('hangjungdong_id', IntegerType() ,True),
	StructField('del_tot', StringType() ,True),
	StructField('c4', StringType() ,True),
	StructField('c5', StringType() ,True),
	StructField('c6', StringType() ,True),
	StructField('c7', StringType() ,True),
	StructField('c8', StringType() ,True),
	StructField('c9', StringType() ,True),
	StructField('c10', StringType() ,True),
	StructField('c11', StringType() ,True),
	StructField('c12', StringType() ,True),
	StructField('c13', StringType() ,True),
	StructField('c14', StringType() ,True),
	StructField('c15', StringType() ,True),
	StructField('c16', StringType() ,True),
	StructField('c17', StringType() ,True),
	StructField('c18', StringType() ,True),
	StructField('c19', StringType() ,True),
	StructField('c20', StringType() ,True),
	StructField('c21', StringType() ,True),
	StructField('c22', StringType() ,True),
	StructField('c23', StringType() ,True),
	StructField('c24', StringType() ,True),
	StructField('c25', StringType() ,True),
	StructField('c26', StringType() ,True),
	StructField('c27', StringType() ,True),
	StructField('c28', StringType() ,True),
	StructField('c29', StringType() ,True),
	StructField('c30', StringType() ,True),
	StructField('c31', StringType() ,True)
])

# 지정한 컬럼명과 타입으로 불러오기
population1 = spark.read.option('header', 'true').schema(set_columns).csv('hdfs://localhost:9000/home/ubuntu/file_data/csv/LOCAL_PEOPLE_DONG_2201.csv')


# 비어있는 스키마 
pop_schema = population1.schema

union_pop = spark.createDataFrame([], pop_schema)

#2017
for m in range(1, 10): 
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/LOCAL_PEOPLE_DONG_170{m}.csv')
	union_pop = union_pop.union(tmp)

for n in range(10, 13): 
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/LOCAL_PEOPLE_DONG_17{n}.csv')
	union_pop = union_pop.union(tmp)
##### 3714240
        
# 2018
for m in range(1, 10): 
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/LOCAL_PEOPLE_DONG_180{m}.csv')
	union_pop = union_pop.union(tmp)

for n in range(10, 13): 
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/LOCAL_PEOPLE_DONG_18{n}.csv')
	union_pop = union_pop.union(tmp)
##### 7428480

#2019
for m in range(1, 10): 
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/LOCAL_PEOPLE_DONG_190{m}.csv')
	union_pop = union_pop.union(tmp)

for n in range(10, 13): 
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/LOCAL_PEOPLE_DONG_19{n}.csv')
	union_pop = union_pop.union(tmp)
##### 11010432


#2020
for m in range(1, 10): 
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/LOCAL_PEOPLE_DONG_200{m}.csv')
	union_pop = union_pop.union(tmp)

for n in range(10, 13): 
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/LOCAL_PEOPLE_DONG_20{n}.csv')
	union_pop = union_pop.union(tmp)
#####14734848


#2021
for m in range(1, 10): 
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/LOCAL_PEOPLE_DONG_210{m}.csv')
	union_pop = union_pop.union(tmp)

for n in range(10, 13): 
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/LOCAL_PEOPLE_DONG_21{n}.csv')
	union_pop = union_pop.union(tmp)
#####18449088



#2022
for i in range(1, 8):
    tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/LOCAL_PEOPLE_DONG_220{i}.csv')
    union_pop = union_pop.union(tmp)
#####20606400



# 열 형 변환 - int 숫자형으로 (소수점 없애기)
for i in range(4, 32): 
	union_pop = union_pop\
	.withColumn(f'c{i}', col(f'c{i}').cast("int"))


# del_date컬럼 substring사용해서 " 제거하기
union_pop = union_pop.withColumn('del_date', substring('del_date', 1, 8))


# 날짜 컬럼 date타입으로 형변환, 요일 표시
union_pop = union_pop.withColumn('del_date', to_date(col('del_date'), "yyyyMMdd"))\
.withColumn("day_of_week", date_format(col('del_date'), "E"))


# 열 합치기
'''
0_9 = 4, 18
10_19 = 5, 6, 19, 20
20_29 = 7, 8, 21, 22
30_39 = 9, 10, 23, 24
40_49 = 11, 12, 25, 26
50_59 = 13, 14, 27, 28
60_69 = 15, 16, 29, 30
70_ = 17, 31
'''
union_pop = union_pop\
.withColumn('0_9', (col('c4') + col('c18')))\
.withColumn('10_19', (col('c5') + col('c6') + col('c19') + col('c20')))\
.withColumn('20_29', (col('c7') + col('c8') + col('c21') + col('c22')))\
.withColumn('30_39', (col('c9') + col('c10') + col('c23') + col('c24')))\
.withColumn('40_49', (col('c11') + col('c12') + col('c25') + col('c26')))\
.withColumn('50_59', (col('c13') + col('c14') + col('c27') + col('c28')))\
.withColumn('60_69', (col('c15') + col('c16') + col('c29') + col('c30')))\
.withColumn('70_', (col('c17') + col('c31')))


# 열 삭제
union_pop = union_pop.drop(union_pop.del_tot)



union_pop = union_pop.drop(union_pop.c4)
union_pop = union_pop.drop(union_pop.c5)
union_pop = union_pop.drop(union_pop.c6)
union_pop = union_pop.drop(union_pop.c7)
union_pop = union_pop.drop(union_pop.c8)
union_pop = union_pop.drop(union_pop.c9)
union_pop = union_pop.drop(union_pop.c10)
union_pop = union_pop.drop(union_pop.c11)
union_pop = union_pop.drop(union_pop.c12)
union_pop = union_pop.drop(union_pop.c13)
union_pop = union_pop.drop(union_pop.c14)
union_pop = union_pop.drop(union_pop.c15)
union_pop = union_pop.drop(union_pop.c16)
union_pop = union_pop.drop(union_pop.c17)
union_pop = union_pop.drop(union_pop.c18)
union_pop = union_pop.drop(union_pop.c19)
union_pop = union_pop.drop(union_pop.c20)
union_pop = union_pop.drop(union_pop.c21)
union_pop = union_pop.drop(union_pop.c22)
union_pop = union_pop.drop(union_pop.c23)
union_pop = union_pop.drop(union_pop.c24)
union_pop = union_pop.drop(union_pop.c25)
union_pop = union_pop.drop(union_pop.c26)
union_pop = union_pop.drop(union_pop.c27)
union_pop = union_pop.drop(union_pop.c28)
union_pop = union_pop.drop(union_pop.c29)
union_pop = union_pop.drop(union_pop.c30)
union_pop = union_pop.drop(union_pop.c31)


# date 컬럼 삭제
union_pop = union_pop.drop(union_pop.del_date)


# 열의 순서 재배치
union_pop = union_pop.select("day_of_week", "ref_time", "hangjungdong_id", "0_9", "10_19", "20_29", "30_39", "40_49", "50_59", "60_69", "70_")

# day_of_week와 hangjungdong_id를 기준으로 sum
union_pop.createOrReplaceTempView('upop')


union_pop = spark.sql("""
select day_of_week, ref_time, hangjungdong_id, sum(0_9) as 0_9, sum(10_19) as 10_19, sum(20_29) as 20_29, sum(30_39) as 30_39, sum(40_49) as 40_49, sum(50_59) as 50_59, sum(60_69) as 60_69, sum(70_) as 70_
from upop
group by day_of_week, ref_time, hangjungdong_id
order by day_of_week, ref_time asc
""")

# 정렬
# union_pop = union_pop.orderBy(['day_of_week', 'ref_time'], ascending=[1,1])
union_pop = union_pop.orderBy(col('day_of_week').asc())

# 저장
union_pop.write.jdbc(url, dbtable, "append", properties={"driver":driver, "user": user, "password": password})