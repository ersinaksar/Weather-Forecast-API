# weather_api/tomorrow/models.py

from django.db import models


class Tomorrow(models.Model):
    # Define needed values here
    date = models.DateField()
    warm = models.BooleanField()
    sunny = models.BooleanField()
    windy = models.BooleanField()
