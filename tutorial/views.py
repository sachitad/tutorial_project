from django.views.generic import TemplateView

from .models import Topic, Category

class IndexView(TemplateView):
    """
    This is the homepage, I would like to call main page of my website Index
    What do we wanna show here:
    1) Subscribe, we want to collect as much user email as possible and send
    them nice content and come back to our website.
    2) Topics and their categories -> ie if you we have topic else (max 5)
    3) Categories and the tutorial title -> (max 5)
    """
    template_name = 'tutorial/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        topics = Topic.objects.all()
        # If we have topic send only topic to context
        # we will get categories from set_objects
        if topics.exists():
            context['topics'] = topics
        else:
            # if we don't have topic we send the categories and get tutorial
            # from set_objects
            context['categories'] = Category.objects.all()
        return context

