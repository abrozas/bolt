# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0003_auto_20150724_0840'),
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=2, choices=[(b'TT', 'Time Trial'), (b'LE', 'Length')])),
                ('event', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('round', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('meeting', models.ForeignKey(to='meetings.Meeting')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('record', models.FloatField(null=True, blank=True)),
                ('position', models.IntegerField(null=True, blank=True)),
                ('extra', models.CharField(max_length=2, blank=True)),
                ('athlete', models.ForeignKey(to='athletes.Athlete')),
                ('race', models.ForeignKey(to='races.Race')),
            ],
        ),
    ]
