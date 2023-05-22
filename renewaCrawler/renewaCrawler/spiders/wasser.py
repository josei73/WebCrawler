import scrapy


class WasserSpider(scrapy.Spider):
    name = 'wasser'
    allowed_domains = ['water.gov']
    start_urls = ['http://water.gov/']

    def parse(self, response):

        pass
