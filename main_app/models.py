from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    appearance = models.TextField(max_length=250)
    seen = models.CharField(max_length=100)
    image = models.URLField(max_length=200)