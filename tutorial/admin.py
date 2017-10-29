from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
# Note: we are renaming the original Admin and Form as we import them!
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld
from django import forms

from ckeditor.widgets import CKEditorWidget

from adminsortable.admin import SortableAdmin

from .models import Topic, Category, Tutorial, Subscriber


@admin.register(Topic)
class TopicAdmin(SortableAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(SortableAdmin):
    pass


@admin.register(Tutorial)
class TutorialAdmin(SortableAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Subscriber)
class SubscriberAdmin(SortableAdmin):
    pass


class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = FlatPage # this is not automatically inherited from FlatpageFormOld
        fields = '__all__'


class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm


# We have to unregister the normal admin, and then reregister ours
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)