from .models import Fund
from rest_framework import serializers


class FundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fund
        fields = '__all__'