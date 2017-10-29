from django import template

from tutorial.models import Topic, Category
from tutorial.forms import SubscriberForm

register = template.Library()

@register.inclusion_tag('tutorial/includes/nav_menu.html')
def nav_menu():
    """
    Get the topics and show them as nav menu
    If No topics - we know it is a specific niche tutorial website such as
    python tutorial.com so show category as nav menu
    """
    # Both of these have name attribute so don't hesitate while calling
    # that attribute name in template
    topics = Topic.objects.all()
    if topics.exists():
        return {'menu': topics}
    return {'menu': Category.objects.all()}


@register.inclusion_tag('tutorial/includes/form.html')
def subscriber_form():
    """
    We want to show the subscriber form in the footer in all the pages
    thus creating this template tag
    """
    return {'form': SubscriberForm}


