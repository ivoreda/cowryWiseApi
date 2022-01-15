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

    # some = KeyGenSerializer.fields.data()
    # print(some)

    # def post(request):
    #     serializer = KeyGenSerializer(request.data, many=True)
    #     dict(dateTime=serializer.data.timestamp, idKey=serializer.data.uuid)
    #     return Response


@api_view(["GET"])
def ivor(request):
    context = {}
    item = KeyGen.objects.all()
    serializer = KeyGenSerializer(item, many=True)
    for serializers in serializer:
        context[serializers.data.dateTime] = serializers.data.idKey
    print(serializer)
    return Response(context)
