import pandas as pd
import os


def save_reviews(df, filename='./Data/kenya_airways_reviews.csv'):
    if not df.empty:
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("No reviews found to save.")

def load_reviews(filename='./Data/kenya_airways_reviews.csv'):
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        print(f"No file found at {filename}. Returning an empty DataFrame.")
        return pd.DataFrame()
