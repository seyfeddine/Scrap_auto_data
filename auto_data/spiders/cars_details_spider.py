import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CarUrlSpider(CrawlSpider):
    name = "cars_details"
    allowed_domains = ['www.auto-data.net']
    BASE_URL = "https://www.auto-data.net"

    def start_requests(self):
        yield scrapy.Request(url="https://www.auto-data.net/en/allbrands", callback=self.parse_brands)

    def parse_brands(self, response):
        brands = response.xpath('//a[@class="marki_blok"]/@href').getall()
        for brand in brands:
            yield response.follow(f"{self.BASE_URL}{brand}", callback=self.parse_models)

    def parse_models(self, response):
        models = response.xpath('//a[@class="modeli"]/@href').getall()
        for model in models:
            yield response.follow(f"{self.BASE_URL}{model}", callback=self.parse_models)

    def parse_generations(self, response):
        generations = response.xpath('//a[@class="position"]/@href').getall()
        for gen in generations:
            yield response.follow(f"{self.BASE_URL}{gen}", callback=self.parse_car_details)
    
    def parse_modifications(self, response):
        modifications = response.xpath("//th/a/@href").get()
        for mod in modifications:
            yield response.follow(f"{self.BASE_URL}{mod}", callback=self.parse_car_details)



    def parse_car_details(self):
        pass