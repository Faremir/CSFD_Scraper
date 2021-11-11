from django.shortcuts import render
from quicksearch.models import Movie


def view(request, csfd_if):
    movie_obj = Movie.objects.get(csfd_id=csfd_if)
    context = {
        "categoryName": "Herci:",
        "relativesName": "actor",
        "activeobj": movie_obj,
        "relatives": movie_obj.cast.all()
    }

    return render(request, 'item.html', context)
