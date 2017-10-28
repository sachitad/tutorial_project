from django.contrib import admin

from adminsortable.admin import SortableAdmin

from .models import Topic, Category, Tutorial


@admin.register(Topic)
class TopicAdmin(SortableAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(SortableAdmin):
    pass


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    pass