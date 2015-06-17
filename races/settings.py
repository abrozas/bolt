# -*- coding: utf-8 -*-
from django.conf import settings

RACES_TYPES = {
    'TT': u'Time Trial',
    'LE': u'Length'
}

RACES_TYPES = getattr(settings, 'RACES_TYPE', RACES_TYPES)