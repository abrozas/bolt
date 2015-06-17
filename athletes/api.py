# -*- coding: utf-8 -*-
from athletes.models import Athlete
from rest_framework.mixins import ListModelMixin


class AthletesViewSet(ListModelMixin):
    queryset = Athlete.objects.all()