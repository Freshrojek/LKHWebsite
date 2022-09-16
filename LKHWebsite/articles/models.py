from django.db import models
from datetime import date

# Create your models here.
class Article(models.Model):
    """Table schema to store articles."""
    name = models.CharField(max_length=64)
    author = models.ForeignKey('articles.Author', on_delete=models.CASCADE)
    content = models.TextField()
    overview = models.TextField()
    slug = models.CharField(default='', max_length=64)
    date = models.DateField("Date", auto_now_add=True)

    def __str__(self):
        return '%s' % self.name

class Author(models.Model):
    """Table schema to store auhtors."""
    name = models.CharField(max_length=64)
    slug = models.CharField(default='', max_length=64)

    def __str__(self):
        return '%s' % self.name
