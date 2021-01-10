import utils.load_avro_schema_from_file as LoadAvroSchema
from confluent_kafka.avro import AvroProducer
import uuid
import json

def SendRecord(_producer_config, _topic_name, _schema_file_path, _record_value) :
	key_schema, value_schema = LoadAvroSchema.LoadAvroSchemaFromFile(_schema_file_path)

	producer = AvroProducer(_producer_config, default_key_schema = key_schema, default_value_schema = value_schema)
	key = str(uuid.uuid4())
	value = json.loads(_record_value)

	try :
		producer.produce(topic = _topic_name, key = key, value = value)
	except Exception as e:
		print(f"Exception while producing record <{_record_value}> to topic <{_topic_name}> : {e}")
	else :
		print(f"Successful produce record <{_record_value}> to topic <{_topic_name}>")

	producer.flush()
