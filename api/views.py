from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics

import api
from .models import KeyGen
from .serializers import KeyGenSerializer
from api import serializers
# Create your views here.


class ListKeyGen(generics.ListCreateAPIView):
    queryset = KeyGen.objects.all()
    serializer_class = KeyGenSerializer
