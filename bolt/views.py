from bolt import settings
from django.views.generic import TemplateView


class IndexView(TemplateView):
    '''
    Renders the index page
    '''
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        return {'VERSION': settings.VERSION}
