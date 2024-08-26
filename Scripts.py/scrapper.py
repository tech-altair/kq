import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the Trustpilot page with reviews
url = "https://www.trustpilot.com/review/www.kenya-airways.com"

# Initialize empty lists to store data
data_list = []

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the review elements on the page (you may need to inspect the HTML structure to get the right selector)
    review_elements = soup.find_all("div", {"class": "styles_cardWrapper__LcCPA"})

    # Loop through the review elements and extract the text of each review
    for review_element in review_elements:
        review_dict = {}
        
        # Extract review name
        review_dict['review_name'] = review_element.find("span", {"class": "typography_heading-xxs__QKBS8"}).text
        
        # Extract review text
        review_dict['review_text'] = review_element.find("h2", {"class": "typography_heading-s__f7029"}).text

        # Extract review content
        review_dict['review_content'] = review_element.find("p", {"class": "typography_body-l__KUYFJ"}).text
        
        # Extract rating
        star_rating = review_element.find("div", {"class": "star-rating_starRating__4rrcf"}).find('img').get('alt')
        review_dict['rating'] = star_rating
        
        # Add the dictionary to our list
        data_list.append(review_dict)
    
    # Create a DataFrame from our list of dictionaries
    df = pd.DataFrame(data_list)
    
    # Save the DataFrame to a CSV file
    df.to_csv('trustpilot_reviews.csv', index=False)
    
    print(f"Reviews saved successfully to trustpilot_reviews.csv")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")