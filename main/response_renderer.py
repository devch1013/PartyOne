from rest_framework.renderers import JSONRenderer


class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context:
            if renderer_context["response"].status_code == 200:
                return super().render({"message": "success", "status": 200, "data": data})
            else:
                return super().render(
                    {
                        "message": "fail",
                        "status": renderer_context["response"].status_code,
                        "data": data,
                    }
                )
        else:
            return super().render(data)
