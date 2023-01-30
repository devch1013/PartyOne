from rest_framework.serializers import ModelSerializer, Serializer, ReadOnlyField
from .models import Party


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
            "id",
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
