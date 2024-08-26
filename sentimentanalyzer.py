import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import nltk
import webscrap


#nltk.download('all')
sorted = webscrap.sorted
df = pd.DataFrame(data=sorted)#create a data frame object to save the data in a csv format to make it readable by pandas
df.to_csv('sorted_data.csv')
df= pd.read_csv('sorted_data.csv')#load dataset

def preprocess_text(text):
    tokens = word_tokenize(text.lower())#normalize text to make it consistent
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]#remove stop words- unnecessary tokens

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    processed_text = ' '.join(lemmatized_tokens)

    return processed_text

df.loc[:,'reviewText'] = df['text'].apply(preprocess_text)
df