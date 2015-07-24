# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0002_auto_20150724_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='region',
            field=models.CharField(default=20, max_length=2, blank=True, choices=[(b'02', 'Arag\xf3n'), (b'03', 'Asturias, Principado de'), (b'13', 'Madrid, Comunidad de'), (b'01', 'Andaluc\xeda'), (b'06', 'Cantabria'), (b'07', 'Castilla y Le\xf3n'), (b'04', 'Balears, Illes'), (b'05', 'Canarias'), (b'19', 'Melilla'), (b'18', 'Ceuta'), (b'08', 'Castilla - La Mancha'), (b'09', 'Catalu\xf1a'), (b'20', 'Other'), (b'16', 'Pa\xeds Vasco'), (b'12', 'Galicia'), (b'17', 'Rioja, La'), (b'14', 'Murcia, Regi\xf3n de'), (b'11', 'Extremadura'), (b'15', 'Navarra, Comunidad Foral de'), (b'10', 'Comunitat Valenciana')]),
        ),
    ]
