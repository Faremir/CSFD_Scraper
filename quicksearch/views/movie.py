from django.shortcuts import render
from quicksearch.models import Movie


def view(request, csfd_id):
    movie_obj = Movie.objects.get(csfd_id=csfd_id)
    context = {
            "categoryName" : "Herci:",
            "relativesName": "actor",
            "activeobj"    : movie_obj,
            "relatives"    : movie_obj.cast.all()
            }

    return render(request, 'item.html', context)
