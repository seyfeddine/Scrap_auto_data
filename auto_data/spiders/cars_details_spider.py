import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import BrandsItem

class CarUrlSpider(CrawlSpider):
    name = "cars_details"
    allowed_domains = ['www.auto-data.net']
    BASE_URL = "https://www.auto-data.net"

    def start_requests(self):
        yield scrapy.Request(url="https://www.auto-data.net/en/allbrands", callback=self.parse_brands)

    def parse_brands(self, response):
        brands = response.xpath('//a[@class="marki_blok"]')
        for brand in brands:
            brand_item = BrandsItem()
            brand_item["name"] = brand.xpath("strong/text()").get()
            brand_item["logo"] = brand.xpath("img/@src").get()
            yield brand_item
            brand_url = brand.xpath("@href").get()
            yield response.follow(f"{self.BASE_URL}{brand_url}", callback=self.parse_models)

    def parse_models(self, response):
        models_urls = response.xpath('//a[@class="modeli"]/@href').getall()
        for model in models_urls:
            yield response.follow(f"{self.BASE_URL}{model}", callback=self.parse_models)

    def parse_generations(self, response):
        generations_urls = response.xpath('//a[@class="position"]/@href').getall()
        for gen in generations_urls:
            yield response.follow(f"{self.BASE_URL}{gen}", callback=self.parse_car_details)
    
    def parse_modifications(self, response):
        modifications_urls = response.xpath("//th/a/@href").get()
        for mod in modifications_urls:
            yield response.follow(f"{self.BASE_URL}{mod}", callback=self.parse_car_details)



    def parse_car_details(self):
        pass