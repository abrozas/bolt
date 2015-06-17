from athletes.models import Athlete
from django.db import models
from meetings.models import Meeting
from races import settings as races_settings


class Race(models.Model):
    type = models.CharField(max_length=2, choices=races_settings.RACES_TYPES.items())
    category = models.CharField(max_length=50)
    round = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    meeting = models.ForeignKey(Meeting)


class Result(models.Model):
    race = models.ForeignKey(Race)
    athlete = models.ForeignKey(Athlete)
    record = models.FloatField(blank=True)
    position = models.IntegerField(blank=True)
    extra = models.CharField(max_length=2, blank=True)