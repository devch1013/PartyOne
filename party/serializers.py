from rest_framework.serializers import ModelSerializer, Serializer, ReadOnlyField
from .models import Party
import random
import string
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from main.open_api.responses import *


class PartyCreateSerializer(ModelSerializer):
    thumbnail = serializers.ImageField(required=False)

    class Meta:
        model = Party
        fields = (
            "name",
            "description",
            "location",
            "start_date",
            "end_date",
            "max_attendees",
            "thumbnail",
            "latitude",
            "longitude",
        )

    def create(self, validated_data):
        del validated_data["thumbnail"]
        party = Party.objects.create(col=generate_col(10), **validated_data)
        return party


class PartyListSerializer(ModelSerializer):
    host_name = ReadOnlyField(source="host.username")

    class Meta:
        model = Party
        fields = (
            "col",
            "name",
            "start_date",
            "location",
            "host_name",
        )


class PartyObjectSerializer(ModelSerializer):
    class Meta:
        model = Party
        fields = (
            "col",
            "name",
            "description",
            "start_date",
            "uuid",
        )


class ResponseSerializer(Serializer):
    message = ReadOnlyField()
    status = ReadOnlyField()
    data = ReadOnlyField()

    class Meta:
        fields = ("message", "status", "data")


def generate_col(n: int):
    rand_str = ""
    for _ in range(n):
        rand_str += str(random.choice(string.ascii_letters + string.digits))

    return rand_str
