import json

import scrapy


class ElectricitypricesSpider(scrapy.Spider):
    name = 'electricityPrices'
    allowed_domains = ['eia.gov']
    start_urls = ['https://api.eia.gov/v2/electricity/retail-sales/data/?api_key'
                  '=CZdQsisRJzwOfqUWV3jiMPNEx3ZbHcuJ2VQus04i&frequency=monthly&data['
                  '0]=price&start=2021-01&sort[0][column]=period&sort[0]['
                  'direction]=desc&offset=0&length=5000']
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'electricity_prices.json'

    }

    def parse(self, response):
        json_data = json.loads(response.body)
        data = json_data['response']['data']
        yield {'data': data}
