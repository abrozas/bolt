# -*- coding: utf-8 -*-
from django.conf import settings

RACES_TYPE = {
	'TT': u'Time Trial',
	'LE': u'Length'
}

RACES_TYPE = getattr(settings, 'RACES_TYPE', RACES_TYPE)