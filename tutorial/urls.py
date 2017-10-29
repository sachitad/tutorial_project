from django.conf.urls import url, include

from .views import IndexView, TopicView, TutorialView, subscribe_view

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    # This needs to be here because of the rule of topic url
    url(r'^subscribe/$', subscribe_view, name='subscribe'),
    url(r'^(?P<slug>[\w-]+)/$', TopicView.as_view(), name='topic'),
    url(r'^(?P<topic_slug>[\w-]+)/(?P<slug>[\w-]+)/$', TutorialView.as_view(),
        name='tutorial'),
]
