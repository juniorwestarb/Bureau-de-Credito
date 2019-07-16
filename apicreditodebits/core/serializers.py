from rest_framework import serializers
from .models import Person, Debt


class DebtsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Debt
        fields = ('id', 'company', 'value', 'created_at', 'person')


class PersonSerializer(serializers.ModelSerializer):
    debits = DebtsSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ('id', 'cpf', 'name', 'address', 'debits')
