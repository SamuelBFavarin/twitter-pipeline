from concurrent import futures
from google.cloud import pubsub_v1
import json


class PubSubPublisher():
    
    def __init__(self, project_id: str, topic_id: str):
        self.project_id = project_id
        self.topic_id = topic_id
        
        self.publisher = pubsub_v1.PublisherClient()
        self.topic_path = self.publisher.topic_path(project_id, topic_id)   
        self.publish_futures = []   
        
    
    def publish(self, message: str):
        
        try:
            publish_future = self.publisher.publish(self.topic_path, json.dumps(message).encode("utf-8"))  
            publish_future.add_done_callback(self._get_callback(publish_future, message))
            self.publish_futures.append(publish_future)
            return True
        
        except:
            print(f"Error on publish this message: {message}")            
            return False
                
    
    def _get_callback(self, publish_future: pubsub_v1.publisher.futures.Future, data: str):
        
        def callback(publish_future: pubsub_v1.publisher.futures.Future) -> None:
            try:
                print(publish_future.result(timeout=60))
            except futures.TimeoutError:
                print(f"Publishing {data} timed out.")

        return callback
