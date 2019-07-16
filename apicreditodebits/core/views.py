from django.shortcuts import render
from .models import Person, Debt
from .serializers import PersonSerializer, DebtsSerializer
from rest_framework import viewsets


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class DebtsViewSet(viewsets.ModelViewSet):
    queryset = Debt.objects.all()
    serializer_class = DebtsSerializer
