from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import models

# Create your views here.

from rest_framework import serializers

class HelloWorldProcessSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.HelloWorldProcess
        fields = "__all__"


class HelloWorldViewSet(ModelViewSet):
    queryset = models.HelloWorldProcess.objects.all()
    serializer_class = HelloWorldProcessSerializer
