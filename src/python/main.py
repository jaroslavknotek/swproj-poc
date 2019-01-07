import analyser
import loader
import visualiser
import json


reddit_cred = {}
twitter_cred = {}

print("reading data from credentials")
with open('config/credentials.json') as f:
    data = json.load(f)
    reddit_cred = data["reddit"]
    twitter_cred = data["twitter"]

topic = "apple"
print("The topic is: ", topic )

headers = loader.construct_header(reddit_cred, "https://www.reddit.com/api/v1/access_token")

print("getting reddit data")
reddit_records = loader.get_data_reddit(headers,topic)

print("getting twitter data")
twitter_records = loader.get_data_twitter(twitter_cred, topic)

records = reddit_records + twitter_records

print("analysing data")
histogram = analyser.histogram_of_counts(records)

print("visualising")
visualiser.visualize_pairs(histogram)




