from django.test import TestCase
from quicksearch.models import Actor
from quicksearch.models import Movie


class ActorTest(TestCase):
    normalized_names = {
            0: ("Alba Gaïa Kraghede Bellugi", "alba gaia kraghede bellugi"),
            1: ("Ahna O'Reilly", "ahna o'reilly")
            }

    @classmethod
    def setUpTestData(cls):
        for key, value in cls.normalized_names.items():
            Actor.objects.create(name=value[0], csfd_id=key)

    def test_normalized_name(self):
        for key, value in self.normalized_names.items():
            obj = Actor.objects.get(csfd_id=key)
            self.assertEqual(obj.normalized_name, value[1])


class MovieTest(TestCase):
    normalized_names = {
            0: ("Jeanne d'Arc", "jeanne d'arc"),
            1: ("Šermon na pastvě", "sermon na pastve"),
            2: ("Světáci", "svetaci")
            }

    @classmethod
    def setUpTestData(cls):
        for key, value in cls.normalized_names.items():
            Movie.objects.create(name=value[0], csfd_id=key)

    def test_normalized_name(self):
        for key, value in self.normalized_names.items():
            obj = Movie.objects.get(csfd_id=key)
            self.assertEqual(obj.normalized_name, value[1])
