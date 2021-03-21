from django.db import models


# Create your models here. db executions here
# Define template of the created migration
class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083) # Max for URLS

class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.TextField()
    discount = models.FloatField()

