# -*- coding: utf-8 -*-
from athletes.models import Athlete
from athletes.serializers import AthleteSerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet


class AthletesViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    paginate_by = 20
