# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='birthday',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='trainer',
            field=models.ForeignKey(blank=True, to='trainers.Trainer', null=True),
        ),
    ]
