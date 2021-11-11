from enum import Enum
from django.core.management.base import BaseCommand
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scraper.spiders import CSFDMovieSpider as MovieSpider, CSFDActorSpider as ActorSpider


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--count', '-c', nargs='+', type=int)
        parser.add_argument('--best', '-tb', action="store_const", const="nejlepsi", dest="type"),
        parser.add_argument('--favourites', '-tf', action="store_const", const="nejoblibenejsi", dest="type"),
        parser.add_argument('--controversial', '-tc', action="store_const", const="nejrozporuplnejsi", dest="type"),
        parser.add_argument('--worst', '-tw', action="store_const", const="nejhorsi", dest="type"),

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        movie_no = options['count'] if options['count'] else 300
        chart_type = options['type'] if options['type'] else 0

        @defer.inlineCallbacks
        def crawl():
            """ Chaining the deferreds spiders to run synchronously in one thread """
            yield process.crawl(MovieSpider.CSFDMovieSpider, movie_no=movie_no, chart_type=chart_type)
            yield process.crawl(ActorSpider.CSFDActorSpider)
            reactor.stop()

        # process.crawl(ActorSpider.CSFDActorSpider)

        crawl()
        reactor.run()
