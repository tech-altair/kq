import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re

def preprocess_reviews(reviews):
    lemma = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))

    def clean_text(text):
        text = re.sub('[^a-zA-Z]', ' ', text)
        words = text.lower().split()
        return " ".join(lemma.lemmatize(word) for word in words if word not in stop_words)

    df = pd.DataFrame(reviews, columns=['review_text', 'date'])
    df['cleaned_reviews'] = df['review_text'].apply(clean_text)
    
    # Add the word_count column
    df['word_count'] = df['cleaned_reviews'].apply(lambda x: len(x.split()))
    # Creates a new column that extracts the information on whether the trip is verified or not
    df['verified'] = df['review_text'].str.contains("Trip Verified", case=False, regex=False)

    return df

def analyze_sentiment_vader(df):
    vds = SentimentIntensityAnalyzer()

    def get_sentiment_label(text):
        score = vds.polarity_scores(text)['compound']
        if score > 0.2:
            return 1  # Positive
        elif score < 0:
            return -1  # Negative
        else:
            return 0  # Neutral
    
    df['sentiment'] = df['cleaned_reviews'].apply(get_sentiment_label)

    df['label'] = df['cleaned_reviews'].apply(get_sentiment_label)
    return df
