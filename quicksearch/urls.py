from django.urls import path

from . import views

app_name = "quicksearch"
urlpatterns = [
        path('', views.index.view, name='index'),
        path('movie/<int:csfd_if>', views.movie.view, name='movie'),
        path('actor/<int:csfd_if>', views.actor.view, name='actor'),
]
