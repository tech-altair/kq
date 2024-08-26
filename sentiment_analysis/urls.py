from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reviews import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reviews.urls')),
    path('dashboard/', views.dashboard),
    path('review-list/', views.review_list, name='review-list')
]
