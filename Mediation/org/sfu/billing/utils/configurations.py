from pyspark.sql import SparkSession
from org.sfu.billing.utils.propertiesReader import Properties


class SparkConfig:

    properties = Properties.load_properties()

    @staticmethod
    def get_spark():
        print(SparkConfig.properties["DATABASE"]["DB_INPUT_URI"])
        spark = SparkSession.builder.appName('Billing_Engine_Listener') \
            .config("spark.jars.packages","org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.0,org.mongodb.spark:mongo-spark-connector_2.11:2.3.0") \
            .config('spark.mongodb.input.uri', SparkConfig.properties["DATABASE"]["DB_INPUT_URI"]) \
            .config('spark.mongodb.output.uri', SparkConfig.properties["DATABASE"]["DB_OUTPUT_URI"]) \
            .getOrCreate()

        spark.sparkContext.setLogLevel('WARN')

        return spark

    @staticmethod
    def get_events():
        spark = SparkConfig.get_spark()
        bootstrap_servers = SparkConfig.properties["KAFKA"]["SERVER_IP"] + ':' + SparkConfig.properties["KAFKA"]["SERVER_PORT"]
        topics = SparkConfig.properties["KAFKA"]["TOPIC_NAMES"]

        print("type of ============ ", type(bootstrap_servers))

        messages = spark.readStream.format('kafka') \
            .option('kafka.bootstrap.servers', bootstrap_servers) \
            .option('subscribe', topics) \
             .load()

        return messages
    
    

def save_batch(df, epoch_id):
        df.write.format("com.mongodb.spark.sql.DefaultSource").mode("append") \
            .option("database","billing") \
            .option("collection", "custEventSource") \
            .save()
        pass
    
def main():
    #spark = SparkSession.builder.getOrCreate()
    spark_config = SparkConfig()  # ("events")
    messages = spark_config.get_events()

    stream = messages.writeStream.foreachBatch(save_batch).start()
    print("type of stream: ", type(stream))
    stream.awaitTermination(900000)
    #print("Spark version:  ",spark.version)


if __name__ == '__main__':
    main()
