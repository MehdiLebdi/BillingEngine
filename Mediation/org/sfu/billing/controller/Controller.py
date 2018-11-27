from org.sfu.billing.utils.configurations import SparkConfig
from org.sfu.billing.utils import configurations
from org.sfu.billing.controller import Controller
#from pyspark.sql.streaming import StreamingQuery


class Controller():
    """
    Controller class is used to control lifecycle of entire application. It invokes all modules in logical sequence.
    Execution pipeline is Mediation module, Rating Module and Persistent module        
    """

    def raw_cdr(self):
        spark_config = SparkConfig()
        events = spark_config.get_events()
        return events
    
    def process(self):
        events = self.raw_cdr()

        #TODO:
        #1. getDeviceType
        #2. map raw_cdr to df
        #3. Invoke mediation on df
        #4. Invoke Rating on df

        #TODO: save_batch method should be invoked from dataloader module
        stream = events.writeStream.foreachBatch(configurations.save_batch).start()
        self.stopStreaming(stream)
        pass
        
        
    def stopStreaming(self,streamingQuery):
        streamingQuery.awaitTermination(900000)

def main():
    controller = Controller()
    controller.process()

if __name__ == "__main__":
    main()

#from pyspark import SparkConf, SparkContext
#import sys
#import math

#assert sys.version_info >= (3, 5)  # make sure we have Python 3.5+
#import re, datetime, uuid
#from pyspark.sql import SQLContext, Row, SparkSession, functions, types
#from pyspark.sql.types import StructType, StructField, StringType, FloatType, TimestampType


#def main(topic):

    
#    spark = SparkSession.builder.appName('Read_Stream') \
#            .config('spark.cassandra.connection.host','localhost') \
#            .config('spark.mongodb.input.uri','mongodb://Mirza_Tauqeer:<pwd>@ds031968.mlab.com:31968/billing') \
#            .config('spark.mongodb.output.uri', 'mongodb://Mirza_Tauqeer:<pwd>@ds031968.mlab.com:31968/billing') \
#            .getOrCreate()

#        messages = spark.readStream.format('kafka') \
#        .option('kafka.bootstrap.servers', 'localhost:9092') \
#        .option('subscribe', topic).load()
#        ###

#    spark.sparkContext.setLogLevel('WARN')

#    values = messages.select(messages['value'].cast('string'))
#    split_val = functions.split(values['value'], ',')
#    values = values.withColumn('custId', split_val.getItem(0))
#    values = values.withColumn('startDate', split_val.getItem(1))
#    #values = values.withColumn('endDate', split_val.getItem(2))

#    stream = values.writeStream.foreachBatch(save_batch).start()

#    stream.awaitTermination(600)

#if __name__ == "__main__":
#    topic = "events"
#    main(topic)

