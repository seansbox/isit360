from django.db import models
from django.core import validators
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


class Celeb(models.Model):
    name = models.CharField(max_length=63)
    birthday = models.DateField(null=True, blank=True)
    birthplace = models.CharField(max_length=128)
    thumb = models.CharField(max_length=255, null=True, blank=True)
    summary = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


class Movie(models.Model):
    name = models.CharField(max_length=63)
    release = models.DateField()
    thumb = models.CharField(max_length=255, null=True, blank=True)
    summary = models.TextField(blank=True)
    meter = models.IntegerField(
        null=True, blank=True, validators=[validators.MaxValueValidator(100), validators.MinValueValidator(1)]
    )
    score = models.IntegerField(
        null=True, blank=True, validators=[validators.MaxValueValidator(100), validators.MinValueValidator(1)]
    )

    genres = models.ManyToManyField(Genre)
    celebs = models.ManyToManyField(Celeb)

    def __str__(self):
        return f"{self.name} ({self.release})"

    def get_absolute_url(self):
        return reverse("movies:detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["name"]
