from django.urls import path
from SentimentAnalysis import views

urlpatterns = [
    # path('department', views.GetAllDepartments.as_view(), name='get-all-department'),
    # path('department/<int:department_id>', views.GetDepartment.as_view(), name='get-single-department'),
    # path('department/add', views.CreateDepartment.as_view(), name='create-department'),
    # path('department/update/<int:department_id>', views.UpdateDepartment.as_view(), name='update-department'),
    # path('department/delete/<int:department_id>', views.DeleteDepartment.as_view(), name='delete-department'),
    
    # reviews all paths 
    path('test', views.TestRoute.as_view(), name='test-routes'),
    path('reviews', views.GetAllReviews.as_view(), name='get-all-reviews'),
    path('reviews/positive', views.GetPositiveReviewSentiment.as_view(), name='get-positive-review-sentiment'),
    path('reviews/negative', views.GetNegativeReviewSentiment.as_view(), name='get-negative-review-sentiment'),
    path('reviews/neutral', views.GetNeutralReviewSentiment.as_view(), name='get-neutral-review-sentiment'),
    
    path('reviews/<int:review_id>', views.GetReview.as_view(), name='get-single-review'),
    path('reviews/add', views.CreateReview.as_view(), name='create-review'),
    path('reviews/update/<int:review_id>', views.UpdateReview.as_view(), name='update-review'),
    path('reviews/delete/<int:review_id>', views.DeleteReview.as_view(), name='delete-review'),
    path('reviews/destroy', views.DeleteAllReviews.as_view(), name='delete-all-reviews'),
    # path('reviews/sentiment', views.GetReviewSentiment.as_view(), name='get-review-sentiment'),
    
]

