import findspark
findspark.init()

from pyspark import SparkConf, SparkContext 
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.streaming import DataStreamReader
import time
import requests
import os

# spark_version = '3.2.2'
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.2'
# os.environ['JAVA_HOME']='/usr/bin/jvm/java-11-openjdk-arm64'
# Session 생성
spark = SparkSession.builder.appName('Stream_bikes').getOrCreate()

stream_kafka_data = spark.readStream.format("kafka")\
    .option("kafka.bootstrap.servers", "ubuntu:9091,ubuntu:9092,ubuntu:9093")\
    .option('subscribe','stream_bikes')\
    .option('startingOffsets','earliest')\
    .load()
# stream_kafka_data.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

stream_kafka_data.printSchema()