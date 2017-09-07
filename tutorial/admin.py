from django.contrib import admin

from .models import Topic, Category, Tutorial


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    pass