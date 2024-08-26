import sys
import os
import pickle
import contextlib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from scraper import scrape_reviews
from processor import preprocess_reviews, analyze_sentiment_vader
from storage import save_reviews
from visualization import generate_visualizations

def train_and_evaluate_model(df):
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(df['cleaned_reviews'], df['sentiment'], test_size=0.2, random_state=42)

    # Feature extraction using CountVectorizer
    vectorizer = CountVectorizer(max_features=5000)
    X_train_vect = vectorizer.fit_transform(X_train)
    X_test_vect = vectorizer.transform(X_test)

    # Logistic Regression model
    model = LogisticRegression(max_iter=200)
    model.fit(X_train_vect, y_train)

    # Predictions and evaluation
    y_pred = model.predict(X_test_vect)

    # Write the results to a file
    with open('model_results.txt', 'w') as file:
        with contextlib.redirect_stdout(file):
            accuracy = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred, zero_division=0)  # Set zero_division to handle undefined metrics
            print(f'Accuracy: {accuracy:.2f}')
            print(report)

    # Save the model and vectorizer
    with open('sentiment_model.pkl', 'wb') as file:
        pickle.dump(model, file)

    with open('vectorizer.pkl', 'wb') as file:
        pickle.dump(vectorizer, file)

    # Generate visualizations including confusion matrix
    generate_visualizations(df, y_test=y_test, y_pred=y_pred, model=model)

    # Return accuracy and report for dashboard display
    return accuracy, report

def run_pipeline():
    # Scrape reviews
    reviews = scrape_reviews()

    # Process and analyze sentiment
    if reviews:
        df = preprocess_reviews(reviews)
        #df = analyze_sentiment(df)
        df = analyze_sentiment_vader(df)  # Perform VADER sentiment analysis

        # Store the results
        save_reviews(df)

        # Train and evaluate the model, save the results
        accuracy, report = train_and_evaluate_model(df)

        return accuracy, report
    else:
        print("No reviews scraped.")
        return None, None

if __name__ == "__main__":
    run_pipeline()
