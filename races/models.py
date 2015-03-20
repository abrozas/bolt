from athletes.models import Athlete
from django.db import models
from meetings.models import Meeting
from races import settings as races_settings


class Race(models.Model):
	type = models.CharField(max_length=2, choices=races_settings.RACE_TYPES)
	category = models.CharField(max_length=50)
	round = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	meeting = models.ForeignKey(Meeting)


class Results(models.Model):
	race = models.ForeignKey(Race)
	athlete = models.ForeignKey(Athlete)
	record = models.FloatField()
	position = models.IntegerField()