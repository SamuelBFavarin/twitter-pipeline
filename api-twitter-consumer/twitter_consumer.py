import tweepy
import json

from pub_sub_publisher import PubSubPublisher
  
credentials_twitter = json.load(open('./credentials/api_credentials.json'))
credentials_gcloud = json.load(open('./credentials/gcloud_credentials.json'))

#TWITTER API SETUP
ACCESS_TOKEN = credentials_twitter['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = credentials_twitter['ACCESS_TOKEN_SECRET']
CONSUMER_KEY = credentials_twitter['CONSUMER_KEY']
CONSUMER_SECRET = credentials_twitter['CONSUMER_SECRET']
FOLLOW_USERS = [2941621343, 44196397, 797869498757955589, 2579497028]

#GCLOUD SETUP
PROJECT_ID = credentials_gcloud['PROJECT_ID']
TOPIC_ID = credentials_gcloud['TOPIC_ID']

#AVRO SCHEMA
AVRO_SCHEMA = './avro-schema/tweets_schema.json'

class TwitterConsumer(tweepy.Stream):
    
    def on_status(self, status):
        
        message = {
            'id': status.id,
            'id_user': status.user.id,
            'message': status.text,
            'created_at': status.created_at.strftime("%Y-%m-%d %H:%M:%S")             
        }
        
        pub_sub_publisher = PubSubPublisher(PROJECT_ID, TOPIC_ID, AVRO_SCHEMA)
        pub_sub_publisher.publish(message)
        print(message)

print("Listing tweets...")
consumer = TwitterConsumer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
consumer.filter(follow=FOLLOW_USERS)
consumer.sample()