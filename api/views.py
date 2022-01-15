from django.shortcuts import render

from rest_framework import generics
from .models import KeyGen
from .serializers import KeyGenSerializer
# Create your views here.


class ListKeyGen(generics.ListCreateAPIView):
    queryset = KeyGen.objects.all()
    serializer_class = KeyGenSerializer
