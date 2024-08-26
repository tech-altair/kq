import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.tripadvisor.com/Hotel_Review-g294207-d302925-Reviews-Kenya_Airways-Nairobi.html'
headers = {'User-Agent': 'Mozilla/5.0'}

def scrape_tripadvisor():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    reviews = soup.find_all('q', {'class': 'IRsGHoPm'})
    reviews_text = [review.get_text() for review in reviews]

    # Save reviews to a CSV file 
    with open('kenya_airways_tripadvisor_reviews.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Review'])
        for review_text in reviews_text:
            writer.writerow([review_text])

    print("Reviews scraped and saved successfully.")
    return reviews_text  

if __name__ == "__main__":
    scrape_tripadvisor()  
