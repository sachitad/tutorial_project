from django.db import models

from ckeditor.fields import RichTextField


class Topic(models.Model):
    """
    This model basically stores what is the tutorial topic about:
    like django, python or whatever
    """
    topic = models.CharField(max_length=255,
                             help_text='High Level: Python or Ruby or ROR')

    def __str__(self):
        return self.topic


class Category(models.Model):
    """
    There can be category styled tutorial, this model handles that
    """
    name = models.CharField(max_length=255)
    # If your tutorial website is niche based like pythontutorial.com
    # you won't be creating topic so this is optional
    topic = models.ForeignKey(Topic, blank=True, null=True,
                              help_text='If you have used topic make sure'
                                        'to input it here')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Tutorial(models.Model):
    """
    Tutorial will belong to Category and Topic
    """
    # Enforcing that this tutorial website will have category
    # This is how I like it
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=255)
    body = RichTextField()

    def __str__(self):
        return self.title