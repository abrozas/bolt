from clubs.models import Club
from masters import settings as masters_settings
from django.db import models
from trainers.models import Trainer


class Athlete(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=3, blank=True)
    region = models.CharField(max_length=2, choices=masters_settings.STATES.items(), default=20, blank=True)
    licence = models.CharField(max_length=10, blank=True)
    trainer = models.ForeignKey(Trainer, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_mod_date = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=255, unique=True, default=name)

    def __unicode__(self):
        return unicode(self.name) + u' ' + unicode(self.surname)

class ClubForAthlete(models.Model):
    athlete = models.ForeignKey(Athlete)
    club = models.ForeignKey(Club)
    season = models.CharField(max_length=4)

    def __unicode__(self):
        return unicode(self.athlete) + u' - ' + unicode(self.club)