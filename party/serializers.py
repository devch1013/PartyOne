from rest_framework.serializers import ModelSerializer, Serializer, ReadOnlyField
from .models import Party
import random
import string


class PartyCreateSerializer(ModelSerializer):
    class Meta:
        model = Party
        fields = (
            "name",
            "description",
            "location",
            "date",
            "max_attendees",
        )

    def create(self, validated_data):
        party = Party.objects.create(
            name=validated_data["name"],
            col=generate_col(10),
            description=validated_data["description"],
            location=validated_data["location"],
            date=validated_data["date"],
            max_attendees=validated_data["max_attendees"],
            host=validated_data["host"],
        )
        return party


class PartyListSerializer(ModelSerializer):
    host_name = ReadOnlyField(source="host.username")

    class Meta:
        model = Party
        fields = (
            "col",
            "name",
            "date",
            "location",
            "host_name",
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
