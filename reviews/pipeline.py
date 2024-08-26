import requests
from bs4 import BeautifulSoup
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from django.db.models import Q
from .models import Review

def scrape_and_save_reviews(url):
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
        
        # Save the data to the database
        for review in data_list:
            Review.objects.update_or_create(
                review_name=review['review_name'],
                defaults={'review_text': review['review_text'], 'review_content': review['review_content'], 'rating': review['rating']}
            )
        
        # Perform sentiment analysis and save it
        analyzer = SentimentIntensityAnalyzer()
        for review in data_list:
            sentiment_score = analyzer.polarity_scores(review['review_content'])['compound']
            if sentiment_score >= 0.05:
                review['sentiment'] = 'positive'
            elif sentiment_score <= -0.05:
                review['sentiment'] = 'negative'
            else:
                review['sentiment'] = 'neutral'
            
            # Update the database with sentiment information
            Review.objects.filter(review_name=review['review_name']).update(sentiment=review['sentiment'])
        
        return data_list
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
    return []

# Main function to run the pipeline
def main():
    url = "https://www.trustpilot.com/review/www.kenya-airways.com"
    reviews = scrape_and_save_reviews(url)
    print(f"Successfully scraped and saved {len(reviews)} reviews.")

if __name__ == "__main__":
    main()
