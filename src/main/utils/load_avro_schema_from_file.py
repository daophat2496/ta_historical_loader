from confluent_kafka import avro

def LoadAvroSchemaFromFile(_schema_file_path) :
	key_schema_string = """
	{"type" : "string"}
	"""

	key_schema = avro.loads(key_schema_string)
	value_schema = avro.load(_schema_file_path)

	return key_schema, value_schema
