from django.test import TestCase
from django.urls import reverse

from quicksearch.models import Actor
from quicksearch.models import Movie


class IndexViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Actor.objects.create(name="Alba Gaïa Kraghede Bellugi", csfd_id=0)

    def test_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_search_requests(self):
        response = self.client.get('', data={'search': 'alba'})
        self.assertEqual(response.status_code, 200)
        actor = response.context['actors'].all().first()
        self.assertIn("alba", actor.normalized_name)
        self.assertEqual(actor.csfd_id, 0)


class ActorViewTest(TestCase):
    elements_no = 13

    @classmethod
    def setUpTestData(cls):
        for i in range(cls.elements_no):
            Actor.objects.create(name="Irrelevant", csfd_id=i)

    def test_url(self):
        for i in range(self.elements_no):
            response = self.client.get(f"/actor/{i}/")
            self.assertEqual(response.status_code, 200)
            response = self.client.get(f"/actor/{i}")
            self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('/actor/10/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'item.html')


class MovieViewTest(TestCase):
    elements_no = 13

    @classmethod
    def setUpTestData(cls):
        for i in range(cls.elements_no):
            Movie.objects.create(name="Irrelevant", csfd_id=i)

    def test_url(self):
        for i in range(self.elements_no):
            response = self.client.get(f"/movie/{i}/")
            self.assertEqual(response.status_code, 200)
            response = self.client.get(f"/movie/{i}")
            self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/movie/10/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'item.html')
