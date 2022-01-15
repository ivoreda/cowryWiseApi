from dataclasses import field
from datetime import datetime
from uuid import uuid4
from rest_framework import serializers
from .models import KeyGen


class KeyGenSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyGen
        fields = ('dateTime', 'idKey')

    def to_representation(self, instance):
        res = super(KeyGenSerializer, self).to_representation(instance)
        return {res['dateTime']: res['idKey']}
        # or you can fetch the id by data directly
        #   return {str(data.id): res}

    def create(self, validated_data):
        key_gen = KeyGen.objects.create(dateTime=datetime.now)
        return key_gen


class MySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    field1 = serializers.ReadOnlyField()
    field2 = serializers.ReadOnlyField()

    def to_representation(self, data):
        res = super(MySerializer, self).to_representation(data)
        return {res['id']: res}
        # or you can fetch the id by data directly
        # return {str(data.id): res}
