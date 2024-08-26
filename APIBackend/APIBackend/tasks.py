# from .email import send_otp_mail
from textblob import TextBlob
from celery.utils.log import get_task_logger
from celery import shared_task
from SentimentAnalysis.models import Reviews
from SentimentAnalysis.serializers import AdditionSerializer,ReviewsSerializer
import datetime
from rest_framework import response, status
#scrapping data with beautifulsoup
from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
from ntscraper import Nitter
from SentimentAnalysis.helpers import check_existing_review_by_title_and_description
#get environment variables
import os
from dotenv import load_dotenv
load_dotenv()



logger = get_task_logger(__name__)

#create a global function to call all the tasks
@shared_task(name='APIBackend.tasks.run_all_tasks')
def run_all_tasks():
    # numbers = add_two_numbers.delay(1, 2)
    # division = divide_two_numbers.delay(5, 2)
    twitter = scrap_data_from_twitter.delay()
    scrapping = scrap_data_from_site.delay("https://www.airlineratings.com/airlines/kenya-airways/reviews")
    google = scrap_data_from_google_maps.delay()
    sentiments = get_sentiment.delay()
    return {
        # 'numbers_task_id': numbers.id,
        # 'division_task_id': division.id,
        'twitter_task_id': twitter.id,
        'google_task_id': google.id,
        'sentiments_task_id': sentiments.id
    }

@shared_task(name='APIBackend.tasks.add_two_numbers')
def add_two_numbers(a, b):
    logger.info('add two numbers')
    #store the result in the database
    try:
        result = a + b
        # my_object = {"num_1":a, "num_2":b, "result":result,"date" : datetime.datetime.now()}
        my_object = {"num_1":a, "num_2":b, "result":result}
        # print(my_object)
        
        serializer = AdditionSerializer(data=my_object)
        # print(serializer)
        if serializer.is_valid():
            # print("serializer is valid")
            serializer.save()
        else:
            print("serializer is not paused ")
            # return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return result
    except Exception as e:
        print("error", e)
        return response.Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@shared_task(name='APIBackend.tasks.divide_two_numbers')
def divide_two_numbers(a, b):
    logger.info('dividing two numbers')
    return a / b

@shared_task(name='APIBackend.tasks.scrap_data_from_twitter')
def scrap_data_from_twitter():
    search_params = [
        "Kenya Airways", "KQ", "Kenya Air", "Kenyan Airlines", "Pride of Africa",
        "KenyaAir", "Kenya's Flag Carrier", "East African Carrier", "Kenyan National Airline",
        "KQ Airways", "Kenya's Pride", "KA", "Kenya Air Lines", "Kenya's Wings",
        "The Kenyan Airline", "Kenya National Airways", "KQ.com", "Kenya Airways Limited",
        "Kenya Airways PLC", "Nairobi-based Carrier", "KQ Airline"
    ]
    # search_params = ["Kenya Airways", "KQ"]
    for query in search_params:
        final_tweets = None
        while final_tweets is None:
            final_tweets = get_tweets_with_params(query)
            
        serialized_data = []
        for review in final_tweets:
            # print(review)
            source = "twitter-x"
            source_link = review[0]
            title = review[1]
            description = review[1]
            # print("source", source, "source_link", source_link, "title", title, "description", description)
            try:
                my_object = {
                    "source": source,
                    "source_link": source_link,
                    "title": title,
                    "description": description,
                    "sentiment": None  # Use None instead of null
                }
                review_exits = check_existing_review_by_title_and_description(title, description)
                if review_exits:
                    print("Review already exists")
                    continue
                serializer = ReviewsSerializer(data=my_object)
                if serializer.is_valid():
                    print("serializer is valid and saving")
                    serializer.save()
                    serialized_data.append(serializer.data)
                else:
                    print("serializer is not valid")
                    print(serializer.errors)  # Print serializer errors
            except Exception as e:
                print("error", e)

            # print(final_tweets)
            
        # tweets = scraper.get_tweets(query, mode="hashtag", number=10)
        # final_tweets = []
        # for tweet in tweets['tweets']:
        #     date = datetime.strptime(tweet['date'], '%b %d, %Y · %I:%M %p %Z')
        #     data =[tweet['link'], tweet['text'], date, tweet['stats']['likes'], tweet['stats']['comments'], tweet['stats']['retweets']]
        #     final_tweets.append(data)
        # print(final_tweets)

def get_tweets_with_params(query):
    scraper = Nitter()
    tweets = scraper.get_tweets(query, mode="hashtag", number=10)
    final_tweets = []
    for tweet in tweets['tweets']:
        date = datetime.strptime(tweet['date'], '%b %d, %Y · %I:%M %p %Z')
        data =[tweet['link'], tweet['text'], date, tweet['stats']['likes'], tweet['stats']['comments'], tweet['stats']['retweets']]
        final_tweets.append(data)
    return final_tweets



# @shared_task(name='APIBackend.tasks.scrap_data_with_beautifulsoup')
# def scrap_data_with_beautifulsoup(web_url):
#     page_to_scrape = requests.get(web_url)
#     soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
#     # print(soup.prettify())
#     quotes =soup.find_all('span', attrs={'class':'text'})
#     authors =soup.find_all('small', attrs={'class':'author'})
#     tag =soup.find_all('a', attrs={'class':'tag'})
#     file = open('quotes.csv', 'w')
#     writer = csv.writer(file)
#     writer.writerow(['Quote', 'Author', 'Tags'])
#     for i in range(0, len(quotes)):
#         writer.writerow([quotes[i].text, authors[i].text, tag[i].text])
#     file.close()


@shared_task(name='APIBackend.tasks.scrap_data_from_site')
def scrap_data_from_site(web_url):
    page_to_scrape = requests.get(web_url)
    soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
    # Find the 'a' tag with the specified class
    review_links = soup.find_all('a', class_='w-full hover:bg-foreground-50 transition-all rounded-xl p-6 border border-foreground-100')
    reviews = []
    for link in review_links:
        # Find the 'h1' element for the header
        header = link.find('h1', class_='text-lg font-semibold font-heading my-4 inline-block transition-all')
        # Find the 'p' element for the description
        description = link.find('p', class_='whitespace-pre-wrap w-full line-clamp-1')
        
        if header and description:
            reviews.append({
                'header': header.text.strip(),
                'description': description.text.strip()
            })
    
    serialized_data = []
    for review in reviews:
        try:
            my_object = {
                "source": "travel-review-site",
                "source_link": web_url,
                "title": review['header'],
                "description": review['description'],
                "sentiment": None  # Use None instead of null
            }
            review_exits = check_existing_review_by_title_and_description(review['header'], review['description'])
            if review_exits:
                print("Review already exists")
                continue
            serializer = ReviewsSerializer(data=my_object)
            if serializer.is_valid():
                serializer.save()
                serialized_data.append(serializer.data)
            else:
                print("serializer is not valid")
                print(serializer.errors)  # Print serializer errors
        except Exception as e:
            print("error", e)
    

    # return serialized_data
    
@shared_task(name='APIBackend.tasks.scrap_data_from_google_maps')
def scrap_data_from_google_maps():
    
    # api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    # place_id = os.getenv('GOOGLE_MAPS_PLACE_ID')
    
    url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,rating,reviews&key={api_key}'
    # Make a request to the Google Maps API
    response = requests.get(url)
    # response = requests.get("https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJBZrsNtYTLxgRDBcAL1dZN1U&fields=name,rating,reviews&key=AIzaSyBB4OYc8YhncuYC6oXvo_HxTZp6lB7NEt0")
    # Get the JSON data from the response
    data = response.json()
 
    title = data.get('result', {}).get('name', 'No Title')
        
    #  # Extract the reviews
    # reviews_data = data.get('result', {}).get('reviews', [])
    # reviews = [review.get('text', 'No Review') for review in reviews_data]
    # author_url = [review.get('author_url', 'No link') for review in reviews_data]
     # Extract the reviews
    reviews_data = data.get('result', {}).get('reviews', [])
    reviews = [{'text': review.get('text', 'No Review'), 'author_url': review.get('author_url', 'No link')} for review in reviews_data]
        
    
    for review in reviews:
        # print(f'- {review}')
        # # store the result in the database
        try:
            my_object = {
                "source": "google-maps",
                "source_link": review['author_url'],
                "title": review['text'],
                "description": review['text'],
                "sentiment": None  # Use None instead of null
            }
            review_exits = check_existing_review_by_title_and_description(review['text'], review['text'])
            if review_exits:
                print("Review already exists")
                continue
            serializer = ReviewsSerializer(data=my_object)
            if serializer.is_valid():
                print("serializer is valid and saving from google maps")
                serializer.save()
            else:
                print("serializer is not valid")
                print(serializer.errors)  # Print serializer errors
        except Exception as e:
            print("error", e)
    
    
# using textblob to get the sentiment of the review, positive, negative or neutral
@shared_task(name='APIBackend.tasks.get_sentiment')
def get_sentiment():
    reviews = Reviews.objects.all()
    for review in reviews:
        description = review.description
        blob = TextBlob(description)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            print("positive")
            review.sentiment = "positive"
        elif sentiment < 0:
            print("negative")
            review.sentiment = "negative"
        else:
            print("neutral")
            review.sentiment = "neutral"
        review.save()
    return "Sentiment analysis done"