# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
        ('trainers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('birthday', models.DateField(blank=True)),
                ('nationality', models.CharField(max_length=3, blank=True)),
                ('region', models.CharField(default='Other', max_length=2, blank=True, choices=[(b'02', 'Arag\xf3n'), (b'03', 'Asturias, Principado de'), (b'13', 'Madrid, Comunidad de'), (b'01', 'Andaluc\xeda'), (b'06', 'Cantabria'), (b'07', 'Castilla y Le\xf3n'), (b'04', 'Balears, Illes'), (b'05', 'Canarias'), (b'19', 'Melilla'), (b'18', 'Ceuta'), (b'08', 'Castilla - La Mancha'), (b'09', 'Catalu\xf1a'), (b'20', 'Other'), (b'16', 'Pa\xeds Vasco'), (b'12', 'Galicia'), (b'17', 'Rioja, La'), (b'14', 'Murcia, Regi\xf3n de'), (b'11', 'Extremadura'), (b'15', 'Navarra, Comunidad Foral de'), (b'10', 'Comunitat Valenciana')])),
                ('licence', models.CharField(max_length=10, blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_mod_date', models.DateTimeField(auto_now=True)),
                ('slug', models.CharField(default=models.CharField(max_length=255), unique=True, max_length=255)),
                ('trainer', models.ForeignKey(to='trainers.Trainer', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClubForAthlete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('season', models.CharField(max_length=4)),
                ('athlete', models.ForeignKey(to='athletes.Athlete')),
                ('club', models.ForeignKey(to='clubs.Club')),
            ],
        ),
    ]
