from django.shortcuts import render

from quicksearch.lib import stringUtils
from quicksearch.models import Actor, Movie


def view(request):
    search = request.POST.get("search", "")
    if search:
        search = stringUtils.normalize(search)
    movies = Movie.objects.filter(normalized_name__contains=search)
    actors = Actor.objects.filter(normalized_name__contains=search)

    context = {
            'lookup': search is not None,
            'movies': movies,
            'actors': actors
            }
    return render(request, 'index.html', context)
