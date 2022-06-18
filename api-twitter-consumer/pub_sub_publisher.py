import avro
import io
import json
from avro.io import BinaryEncoder, DatumWriter
from google.cloud import pubsub_v1
from google.pubsub_v1.types import Encoding
from google.api_core.exceptions import NotFound

class PubSubPublisher():
    
    def __init__(self, project_id: str, topic_id: str, avro_schema_file: str):
        self.project_id = project_id
        self.topic_id = topic_id
        self.avro_schema_file = avro_schema_file
        
        self.publisher_client = pubsub_v1.PublisherClient()
        self.topic_path = self.publisher_client.topic_path(project_id, topic_id)   
        
    
    def publish(self, message: str):
        
        # Prepare to write Avro records to the binary output stream.
        avro_schema = avro.schema.parse(open(self.avro_schema_file, "rb").read())
        writer = DatumWriter(avro_schema)
        bout = io.BytesIO()
        
        try:
            # Get the topic encoding type.
            topic = self.publisher_client.get_topic(request={"topic": self.topic_path})
            encoding = topic.schema_settings.encoding

            # Encode the data according to the message serialization type.
            if encoding == Encoding.BINARY:
                encoder = BinaryEncoder(bout)
                writer.write(message, encoder)
                data = bout.getvalue()
                print(f"Preparing a binary-encoded message:\n{data.decode()}")
                
            elif encoding == Encoding.JSON:
                data_str = json.dumps(message)
                print(f"Preparing a JSON-encoded message:\n{data_str}")
                data = data_str.encode("utf-8")
                
            else:
                print(f"No encoding specified in {self.topic_path}. Abort.")
                exit(0)

            future = self.publisher_client.publish(self.topic_path, data)
            print(f"Published message ID: {future.result()}")

        except NotFound:
            print(f"{self.topic_id} not found.")
