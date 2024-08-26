from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer

from django.http import JsonResponse
from reviews.models import Review
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

from django.shortcuts import render
from .models import Review

def review_list(request):
    reviews = list(Review.objects.values('review_name', 'review_content', 'sentiment'))
    return JsonResponse(reviews, safe=False)

def dashboard(request):
    return render(request, 'reviews/index.html')


class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



def scrape_and_analyze(request):
    url = "https://www.trustpilot.com/review/www.kenya-airways.com"
    response = requests.get(url)
    sentiment_pipeline = pipeline('sentiment-analysis')

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        review_elements = soup.find_all("div", {"class": "styles_cardWrapper__LcCPA"})

        for element in review_elements:
            name = element.find("span", {"class": "typography_heading-xxs__QKBS8"}).text
            heading = element.find("h2", {"class": "typography_heading-s__f7029"}).text
            content = element.find("p", {"class": "typography_body-l__KUYFJ"}).text
            star_rating = element.find("div", {"class": "star-rating_starRating__4rrcf"}).find('img').get('alt')
            sentiment = sentiment_pipeline(content)[0]['label'].lower()

            Review.objects.create(
                review_name=name,
                review_text = heading,
                review_content=content,
                rating=star_rating,
                sentiment=sentiment
            )

        return JsonResponse({'status': 'success', 'message': 'Reviews scraped and analyzed successfully'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Failed to retrieve the page'})