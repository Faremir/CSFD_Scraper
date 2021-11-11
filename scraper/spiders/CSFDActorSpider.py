import re

import scrapy
from scraper.items import CSFDActor
from quicksearch.models import Movie, Actor


class CSFDActorSpider(scrapy.Spider):
    name = "CSFD Actor Spider"
    item_index = 0
    actors = set()
    custom_settings = {

        'CONCURRENT_ITEMS': 200,
        'CONCURRENT_REQUESTS ': 50,
        'DOWNLOAD_DELAY ': 0,
        'CONCURRENT_REQUESTS_PER_DOMAIN ': 50,
        'LOG_LEVEL ': 'ERROR',
        'RETRY_TIMES ': 2,
        'CONNECTION_TIMEOUT ': 30,
        'RANDOMIZE_DOWNLOAD_DELAY  ': True,
    }

    def start_requests(self):

        for movie in Movie.objects.all():
            url = f"https://www.csfd.cz/film/{str(movie.csfd_id)}"
            yield scrapy.Request(url, meta={"current_movie": movie.pk})

    def parse(self, response, **kwargs):
        for line in response.xpath("//h4[contains(text(), 'Hrají')]//..//a[contains(@href,'/tvurce/')]"):
            csfd_id = line.css("a::attr(href)").extract_first().strip()
            csfd_id = re.search(r'\d+', csfd_id).group()
            if Actor.objects.filter(csfd_id=csfd_id).exists():
                item = Actor.objects.get(csfd_id=csfd_id)
            else:
                item = CSFDActor()
                item['name'] = line.css("a::text").extract_first().strip()
                item['csfd_id'] = csfd_id
                item = item.save()
            movie = Movie.objects.get(pk=response.meta['current_movie'])
            if not movie.cast.filter(pk=item.pk).exists():
                movie.cast.add(item)
