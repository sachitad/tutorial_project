from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField

from adminsortable.models import SortableMixin



class Topic(SortableMixin):
    """
    This model basically stores what is the tutorial topic about:
    like django, python or whatever
    """
    name = models.CharField(max_length=255, unique=True,
                            help_text='High Level: Python or Ruby or ROR')
    slug = models.SlugField(unique=True) # by default max length 50
    body = RichTextField(blank=True)
    order = models.PositiveIntegerField(default=0, editable=False,
                                        db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tutorial:topic', args=[self.slug])

    class Meta:
        ordering = ['order']


class Category(SortableMixin):
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
    order = models.PositiveIntegerField(default=0, editable=False,
                                        db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['order']


class Tutorial(models.Model):
    """
    Tutorial will belong to Category and Topic
    """
    # Enforcing that this tutorial website will have category
    # This is how I like it
    category = models.ForeignKey(Category, related_name='tutorials')
    title = models.CharField(max_length=255)
    body = RichTextField()

    def __str__(self):
        return self.title
