from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("ReadCSV").getOrCreate()
df = spark.read.csv("hdfs://localhost:9000/path/to/file.csv")
df.show()
spark.stop()