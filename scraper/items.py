from scrapy_djangoitem import DjangoItem
from quicksearch.models import Movie, Actor


class CSFDMovie(DjangoItem):
    django_model = Movie


class CSFDActor(DjangoItem):
    django_model = Actor
