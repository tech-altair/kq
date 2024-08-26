from django.db import models

class Review(models.Model):
    review_name = models.CharField(max_length=255)
    review_text = models.TextField()
    review_content = models.TextField()
    rating = models.CharField(max_length=10)
    sentiment = models.CharField(max_length=10)

    def __str__(self):
        return self.review_name
