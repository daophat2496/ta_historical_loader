from decouple import config
import send_record as SendRecord

def main() :
	bootstrap_servers = config("BOOTSTRAP_SERVERS", default = "localhost:9092")
	schema_registry_url = config("SCHEMA_REGISTRY_URL", default = "localhost:8005")
	print(bootstrap_servers)
	print(schema_registry_url)
	producer_config = {
		"bootstrap.servers" : bootstrap_servers
		, "schema.registry.url" : schema_registry_url
	}

	record_value = '{"clientid":1234,"name":"pd","description":"pd","status":"pd","uuid":"pd","viewinggroupname":"pd","starttimestamp":123,"endtimestamp":123,"createdtimestamp":123,"creatorid":"1","lastmodifiedtimestamp":123,"lastmodifieduserid":"1","ssor":"qTest","ssorid":"2","extrainfo":"pd","eventtype":"INSERT","customfields":"pd","messageversion":"pd"}'

	SendRecord.SendRecord(producer_config, "projects", "./files/projects.avsc", record_value)

if __name__ == "__main__":
	main()
