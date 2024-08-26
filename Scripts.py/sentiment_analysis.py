import requests
from bs4 import BeautifulSoup
import pandas as pd
from transformers import pipeline

# Step 1: Scrape the data
url = "https://www.trustpilot.com/review/www.kenya-airways.com"
data_list = []

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    review_elements = soup.find_all("div", {"class": "styles_cardWrapper__LcCPA"})

    for review_element in review_elements:
        review_dict = {}
        review_dict['review_name'] = review_element.find("span", {"class": "typography_heading-xxs__QKBS8"}).text
        review_dict['review_text'] = review_element.find("h2", {"class": "typography_heading-s__f7029"}).text
        review_dict['review_content'] = review_element.find("p", {"class": "typography_body-l__KUYFJ"}).text
        star_rating = review_element.find("div", {"class": "star-rating_starRating__4rrcf"}).find('img').get('alt')
        review_dict['rating'] = star_rating
        data_list.append(review_dict)
    
    df = pd.DataFrame(data_list)
    df.to_csv('trustpilot_reviews.csv', index=False)
    print(f"Reviews saved successfully to trustpilot_reviews.csv")

    # Step 2: Perform sentiment analysis
    sentiment_pipeline = pipeline('sentiment-analysis')

    def classify_sentiment(text):
        result = sentiment_pipeline(text)[0]
        return result['label'].lower()

    df['sentiment'] = df['review_content'].apply(classify_sentiment)
    df.to_csv('kenya_airways_reviews_with_sentiment_transformers.csv', index=False)
    print("Sentiment analysis complete. Results saved to 'kenya_airways_reviews_with_sentiment_transformers.csv'.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")