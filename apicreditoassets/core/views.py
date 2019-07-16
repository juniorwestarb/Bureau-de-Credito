from django.shortcuts import render
from .models import Consumer, Asset
from .serializers import ConsumerSerializer, AssetsSerializer
from rest_framework import viewsets


class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer


class AssetsViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetsSerializer
