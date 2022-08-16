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
dbtable="transportation_bus"

# 컬럼명, 타입 지정
set_columns = StructType([
	StructField('del_date', StringType() ,True),
	StructField('depart_bus_stop_id', IntegerType() ,True),
	StructField('arrival_bus_stop_id', IntegerType() ,True),
	StructField('bus_00', IntegerType() ,True),
	StructField('bus_01', IntegerType() ,True),
	StructField('bus_02', IntegerType() ,True),
	StructField('bus_03', IntegerType() ,True),
	StructField('bus_04', IntegerType() ,True),
	StructField('bus_05', IntegerType() ,True),
	StructField('bus_06', IntegerType() ,True),
	StructField('bus_07', IntegerType() ,True),
	StructField('bus_08', IntegerType() ,True),
	StructField('bus_09', IntegerType() ,True),
	StructField('bus_10', IntegerType() ,True),
	StructField('bus_11', IntegerType() ,True),
	StructField('bus_12', IntegerType() ,True),
	StructField('bus_13', IntegerType() ,True),
	StructField('bus_14', IntegerType() ,True),
	StructField('bus_15', IntegerType() ,True),
	StructField('bus_16', IntegerType() ,True),
	StructField('bus_17', IntegerType() ,True),
	StructField('bus_18', IntegerType() ,True),
	StructField('bus_19', IntegerType() ,True),
	StructField('bus_20', IntegerType() ,True),
	StructField('bus_21', IntegerType() ,True),
	StructField('bus_22', IntegerType() ,True),
	StructField('bus_23', IntegerType() ,True)
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
union_df =union_df.withColumn('check_bus', expr("depart_bus_stop_id > 9999"))\
.where(col('check_bus')=='true')

# 날짜 컬럼 date타입으로 형변환, 요일 표시
union_df = union_df.withColumn('del_date', to_date(col('del_date'), "yyyyMMdd"))\
.withColumn("day_of_week", date_format(col('del_date'), "E"))


# 열 삭제
union_df = union_df\
.drop(union_df.del_date)\
.drop(union_df.check_bus)

# null 0으로 바꾸기
union_df.createOrReplaceTempView('udf')

union_df = spark.sql("""
select 
day_of_week, depart_bus_stop_id, arrival_bus_stop_id,
ifnull(bus_00, '0') as bus_00, ifnull(bus_01, '0') as bus_01, ifnull(bus_02, '0') as bus_02, ifnull(bus_03, '0') as bus_03,
ifnull(bus_04, '0') as bus_04, ifnull(bus_05, '0') as bus_05, ifnull(bus_06, '0') as bus_06, ifnull(bus_07, '0') as bus_07,
ifnull(bus_08, '0') as bus_08, ifnull(bus_09, '0') as bus_09, ifnull(bus_10, '0') as bus_10, ifnull(bus_11, '0') as bus_11,
ifnull(bus_12, '0') as bus_12, ifnull(bus_13, '0') as bus_13, ifnull(bus_14, '0') as bus_14, ifnull(bus_15, '0') as bus_15,
ifnull(bus_16, '0') as bus_16, ifnull(bus_17, '0') as bus_17, ifnull(bus_18, '0') as bus_18, ifnull(bus_19, '0') as bus_19,
ifnull(bus_20, '0') as bus_20, ifnull(bus_21, '0') as bus_21, ifnull(bus_22, '0') as bus_22, ifnull(bus_23, '0') as bus_23
from udf
""")


# day_category와 depart_bus_stop_id, arrival_bus_stop_id를 기준으로 sum

union_df = spark.sql("""
select 
day_of_week, depart_bus_stop_id, arrival_bus_stop_id,
sum(bus_00) as bus_00, sum(bus_01) as bus_01, sum(bus_02) as bus_02, sum(bus_03) as bus_03,
sum(bus_04) as bus_04, sum(bus_05) as bus_05, sum(bus_06) as bus_06, sum(bus_07) as bus_07,
sum(bus_08) as bus_08, sum(bus_09) as bus_09, sum(bus_10) as bus_10, sum(bus_11) as bus_11,
sum(bus_12) as bus_12, sum(bus_13) as bus_13, sum(bus_14) as bus_14, sum(bus_15) as bus_15,
sum(bus_16) as bus_16, sum(bus_17) as bus_17, sum(bus_18) as bus_18, sum(bus_19) as bus_19,
sum(bus_20) as bus_20, sum(bus_21) as bus_21, sum(bus_22) as bus_22, sum(bus_23) as bus_23
from udf
group by day_of_week, depart_bus_stop_id, arrival_bus_stop_id
order by day_of_week, depart_bus_stop_id, arrival_bus_stop_id
""")

union_df = spark.sql("""
select 
day_of_week, depart_bus_stop_id, arrival_bus_stop_id,
ifnull(sum(bus_00), 0) as b_00, ifnull(sum(bus_01), 0) as b_01, ifnull(sum(bus_02), 0) as b_02, ifnull(sum(bus_03), 0) as b_03,
ifnull(sum(bus_04), 0) as b_04, ifnull(sum(bus_05), 0) as b_05, ifnull(sum(bus_06), 0) as b_06, ifnull(sum(bus_07), 0) as b_07,
ifnull(sum(bus_08), 0) as b_08, ifnull(sum(bus_09), 0) as b_09, ifnull(sum(bus_10), 0) as b_10, ifnull(sum(bus_11), 0) as b_11,
ifnull(sum(bus_12), 0) as b_12, ifnull(sum(bus_13), 0) as b_13, ifnull(sum(bus_14), 0) as b_14, ifnull(sum(bus_15), 0) as b_15,
ifnull(sum(bus_16), 0) as b_16, ifnull(sum(bus_17), 0) as b_17, ifnull(sum(bus_18), 0) as b_18, ifnull(sum(bus_19), 0) as b_19,
ifnull(sum(bus_20), 0) as b_20, ifnull(sum(bus_21), 0) as b_21, ifnull(sum(bus_22), 0) as b_22, ifnull(sum(bus_23), 0) as b_23
from udf
group by day_of_week, depart_bus_stop_id, arrival_bus_stop_id
order by day_of_week, depart_bus_stop_id, arrival_bus_stop_id
""")


# 피봇
unpivotExpr = "stack(24, 'b_00', b_00, 'b_01', b_01, 'b_02', b_02, 'b_03', b_03, 'b_04', b_04, 'b_05', b_05, 'b_06', b_06, 'b_07', b_07, 'b_08', b_08, 'b_09', b_09, 'b_10', b_10, 'b_11', b_11, 'b_12', b_12, 'b_13', b_13, 'b_14', b_14, 'b_15', b_15, 'b_16', b_16, 'b_17', b_17, 'b_18', b_18, 'b_19', b_19, 'b_20', b_20, 'b_21', b_21, 'b_22', b_22, 'b_23', b_23)"

unpivot_union_df = union_df.select('day_of_week', 'depart_bus_stop_id', 'arrival_bus_stop_id', expr(unpivotExpr))

# 열 이름 바꾸기
unpivot_union_df =unpivot_union_df.withColumnRenamed('col0', 'time').withColumnRenamed('col1', 'passenger')


# 시간만 남기기
unpivot_union_df = unpivot_union_df.withColumn('ref_time' ,split(col('time'), '_'))\
.withColumn('time', explode(col('ref_time'))).select('day_of_week', 'depart_bus_stop_id', 'arrival_bus_stop_id','time','passenger')


unpivot_union_df = unpivot_union_df.withColumn('check_time', expr("time != 'b'")).where(col('check_time')=='true')

unpivot_union_df = unpivot_union_df.drop(unpivot_union_df.check_time)


# 저장
unpivot_union_df.write.jdbc(url, dbtable, "append", properties={"driver":driver, "user": user, "password": password})