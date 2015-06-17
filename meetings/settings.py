# -*- coding: utf-8 -*-
from django.conf import settings

MEETINGS_TYPE = {
    'PC': u'Pista Cubierta',
    'AL': u'Aire Libre',
    'CR': u'Cross',
    'RO': u'Ruta'
}

MEETINGS_TYPE = getattr(settings, 'MEETINGS_TYPE', MEETINGS_TYPE)