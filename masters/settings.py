# -*- coding: utf-8 -*-
from django.conf import settings

STATES = {
	'01': u'Andalucía',
	'02': u'Aragón',
	'03': u'Asturias, Principado de',
	'04': u'Balears, Illes',
	'05': u'Canarias',
	'06': u'Cantabria',
	'07': u'Castilla y León',
	'08': u'Castilla - La Mancha',
	'09': u'Cataluña',
	'10': u'Comunitat Valenciana',
	'11': u'Extremadura',
	'12': u'Galicia',
	'13': u'Madrid, Comunidad de',
	'14': u'Murcia, Región de',
	'15': u'Navarra, Comunidad Foral de',
	'16': u'País Vasco',
	'17': u'Rioja, La',
	'18': u'Ceuta',
	'19': u'Melilla'
}

STATES = getattr(settings, 'STATES', STATES)