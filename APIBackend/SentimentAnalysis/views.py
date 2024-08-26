from django.shortcuts import render
from  django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from SentimentAnalysis.models import Departments,Reviews
from SentimentAnalysis.serializers import DepartmentSerializer,ReviewsSerializer
from django.views.decorators.http import require_http_methods
# Create your views here.
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    GenericAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework import response, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .helpers import check_existing_department_name,check_existing_review_by_title_and_description
from APIBackend.tasks import run_all_tasks

class NyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class TestRoute(GenericAPIView):
    def get(self, request):
        numbers = run_all_tasks.delay()
        
        return response.Response({"message": "All tasks are running", "task_id": numbers.task_id}, status=status.HTTP_200_OK)
  
        
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
class GetReview(GenericAPIView):
    serializer_class = ReviewsSerializer
    def get(self, review_id):
        try:
            review = Reviews.objects.get(id=review_id)
            review_serializer = self.serializer_class(review)
            return response.Response(review_serializer.data, status=status.HTTP_200_OK)
        except Reviews.DoesNotExist:
            return response.Response({"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetAllReviews(ListAPIView):
    serializer_class = ReviewsSerializer
    pagination_class = NyPagination
    # queryset = Reviews.objects.all()
    def get(self, request):
        reviews = Reviews.objects.all()
        review_serializer = self.serializer_class(reviews, many=True)
        return response.Response(review_serializer.data, status=status.HTTP_200_OK)
#getting review where sentiment is positive
class GetPositiveReviewSentiment(GenericAPIView):
    serializer_class = ReviewsSerializer
    def get(self, request):
        reviews = Reviews.objects.filter(sentiment='positive')
        review_serializer = self.serializer_class(reviews, many=True)
        return response.Response(review_serializer.data, status=status.HTTP_200_OK)

#getting all reviews where sentiment is negative
class GetNegativeReviewSentiment(GenericAPIView):
    serializer_class = ReviewsSerializer
    def get(self, request):
        reviews = Reviews.objects.filter(sentiment='negative')
        review_serializer = self.serializer_class(reviews, many=True)
        return response.Response(review_serializer.data, status=status.HTTP_200_OK)
    
#getting all reviews where sentiment is neutral
class GetNeutralReviewSentiment(GenericAPIView):
    serializer_class = ReviewsSerializer
    def get(self, request):
        reviews = Reviews.objects.filter(sentiment='neutral')
        review_serializer = self.serializer_class(reviews, many=True)
        return response.Response(review_serializer.data, status=status.HTTP_200_OK)
    
class CreateReview(CreateAPIView):
    serializer_class = ReviewsSerializer
    def post(self, request):
        review_data = request.data
        review_exits = check_existing_review_by_title_and_description(review_data.get('title'), review_data.get('description'))
        if review_exits:
            return response.Response({"error": "Review already exists"}, status=status.HTTP_409_CONFLICT)
        review_serializer = self.serializer_class(data=review_data)
        if review_serializer.is_valid():
            review_serializer.save()
            return response.Response(review_serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UpdateReview(UpdateAPIView):
    serializer_class = ReviewsSerializer
    def put(self, request, review_id):
        review_data = request.data
        try:
            review = Reviews.objects.get(id=review_id)
            serializer = self.serializer_class(review, data=review_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_200_OK)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Reviews.DoesNotExist:
            return response.Response({"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeleteReview(DestroyAPIView):
    def delete(self, request, review_id):
        try:
            review = Reviews.objects.get(id=review_id)
            review.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except Reviews.DoesNotExist:
            return JsonResponse({"error": "Review not found"}, status=404)
        except Exception as e:
            return response.Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class DeleteAllReviews(DestroyAPIView):
    def delete(self, request):
        try:
            Reviews.objects.all().delete()
            return response.Response({"message": "All reviews deleted successfully"}, status=status.HTTP_200_OK)
        except Reviews.DoesNotExist:
            return response.Response({"error": "No reviews found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response.Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
    