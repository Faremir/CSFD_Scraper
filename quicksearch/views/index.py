from django.shortcuts import render

from quicksearch.lib import stringUtils
from quicksearch.models import Actor, Movie


def view(request):
    search = request.POST.get("search", None)
    context = {'lookup': search is not None}
    if search:
        normalized = stringUtils.normalize(search)
        context["movies"] = Movie.objects.filter(normalized_name__contains=normalized)
        context["actors"] = Actor.objects.filter(normalized_name__contains=normalized)

    return render(request, 'index.html', context)
