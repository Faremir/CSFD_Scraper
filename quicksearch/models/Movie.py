from django.db import models
from django.utils import timezone

from quicksearch.lib import stringUtils


class Movie(models.Model):
    name = models.CharField(max_length=255)
    normalized_name = models.CharField(max_length=255)
    csfd_id = models.IntegerField(default=0, null=False, unique=True)
    cast = models.ManyToManyField("Actor", related_name="cast", blank=True, default=None)

    class Meta:
        ordering = ["csfd_id"]

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.normalized_name = stringUtils.normalize(self.name)
        super(Movie, self).save(*args, **kwargs)
