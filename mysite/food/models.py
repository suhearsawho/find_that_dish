from django.db import models

# Create your models here.

class FoodQuery(models.Model):
    """Defines the FoodQuery class"""
    image_path = models.CharField(max_length=400)
    location = models.CharField(max_length=100)
