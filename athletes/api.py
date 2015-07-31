# -*- coding: utf-8 -*-
from athletes.filters import AthleteFilter
from athletes.models import Athlete
from athletes.serializers import AthleteSerializer
from races.models import Result
from races.serializers import ResultSerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet


class AthletesViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    filter_class = AthleteFilter
    paginate_by = 20

    search_fields = ('name', 'surname', 'licence')


class AthletesResultsViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def list(self, request, object_pk):
        athlete = Athlete.objects.get(pk=object_pk)

        self.queryset = self.queryset.filter(athlete=athlete)

        return super(AthletesResultsViewSet, self).list(request, object_pk)
