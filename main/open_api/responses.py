from rest_framework import serializers


class SuccessResponse(serializers.Serializer):
    message = serializers.ReadOnlyField(default="success")
    status = serializers.ReadOnlyField(default=200)


class SuccessDataResponse(SuccessResponse):
    def __init__(self, data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["data"] = data
