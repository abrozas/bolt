from django.db import models
from masters import settings as masters_settings


class Club(models.Model):
	name = models.CharField(max_length=255)
	region = models.CharField(max_length=2, choices=masters_settings.STATES)

