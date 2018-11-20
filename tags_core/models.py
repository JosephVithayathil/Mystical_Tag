from django.db import models

# Create your models here.

class Tags(models.Model):
    """Player Level model."""

    name = models.CharField(max_length=25, null=True, unique=True)
    popularity = models.FloatField(default=0.0)
    is_deleted = models.BooleanField(default=False)


class Director(models.Model):
    """Director model."""

    name = models.CharField(max_length=250, null=True, unique=True)
    popularity = models.FloatField(default=0.0)
    is_deleted = models.BooleanField(default=False)


class Movie(models.Model):
    """Movie model."""

    name = models.CharField(max_length=250, null=True)
    popularity = models.FloatField(default=0.0)
    imdb_score = models.FloatField(default=0.0)
    director = models.ForeignKey(Director, related_name="movie_director",
                                 null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
