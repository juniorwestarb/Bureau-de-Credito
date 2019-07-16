from rest_framework import serializers
from .models import Consumer, Asset


class AssetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset
        fields = ('id', 'description', 'value', 'consumer')


class ConsumerSerializer(serializers.ModelSerializer):
    assets = AssetsSerializer(many=True, read_only=True)

    class Meta:
        model = Consumer
        fields = ('id', 'cpf', 'age', 'address', 'economic_income', 'assets')
