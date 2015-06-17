# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('sort_name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('season', models.CharField(max_length=4)),
                ('city', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=2, choices=[(b'PC', 'Pista Cubierta'), (b'RO', 'Ruta'), (b'AL', 'Aire Libre'), (b'CR', 'Cross')])),
            ],
        ),
    ]
