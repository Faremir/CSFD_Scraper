from django.db.models import signals
from django.dispatch import receiver

from quicksearch.models import Actor, Movie


@receiver(signals.pre_delete, sender=Movie)
def pre_delete_movie(sender, instance, using, **kwargs):
    for actor in instance.cast.all():
        if actor.filmography.count() == 1:
            actor.delete()
    instance.cast.clear()

