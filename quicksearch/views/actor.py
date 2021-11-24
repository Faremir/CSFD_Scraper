from django.shortcuts import render
from quicksearch.models import Actor, Movie


def view(request, csfd_id):
    actor_obj = Actor.objects.get(csfd_id=csfd_id)
    context = {
        "categoryName": "Filmy:",
        "relativesName": "movie",
        "activeobj": actor_obj,
        "relatives": Movie.objects.filter(cast=actor_obj.pk),
    }

    return render(request, 'item.html', context)
