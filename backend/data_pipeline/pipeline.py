from data_ingestion.scrape_x import scrape_tweets
from data_ingestion.scrape_ta import scrape_tripadvisor
from data_processing.text import preprocess_text
from data_processing.sentiment import analyze_sentiment
from data_storage.store_postgres import store_processed_data_in_postgresql
from data_storage.store_mongodb import store_raw_data_in_mongodb
# from data_storage.store_s3 import store_in_data_lake

def execute_pipeline():
    # scrape data
    tweets_data = scrape_tweets()
    tripadvisor_data = scrape_tripadvisor()

    # store raw data
    store_raw_data_in_mongodb(tweets_data)
    store_raw_data_in_mongodb(tripadvisor_data)

    # analyze sentiment
    for data in tweets_data:
        data['sentiment'] = analyze_sentiment(data['text'])

    for data in tripadvisor_data:
        data['sentiment'] = analyze_sentiment(data['text'])

    # store processed data
    store_processed_data_in_postgresql(tweets_data)
    store_processed_data_in_postgresql(tripadvisor_data)

    # store in data lake
    # store_in_data_lake('my-data-lake', 'tweets_data.json', tweets_data)
    # store_in_data_lake('my-data-lake', 'tripadvisor_data.json', tripadvisor_data)

if __name__ == "__main__":
    execute_pipeline()
