from django import template

from tutorial.models import Topic, Category

register = template.Library()

@register.inclusion_tag('tutorial/nav_menu.html')
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


