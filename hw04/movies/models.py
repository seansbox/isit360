from django.db import models
from django.core import validators

class Movie(models.Model):
    name = models.CharField(max_length=63)
    release = models.DateField()
    thumb = models.CharField(max_length=255, null=True, blank=True)
    summary = models.TextField(blank=True)
    meter = models.IntegerField(null=True, blank=True, validators=[
        validators.MaxValueValidator(100),
        validators.MinValueValidator(1)
    ])
    score = models.IntegerField(null=True, blank=True, validators=[
        validators.MaxValueValidator(100),
        validators.MinValueValidator(1)
    ])

    def __str__(self):
        return f"{self.name} ({self.release})"

class Celeb(models.Model):
    name = models.CharField(max_length=63)
    birthday = models.DateField()
    birthplace = models.CharField(max_length=128)
    thumb = models.CharField(max_length=255, null=True, blank=True)
    summary = models.TextField(blank=True)

    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return f"{self.name}"
