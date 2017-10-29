from django.views.generic import TemplateView, DetailView
from django.http import HttpResponse

from .models import Topic, Category, Tutorial, Subscriber

from .forms import SubscriberForm

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


class TopicView(DetailView):
    """
    This the topic view, this is the page when clicks on the topic
    In this page we will display categories of corresponding topic in a card
    and all the tutorials
    """
    template_name = 'tutorial/topic.html'

    model = Topic


class TutorialView(DetailView):
    """
    This is where we show the tutorial
    /topic-slug/tutorial-slug/
    """
    template_name = 'tutorial/tutorial.html'

    model = Tutorial


def subscribe_view(request):
    """
    Subscribe the user to python guides
    """
    if request.is_ajax() and request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            subscriber = Subscriber.objects.filter(email=email)
            # Only add if email doesn't exist before
            if not subscriber.exists():
                Subscriber.objects.create(email=email)
            return HttpResponse(status=200)

    return HttpResponse(status=400)