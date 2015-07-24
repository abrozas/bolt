from django.contrib import admin

# Register your models here.
from media.models import Media, MediaAttachment

admin.site.register(Media)
admin.site.register(MediaAttachment)
