import requests
from bs4 import BeautifulSoup
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Function to scrape data from Trustpilot
def scrape_reviews(url):
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
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
    return data_list

# Function to perform sentiment analysis
def analyze_sentiments(reviews):
    analyzer = SentimentIntensityAnalyzer()
    for review in reviews:
        sentiment_score = analyzer.polarity_scores(review['review_content'])['compound']
        if sentiment_score >= 0.05:
            review['sentiment'] = 'positive'
        elif sentiment_score <= -0.05:
            review['sentiment'] = 'negative'
        else:
            review['sentiment'] = 'neutral'
    return reviews

# Function to save the data to a CSV file
def save_to_csv(reviews, filename):
    df = pd.DataFrame(reviews)
    df.to_csv(filename, index=False)
    print(f"Reviews with sentiment analysis saved successfully to {filename}")

# Main function to run the pipeline
def main():
    url = "https://www.trustpilot.com/review/www.kenya-airways.com"
    reviews = scrape_reviews(url)
    reviews_with_sentiments = analyze_sentiments(reviews)
    save_to_csv(reviews_with_sentiments, 'trustpilot_reviews_with_sentiments.csv')

if __name__ == "__main__":
    main()