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
