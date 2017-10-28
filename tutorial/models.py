from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField

from adminsortable.models import SortableMixin

from django_extensions.db.models import TimeStampedModel


class AdminSortableModel(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False,
                                        db_index=True)

    class Meta:
        abstract = True


class Topic(AdminSortableModel, TimeStampedModel):
    """
    This model basically stores what is the tutorial topic about:
    like django, python or whatever
    """
    name = models.CharField(max_length=255, unique=True,
                            help_text='High Level: Python or Ruby or ROR')
    slug = models.SlugField(unique=True) # by default max length 50
    body = RichTextField(blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tutorial:topic', args=[self.slug])

    class Meta:
        ordering = ['order']


class Category(AdminSortableModel, TimeStampedModel):
    """
    There can be category styled tutorial, this model handles that
    """
    name = models.CharField(max_length=255)
    # If your tutorial website is niche based like pythontutorial.com
    # you won't be creating topic so this is optional
    topic = models.ForeignKey(Topic, blank=True, null=True,
                              help_text='If you have used topic make sure'
                                        'to input it here',
                              related_name='categories')
    body = RichTextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['order']

    def get_absolute_url(self):
        tutorial = self.tutorials.first()
        if tutorial:
            return reverse('tutorial:tutorial',
                       args=[self.topic.slug, tutorial.slug])


class Tutorial(AdminSortableModel, TimeStampedModel):
    """
    Tutorial will belong to Category and Topic
    """
    # Enforcing that this tutorial website will have category
    # This is how I like it
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, related_name='tutorials')
    body = RichTextField()

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('tutorial:tutorial',
                       args=[self.category.topic.slug, self.slug])

    def next_tutorial(self):
        tutorial = self.category.tutorials.filter(order=self.order+1)
        if tutorial.exists():
            tutorial = tutorial[0]
            return reverse('tutorial:tutorial',
                           args=[tutorial.category.topic.slug, tutorial.slug])

    def previous_tutorial(self):
        tutorial = self.category.tutorials.filter(order=self.order-1)
        if tutorial.exists():
            tutorial = tutorial[0]
            return reverse('tutorial:tutorial',
                           args=[tutorial.category.topic.slug, tutorial.slug])


    class Meta:
        ordering = ['order']

