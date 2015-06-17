from django.db import models
from meetings import settings as meetings_settings


class Meeting(models.Model):
    name = models.CharField(max_length=255)
    sort_name = models.CharField(max_length=255)
    date = models.DateField()
    season = models.CharField(max_length=4)
    city = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=meetings_settings.MEETINGS_TYPE.items())
