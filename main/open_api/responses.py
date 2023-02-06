from rest_framework import serializers


class SuccessSimpleResponse(serializers.Serializer):
    message = serializers.ReadOnlyField(default="success")
    status = serializers.ReadOnlyField(default=200)


class SuccessListDataResponse(SuccessSimpleResponse):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["data"] = kwargs["data"]


class SuccessSingleDataResponse(SuccessSimpleResponse):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["data"] = kwargs["data"]
