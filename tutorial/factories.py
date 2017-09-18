import factory

from .models import Topic, Category, Tutorial


class TopicFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Topic
    name = factory.Iterator(['Python', 'C', 'Java'])


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = factory.Iterator(['Introduction', 'Flow Control', 'Functions',
                             'Arrays'])
    topic = factory.SubFactory(TopicFactory)


class TutorialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tutorial
    category = factory.SubFactory(CategoryFactory)
    title = 'Introduction to this programming language'
    body = 'This is the body for now'

