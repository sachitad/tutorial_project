from django.conf.urls import url

from .views import IndexView, TopicView, TutorialView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[\w-]+)/$', TopicView.as_view(), name='topic'),
    url(r'^(?P<topic_slug>[\w-]+)/(?P<slug>[\w-]+)/$', TutorialView.as_view(),
        name='tutorial'),
]
