from django.db import models

# Create your models here.

class Stock(models.Model):
    symbol = models.CharField(max_length = 50, null=False)
    company = models.CharField(max_length = 200, null=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
