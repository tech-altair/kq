from urllib.request import urlopen
import spacy
import pathlib
from bs4 import BeautifulSoup
import pandas as pd

nlp = spacy.load("en_core_web_sm")
url = "https://theprivatetraveller.com/flight-reviews/kenya-airways"
page = urlopen(url)
page
html_bytes = page.read()
#html = html_bytes.decode("utf-8")

#print(html)
#type (review_doc)

#sentences = list(review_doc.sents)
#len(sentences)

soup = BeautifulSoup(html_bytes, "html.parser")
text = soup.get_text()

review_doc = nlp(text)
sentences = [sent.text for sent in review_doc.sents]

#nouns = []
#verbs = []
#adjectives = []
#adverbs = []
sorted = []
for token in review_doc:
#    if token.pos_ == "NOUN":
#        sorted.append(token)
    if token.pos_ == "ADJ":
        sorted.append(token)
    if token.pos_ == "ADV":
        sorted.append(token)
#    if token.pos_ == "VERB":
#        sorted.append(token)



#data_frame.to_csv('sorted_data.csv')

#print( adjectives , adverbs )
#adjectives
#for sentence in sentences:
#    print (f"{sentence[:25]}...")
 #   print (sorted)
