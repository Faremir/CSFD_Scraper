from django.urls import re_path, path

from . import views

app_name = "quicksearch"
urlpatterns = [
        path('', views.index.view, name='index'),
        re_path(r'movie/(?P<csfd_id>\d+)/?$', views.movie.view, name='movie'),
        re_path(r'actor/(?P<csfd_id>\d+)/?$', views.actor.view, name='actor')
]
