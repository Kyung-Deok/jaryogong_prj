from pyspark.sql.types import *
from pyspark.sql.functions import bround, col, expr, to_date, date_format, substring, expr, when, split, explode

from pyspark import SparkContext
from pyspark.sql import SparkSession
import sys

sc = SparkContext()
spark = SparkSession.builder.getOrCreate()

user="root"
password="1234"
url = "jdbc:mysql://localhost:3306/ubuntu"
driver = "com.mysql.cj.jdbc.Driver"
dbtable="transportation_metro"

# 컬럼명, 타입 지정
set_columns = StructType([
	StructField('del_date', StringType() ,True),
	StructField('depart_metro_station_id', IntegerType() ,True),
	StructField('arrival_metro_station_id', IntegerType() ,True),
	StructField('metro_00', IntegerType() ,True),
	StructField('metro_01', IntegerType() ,True),
	StructField('metro_02', IntegerType() ,True),
	StructField('metro_03', IntegerType() ,True),
	StructField('metro_04', IntegerType() ,True),
	StructField('metro_05', IntegerType() ,True),
	StructField('metro_06', IntegerType() ,True),
	StructField('metro_07', IntegerType() ,True),
	StructField('metro_08', IntegerType() ,True),
	StructField('metro_09', IntegerType() ,True),
	StructField('metro_10', IntegerType() ,True),
	StructField('metro_11', IntegerType() ,True),
	StructField('metro_12', IntegerType() ,True),
	StructField('metro_13', IntegerType() ,True),
	StructField('metro_14', IntegerType() ,True),
	StructField('metro_15', IntegerType() ,True),
	StructField('metro_16', IntegerType() ,True),
	StructField('metro_17', IntegerType() ,True),
	StructField('metro_18', IntegerType() ,True),
	StructField('metro_19', IntegerType() ,True),
	StructField('metro_20', IntegerType() ,True),
	StructField('metro_21', IntegerType() ,True),
	StructField('metro_22', IntegerType() ,True),
	StructField('metro_23', IntegerType() ,True)
])

# 지정한 컬럼명과 타입으로 불러오기
sample_df = spark.read.option('header', 'true').schema(set_columns).csv('hdfs://localhost:9000/home/ubuntu/file_data/csv/kscc_dx_ra_od_220211.csv')


# 비어있는 스키마 
empt_schema = sample_df.schema
union_df = spark.createDataFrame([], empt_schema)

#1
for m in range(1, 10):
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/kscc_dx_ra_od_22010{m}.csv')
	union_df = union_df.union(tmp)

for n in range(10, 32):
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/kscc_dx_ra_od_2201{n}.csv')
	union_df = union_df.union(tmp)

#2
for m in range(1, 10):
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/kscc_dx_ra_od_22020{m}.csv')
	union_df = union_df.union(tmp)

for n in range(10, 29):
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/kscc_dx_ra_od_2202{n}.csv')
	union_df = union_df.union(tmp)


#3
for m in range(1, 10):
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/kscc_dx_ra_od_22030{m}.csv')
	union_df = union_df.union(tmp)

for n in range(10, 32):
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/kscc_dx_ra_od_2203{n}.csv')
	union_df = union_df.union(tmp)



#5
for m in range(1, 10):
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/kscc_dx_ra_od_22050{m}.csv')
	union_df = union_df.union(tmp)

for n in range(10, 32):
	tmp = spark.read.option('header', 'true').schema(set_columns).csv(f'hdfs://localhost:9000/home/ubuntu/file_data/csv/kscc_dx_ra_od_2205{n}.csv')
	union_df = union_df.union(tmp)





# 버스 / 지하철 구분: 승차/하차 정류장 ID 9999보다 큰 것 = 버스 정류장 ID
union_df =union_df.withColumn('check_metro', expr("depart_metro_station_id < 9999"))\
.where(col('check_metro')=='true')

# 날짜 컬럼 date타입으로 형변환, 요일 표시
union_df = union_df.withColumn('del_date', to_date(col('del_date'), "yyyyMMdd"))\
.withColumn("day_of_week", date_format(col('del_date'), "E"))


# 열 삭제
union_df = union_df\
.drop(union_df.del_date)\
.drop(union_df.check_metro)

# null 0으로 바꾸기
union_df.createOrReplaceTempView('udf')

union_df = spark.sql("""
select 
day_of_week, depart_metro_station_id, arrival_metro_station_id,
ifnull(metro_00, '0') as metro_00, ifnull(metro_01, '0') as metro_01, ifnull(metro_02, '0') as metro_02, ifnull(metro_03, '0') as metro_03,
ifnull(metro_04, '0') as metro_04, ifnull(metro_05, '0') as metro_05, ifnull(metro_06, '0') as metro_06, ifnull(metro_07, '0') as metro_07,
ifnull(metro_08, '0') as metro_08, ifnull(metro_09, '0') as metro_09, ifnull(metro_10, '0') as metro_10, ifnull(metro_11, '0') as metro_11,
ifnull(metro_12, '0') as metro_12, ifnull(metro_13, '0') as metro_13, ifnull(metro_14, '0') as metro_14, ifnull(metro_15, '0') as metro_15,
ifnull(metro_16, '0') as metro_16, ifnull(metro_17, '0') as metro_17, ifnull(metro_18, '0') as metro_18, ifnull(metro_19, '0') as metro_19,
ifnull(metro_20, '0') as metro_20, ifnull(metro_21, '0') as metro_21, ifnull(metro_22, '0') as metro_22, ifnull(metro_23, '0') as metro_23
from udf
""")


# day_category와 depart_metro_station_id, arrival_metro_station_id를 기준으로 sum

union_df = spark.sql("""
select 
day_of_week, depart_metro_station_id, arrival_metro_station_id,
sum(metro_00) as metro_00, sum(metro_01) as metro_01, sum(metro_02) as metro_02, sum(metro_03) as metro_03,
sum(metro_04) as metro_04, sum(metro_05) as metro_05, sum(metro_06) as metro_06, sum(metro_07) as metro_07,
sum(metro_08) as metro_08, sum(metro_09) as metro_09, sum(metro_10) as metro_10, sum(metro_11) as metro_11,
sum(metro_12) as metro_12, sum(metro_13) as metro_13, sum(metro_14) as metro_14, sum(metro_15) as metro_15,
sum(metro_16) as metro_16, sum(metro_17) as metro_17, sum(metro_18) as metro_18, sum(metro_19) as metro_19,
sum(metro_20) as metro_20, sum(metro_21) as metro_21, sum(metro_22) as metro_22, sum(metro_23) as metro_23
from udf
group by day_of_week, depart_metro_station_id, arrival_metro_station_id
order by day_of_week, depart_metro_station_id, arrival_metro_station_id
""")

union_df = spark.sql("""
select 
day_of_week, depart_metro_station_id, arrival_metro_station_id,
ifnull(sum(metro_00), 0) as m_00, ifnull(sum(metro_01), 0) as m_01, ifnull(sum(metro_02), 0) as m_02, ifnull(sum(metro_03), 0) as m_03,
ifnull(sum(metro_04), 0) as m_04, ifnull(sum(metro_05), 0) as m_05, ifnull(sum(metro_06), 0) as m_06, ifnull(sum(metro_07), 0) as m_07,
ifnull(sum(metro_08), 0) as m_08, ifnull(sum(metro_09), 0) as m_09, ifnull(sum(metro_10), 0) as m_10, ifnull(sum(metro_11), 0) as m_11,
ifnull(sum(metro_12), 0) as m_12, ifnull(sum(metro_13), 0) as m_13, ifnull(sum(metro_14), 0) as m_14, ifnull(sum(metro_15), 0) as m_15,
ifnull(sum(metro_16), 0) as m_16, ifnull(sum(metro_17), 0) as m_17, ifnull(sum(metro_18), 0) as m_18, ifnull(sum(metro_19), 0) as m_19,
ifnull(sum(metro_20), 0) as m_20, ifnull(sum(metro_21), 0) as m_21, ifnull(sum(metro_22), 0) as m_22, ifnull(sum(metro_23), 0) as m_23
from udf
group by day_of_week, depart_metro_station_id, arrival_metro_station_id
order by day_of_week, depart_metro_station_id, arrival_metro_station_id
""")


# 피봇
unpivotExpr = "stack(24, 'm_00', m_00, 'm_01', m_01, 'm_02', m_02, 'm_03', m_03, 'm_04', m_04, 'm_05', m_05, 'm_06', m_06, 'm_07', m_07, 'm_08', m_08, 'm_09', m_09, 'm_10', m_10, 'm_11', m_11, 'm_12', m_12, 'm_13', m_13, 'm_14', m_14, 'm_15', m_15, 'm_16', m_16, 'm_17', m_17, 'm_18', m_18, 'm_19', m_19, 'm_20', m_20, 'm_21', m_21, 'm_22', m_22, 'm_23', m_23)"

unpivot_union_df = union_df.select('day_of_week', 'depart_metro_station_id', 'arrival_metro_station_id', expr(unpivotExpr))

# 열 이름 바꾸기
unpivot_union_df =unpivot_union_df.withColumnRenamed('col0', 'time').withColumnRenamed('col1', 'passenger')


# 시간만 남기기
unpivot_union_df = unpivot_union_df.withColumn('ref_time' ,split(col('time'), '_'))\
.withColumn('time', explode(col('ref_time'))).select('day_of_week', 'depart_metro_station_id', 'arrival_metro_station_id','time','passenger')


unpivot_union_df = unpivot_union_df.withColumn('check_time', expr("time != 'm'")).where(col('check_time')=='true')

unpivot_union_df = unpivot_union_df.drop(unpivot_union_df.check_time)


# 저장
unpivot_union_df.write.jdbc(url, dbtable, "append", properties={"driver":driver, "user": user, "password": password})