from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ring(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, blank=True, on_delete=models.DO_NOTHING)
    how_to_get = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='images')
    user = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


