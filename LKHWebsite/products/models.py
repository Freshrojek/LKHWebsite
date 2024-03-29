from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=50) #max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.FloatField()
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField(default=False) #'null=True' or default=True or set on cmd
