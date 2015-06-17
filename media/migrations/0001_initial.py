# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('uri', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_mod_date', models.DateTimeField(auto_now=True)),
                ('uploader', models.CharField(max_length=255, null=True, blank=True)),
                ('type', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='MediaAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.CharField(max_length=100)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('media', models.ForeignKey(to='media.Media')),
            ],
        ),
    ]
