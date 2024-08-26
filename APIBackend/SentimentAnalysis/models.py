from django.db import models
# Create your models here.

class Departments(models.Model):
        DepartmentId = models.AutoField(primary_key=True)
        DepartmentName = models.CharField(max_length=100)
        # first_name=models.CharField(max_length=100)
        

        

class Addition(models.Model):
        id = models.AutoField(primary_key=True)
        num_1 = models.IntegerField()
        num_2 = models.IntegerField()
        result = models.IntegerField()
        # date = models.DateField()
        
class Reviews(models.Model):
        id = models.AutoField(primary_key=True)
        source = models.CharField(max_length=100)
        source_link = models.TextField(max_length=100, null=True)
        title = models.TextField(null=True)
        description = models.TextField()
        # sentiment can be positive, negative or neutral
        sentiment = models.CharField(max_length=100, null=True)
        created_at = models.DateTimeField(auto_now_add=True)
        