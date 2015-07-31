from athletes.models import Athlete
from races.models import Result
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class AthleteSerializer(ModelSerializer):

    class Meta:
        model = Athlete
        fields = ('pk', 'name', 'surname', 'licence', 'birthday', 'nationality', 'region')

