from athletes.models import Athlete
from bolt.settings import BASE_DIR
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Media(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    uri = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_mod_date = models.DateTimeField(auto_now=True)
    uploader = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=4)

    def get_url(self):
        if self.uri.startswith('http'):
            return self.uri
        else:
            return BASE_DIR + self.uri

    def __unicode__(self):
        return unicode(self.name) + u' # ' + unicode(self.uri)


class MediaAttachment(models.Model):
    media = models.ForeignKey(Media)
    content_type = models.ForeignKey(ContentType)
    object_id = models.CharField(max_length=100)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return _(u'Athlete: %(athlete)s - Media: %(media)s') % {'athlete': self.athlete, 'media': self.media }