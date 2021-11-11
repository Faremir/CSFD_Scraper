from django.db import models

from quicksearch.lib import stringUtils


class Actor(models.Model):
    name = models.CharField(max_length=255)
    normalized_name = models.CharField(max_length=255)
    csfd_id = models.IntegerField(default=0, null=False, unique=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.normalized_name = stringUtils.normalize(self.name)
        super(Actor, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
