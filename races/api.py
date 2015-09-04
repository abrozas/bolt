# -*- coding: utf-8 -*-
from athletes.filters import AthleteFilter
from athletes.models import Athlete
from athletes.serializers import AthleteSerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet


class AthletesViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    filter_class = AthleteFilter
    paginate_by = 20

    search_fields = ('name', 'surname', 'licence')