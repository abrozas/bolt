from races.models import Result
from rest_framework.serializers import ModelSerializer


class ResultSerializer(ModelSerializer):

    class Meta:
        model = Result
        fields = ('race', 'record', 'position', 'extra')

