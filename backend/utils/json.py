from django.http import JsonResponse
from django.views.generic import TemplateView


__all__ = [
    'JSONResponseMixin',
    'JSONView'
]


class JSONResponseMixin:
    def render_to_json_response(self, context, **kwargs):
        resp = {
            'response': self.get_data(context)
        }
        return JsonResponse(
            resp,
            **kwargs
        )

    def get_data(self, context):
        return context


class JSONView(JSONResponseMixin, TemplateView):
    def render_to_response(self, context, **kwargs):
        return self.render_to_json_response(context, **kwargs)
