import scrapy


class WindSpider(scrapy.Spider):
    name = 'wind'
    allowed_domains = ['weather.gov']
    start_urls = ['http://weather.gov/']

    def parse(self, response):
        pass
