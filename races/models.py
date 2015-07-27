import re
from athletes.models import Athlete
from django.db import models
from meetings.models import Meeting
from races import settings as races_settings


class Race(models.Model):
    type = models.CharField(max_length=2, choices=races_settings.RACES_TYPES.items())
    event = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    round = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    meeting = models.ForeignKey(Meeting)

    def __unicode__(self):
        return unicode(self.pk) + ': ' + unicode(self.event) + u' | ' + unicode(self.type) + u' | ' + unicode(self.category) + u' | ' + unicode(self.round) + u' | ' + unicode(self.meeting)


class Result(models.Model):
    race = models.ForeignKey(Race)
    athlete = models.ForeignKey(Athlete)
    record = models.FloatField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    extra = models.CharField(max_length=3, blank=True)

    def set_record(self, value):
        match = re.compile("^([0-9]+)[,-.]([0-9]+)$").match(value)
        if match:
            groups = match.groups()
            self.record = float(groups[0] + '.' + groups[1])
            return

        match = re.compile("^([0-9]+):([0-9]+)[,-.]([0-9]+)$").match(value)
        if match:
            groups = match.groups()
            self.record = float(groups[0])*60 + float(groups[1] + '.' + groups[2])
            return

        match = re.compile("^([A-Z]+)$").match(value.upper())
        if match:
            self.record = None
            self.extra = value[:3]
            return

    def __unicode__(self):
        return unicode(self.race.event) + u'  ' + unicode(self.race.meeting) + ': ' + unicode(self.position) + u' | ' + unicode(self.athlete) + u' | ' + unicode(self.record)
