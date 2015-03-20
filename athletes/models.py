from clubs.models import Club
from masters import settings as masters_settings
from django.db import models
from trainers.models import Trainer


class Athlete(models.Model):
	name = models.CharField(max_length=255)
	surname = models.CharField(max_length=255)
	birthday = models.DateField(blank=True)
	nationality = models.CharField(max_length=3)
	region = models.CharField(max_length=2, choices=masters_settings.STATES)
	licence = models.CharField(max_length=10, blank=True)
	trainer = models.CharField(Trainer, blank=True)
	creation_date = models.DateTimeField(auto_now_add=True)
	last_mod_date = models.DateTimeField(auto_now=True, auto_now_add=True)


class ClubForAthlete(models.Model):
	athlete = models.ForeignKey(Athlete)
	club = models.ForeignKey(Club)
	season = models.CharField(max_length=4)