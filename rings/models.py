from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ring(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name
