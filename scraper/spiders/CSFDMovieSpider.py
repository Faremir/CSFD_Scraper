import scrapy
import re

from scraper.items import CSFDMovie
from quicksearch.models import Movie


class CSFDMovieSpider(scrapy.Spider):
    name = "CSFD Movie Spider"
    custom_settings = {
        'DEPTH_STATS_VERBOSE': True,
        'CONCURRENT_REQUESTS': 1,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'CONCURRENT_REQUESTS_PER_IP': 1,
        'AUTOTHROTTLE_TARGET_CONCURRENCY': 1,
        'AUTOTHROTTLE_ENABLED': False
    }

    crawl_no = 300
    chart_type = "nejlepsi"

    persistent_index = 0

    def __init__(self, movie_no, chart_type, *args, **kwargs):
        """
        :param movie_no:   Number of movies to scrape
        :param chart_type: Movie chart type
        """
        super(CSFDMovieSpider, self).__init__(*args, **kwargs)
        self.crawl_no = movie_no
        self.chart_type = chart_type

    def start_requests(self):
        for page_index in range(0, self.crawl_no + 100, 100):
            url = f"https://www.csfd.cz/zebricky/filmy/{self.chart_type}/?from={str(page_index)}"
            request = scrapy.Request(url, priority=1000 - page_index)
            yield request
            if self.persistent_index >= self.crawl_no: break

    def parse(self, response, **kwargs):
        data = response.css("article.article")
        for line in data:
            if self.persistent_index >= self.crawl_no: break
            self.persistent_index += 1
            csfd_id = line.css("article::attr(id)").extract_first().strip()
            csfd_id = re.search(r'\d+', csfd_id).group()
            if not Movie.objects.filter(csfd_id=csfd_id).exists():
                item = CSFDMovie()
                item['name'] = line.css(".film-title-name::text").extract_first().strip()
                item['csfd_id'] = csfd_id
                item.save()
        return  # Processing items in pipeline changes order of the movies
