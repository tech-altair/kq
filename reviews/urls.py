from django.urls import path
from .views import ReviewListCreate, scrape_and_analyze

urlpatterns = [
    path('reviews/', ReviewListCreate.as_view(), name='review-list-create'),
    path('scrape/', scrape_and_analyze, name='scrape-and-analyze'),
]