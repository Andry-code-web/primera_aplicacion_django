from django.db import models

# Create your models here.

class Review(models.Model):
    review = models.TextField(max_length=4000)
    