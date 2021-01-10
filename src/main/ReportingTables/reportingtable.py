from abc import ABCMeta
import utils.load_avro_schema_from_file as LoadAvroSchema
from confluent_kafka.avro import AvroProducer

class reportingtable(metaclass = ABCMeta) :
	
	def __init__(self, kafka_producer_config, topic_name, schema_file_path, start_date, end_date, client_id_list, batch_size) :
		self.kafka_producer_config = kafka_producer_config
		self.topic_name = topic_name
		self.schema_file_path = schema_file_path
		self.start_date = start_date
		self.end_date = end_date
		self.client_id_list = client_id_list
		self.batch_size = batch_size
		self.current_index = 0

	@abc.abstractmethod
	def GetQuery(index, limit) :
		return

	@abc.abstractmethod
	def ParseRecord(record) :
		return

	def ProduceMessages(records) :
		schema_key, schema_value = LoadAvroSchema.LoadAvroSchemaFromFile(self.schema_file_path)
		for record in records:
			message_key, messgae_value = ParseRecord(record)
			producer = AvroProducer(self.kafka_producer_config, default_schema_key = schema_key, default_schema_value = schema_value)

			try :
				producer.produce(topic = self.topic_name, key = message.key, value = message.value)
			except Exception as e :
				print(f"[Topic {self.topic_name}] [Error record: {record}]: {e}")
			else :
				print(f"Producer message successfuly")

	def ProcessObject(cursor) :
