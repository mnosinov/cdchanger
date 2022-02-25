from django.db import models
from django.core.validators import MinValueValidator


class Cdchanger(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField(validators=[MinValueValidator(1)])


class Disk(models.Model):
    cdchanger = models.ForeignKey(Cdchanger, on_delete=models.CASCADE)
    title=models.CharField(max_length=40)
    default = models.BooleanField(default=False)


class Track(models.Model):
    disk = models.ForeignKey(Disk, on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
