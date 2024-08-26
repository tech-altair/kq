import tweepy
import json
import os

# set up API credentials
bearer_token = os.getenv('AAAAAAAAAAAAAAAAAAAAALAUvgEAAAAAza7oo5OeACff4RJMmPjMboxTyZk%3DpMk6RFkaJA5qtrZMxiSswVdount29FOTQXYmEmurPAjfRhIUzO')

# authenticate with X API v2
client = tweepy.Client(bearer_token=bearer_token)

# query for recent tweets mentioning 'Kenya Airways'
query = 'Kenya Airways'
max_results = 100

def scrape_tweets():
    try:
        response = client.search_recent_tweets(query=query, max_results=max_results)
        tweets = response.data

        if tweets:
            tweets_data = [tweet.text for tweet in tweets]
            # save tweets to a JSON file 
            with open('kenya_airways_tweets_v2.json', 'w') as f:
                json.dump(tweets_data, f, indent=4)
            print(f"Successfully fetched and saved {len(tweets)} tweets.")
            return tweets_data  # return data for further processing
        else:
            print("No tweets found for the given query.")
            return []
    except tweepy.TweepyException as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    scrape_tweets() 