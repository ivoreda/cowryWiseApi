from rest_framework import serializers
from .models import KeyGen


class KeyGenSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyGen
        fields = ('id', 'dateTime')
