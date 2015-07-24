from django.db import models
from masters import settings as masters_settings


class Club(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=2, choices=masters_settings.STATES.items(), blank=True)
    abbreviation = models.CharField(max_length=3, blank=True)

    def __unicode__(self):
        return unicode(self.abbreviation) + u': ' + unicode(self.name)