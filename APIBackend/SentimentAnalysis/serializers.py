from rest_framework import serializers
from SentimentAnalysis.models import Departments, Addition,Reviews


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'
        
        
class UpdateSingleDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields =("DepartmentName",)
        
        
class AdditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addition
        fields = '__all__'
        
class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
        