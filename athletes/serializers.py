from athletes.models import Athlete
from rest_framework.serializers import ModelSerializer


class AthleteSerializer(ModelSerializer):
    class Meta:
        model = Athlete
