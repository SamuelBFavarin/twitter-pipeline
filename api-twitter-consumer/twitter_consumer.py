import tweepy
import json

from pub_sub_publisher import PubSubPublisher
  
credentials_twitter = json.load(open('api_credentials.json'))
credentials_gcloud = json.load(open('gcloud_credentials.json'))

#TWITTER API SETUP
ACCESS_TOKEN = credentials_twitter['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = credentials_twitter['ACCESS_TOKEN_SECRET']
CONSUMER_KEY = credentials_twitter['CONSUMER_KEY']
CONSUMER_SECRET = credentials_twitter['CONSUMER_SECRET']
FOLLOW_USER = 2941621343

#GCLOUD SETUP
PROJECT_ID = credentials_gcloud['PROJECT_ID']
TOPIC_ID = credentials_gcloud['TOPIC_ID']

class TwitterConsumer(tweepy.Stream):
    
    def on_status(self, status):
        
        message = {
            'id': status.id,
            'id_user': status.user.id,
            'message': status.text,
            'created_at': status.created_at             
        }
        
        pub_sub_publisher = PubSubPublisher(PROJECT_ID, TOPIC_ID)
        pub_sub_publisher.publish(message)
        print(message)

print("Listing tweets...")
consumer = TwitterConsumer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
consumer.filter(follow=[FOLLOW_USER])
consumer.sample()