import tweepy
import json
  
credentials = json.load(open('api_credentials.json'))

ACCESS_TOKEN = credentials['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = credentials['ACCESS_TOKEN_SECRET']
CONSUMER_KEY = credentials['CONSUMER_KEY']
CONSUMER_SECRET = credentials['CONSUMER_SECRET']
FOLLOW_USER = 2941621343

class TwitterConsumer(tweepy.Stream):

    def on_status(self, status):
        
        data = {
            'id': status.id,
            'id_user': status.user.id,
            'message': status.text,
            'created_at': status.created_at             
        }
        
        print(data)

print("Listing tweets...")
consumer = TwitterConsumer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
consumer.filter(follow=[FOLLOW_USER])
consumer.sample()