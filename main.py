from json import loads
from kafka import KafkaConsumer,KafkaProducer
import sys
"""
This script is responsible for consuming data from incoming topic. Each message is checked for its timestamp. 
If message timestamp falls within the specified range, message will be sent to output topic.
"""

def createConsumer(incoming_topic,kafka_brokers):
    """
    Create Kafka Consumer
    :param incoming_topic: topic name to comsumer
    :param kafka_brokers: list of kafka brokers
    :return: Kafka Consumer object
    """
    return KafkaConsumer(incoming_topic, bootstrap_servers=kafka_brokers,
                         auto_offset_reset='earliest', enable_auto_commit=True,
                         auto_commit_interval_ms=1000)

def createProducer(kafka_brokers):
    """
    Create Kafka Producer
    :param kafka_brokers: list of kafka brokers
    :return: Kafka Producer object
    """
    return KafkaProducer(bootstrap_servers=kafka_brokers,acks='all',batch_size=32768)

  
def fillMessages(output_topic,producer,consumer):
    """
    Filter messages from incoming topic and write to output topic
    :param output_topic: topic name to produce messages
    :param producer: Kafka producer object
    :param consumer: Kafka consumer object
    """
    for message in consumer:
        message = loads(message.value.decode('utf-8'))
        # Checking if incoming message falls between specified time range
        if message['timestamp'] > 1618398000000 & message['timestamp'] < 1618405200000:
            producer.send(output_topic,str(message).encode('utf-8'))    

if __name__ == "__main__":
  brokers_list = sys.argv[3:]
  inTopic = sys.argv[1]
  outTopic = sys.argv[2]

  kConsumer = createConsumer(inTopic,brokers_list)
  
  kProducer = createProducer(brokers_list)

  fillMessages(outTopic,kProducer,kConsumer)

