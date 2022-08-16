from pyspark.sql.types import *
from pyspark.sql.functions import lit, when

from pyspark import SparkContext
from pyspark.sql import SparkSession
# sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
dbtable="building"

# 컬럼명, 타입 지정
building_columns = StructType([
        StructField('building_detail', StringType() ,True),
            StructField('del_city', StringType() ,True),
                StructField('gugun', StringType() ,True),
                    StructField('hangjungdong', StringType() ,True),
                        StructField('building_count', IntegerType() ,True),
                        ])

# 지정한 컬럼명과 타입으로 불러오기
building = spark.read.format('csv').option('header', 'true').schema(building_columns).load('hdfs://localhost:9000/home/ubuntu/crawling/crawling_building_usage_purpose.csv')

# 2열 삭제
building = building.drop(building[1])

# auto_increment id 위해서 빈 열 추가
# building = building.withColumn('building_id', lit(' '))

# 건축물 유형 열 building_category 생성 후 값 넣기
building = building.withColumn("building_category", when(building.building_detail=="주거용", "주거용")
        .otherwise("업무용"))


# building_detail 바꾸기
building = building.withColumn("building_detail", when(building.building_detail=="주거용", "주거용")
        .when(building.building_detail=="문교사회용", "교육연구용")
        .when(building.building_detail=="상업용", "상업용")
        .when(building.building_detail=="공공용", "공공업무용")
        .when(building.building_detail=="공업용", "공업용"))

# 열의 순서 재배치 (id, category, detail, gugun, hangjungdong, count)
building = building.select("building_category", "building_detail", "gugun", "hangjungdong", "building_count")

# 저장
building.write.jdbc(url, dbtable, "append", properties={"driver":driver, "user": user, "password": password})