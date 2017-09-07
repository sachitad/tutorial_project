from django.views.generic import TemplateView


class IndexView(TemplateView):
    """
    This is the homepage, I would like to call main page of my website Index
    """
    template_name = 'tutorial/index.html'