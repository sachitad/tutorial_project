from django.conf.urls import url

from .views import IndexView, TopicView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[\w-]+)/$', TopicView.as_view(), name='topic'),
]
