# -*- coding: utf-8 -*-
from athletes.models import Athlete
import django_filters


class AthleteFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name="name", lookup_type='icontains')
    surname = django_filters.CharFilter(name="surname", lookup_type='icontains')
    #total_min = django_filters.NumberFilter(name="total", lookup_type='gte')
    #total_max = django_filters.NumberFilter(name="total", lookup_type='lte')
    #invoice_id = django_filters.CharFilter(name="idn", lookup_type='startswith')
    #contract_id = django_filters.CharFilter(name="contract__id", lookup_type='startswith')
    #state = django_filters.CharFilter(name="customer_state")
    #agreement = django_filters.MethodFilter(action='agreement_filter')
    #from_date = django_filters.DateFilter(name="creation_date", lookup_type='gte')
    #to_date = django_filters.DateFilter(name="creation_date", lookup_type='lte')
    #vat_id = django_filters.CharFilter(name="customer_vat_id", lookup_type='icontains')
    #cups = django_filters.CharFilter(name="cups", lookup_type='icontains')

    class Meta:
        model = Athlete
        fields = ['name', 'surname', 'birthday', 'nationality', 'region', 'slug']

    #def agreement_filter(self, queryset, value):
    #    contracts = ContractForAgreement.objects.filter(agreement_id=value).values_list('contract', flat=True)
    #    return queryset.filter(contract__in=contracts)
