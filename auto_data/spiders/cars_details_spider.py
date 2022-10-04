import scrapy
from ..items import BrandsItem, CarDetailsItem, GenerationItem, ModelsItem, ModificationItem
from .helpers import detailsMapper


class CarUrlSpider(scrapy.Spider):
    name = "cars_details"
    allowed_domains = ['www.auto-data.net']
    BASE_URL = "https://www.auto-data.net"

    def start_requests(self):
        yield scrapy.Request(url="https://www.auto-data.net/en/allbrands", callback=self.parse_brands)

    def parse_brands(self, response):
        '''
        this is docs
        '''
        brands = response.xpath('//a[@class="marki_blok"]')
        for brand in brands:
            brand_item = BrandsItem()
            brand_item["name"] = brand.xpath("strong/text()").get()
            brand_item["logo"] = brand.xpath("img/@src").get()
            yield brand_item
            brand_url = brand.xpath("@href").get()
            yield response.follow(f"{self.BASE_URL}{brand_url}", callback=self.parse_models)

    def parse_models(self, response):
        models_urls = response.xpath('//a[@class="modeli"]')
        for model in models_urls:
            model_item = ModelsItem()
            model_item["name"] = model.xpath('strong/text()').get()
            model_item["thumbnail"] = model.xpath('img/@src').get()
            yield model_item
            model_url = model.xpath("@href").get()
            yield response.follow(f"{self.BASE_URL}{model_url}", callback=self.parse_generations)

    def parse_generations(self, response):
        generations_trs = response.xpath(
            "//table[@class='generr']").xpath("tr[@class='f lred']")
        for generation in generations_trs:
            generation_item = GenerationItem()
            generation_item["name"] = generation.xpath(
                'th[@class="i"]/a[@class="position" and not(@rel = "nofollow")]/strong/text()'
            ).get()
            generation_item["thumbnail_url"] = self.BASE_URL + generation.xpath(
                'th[@class="i"]/*/img/@src').get()
            generation_years = generation.xpath(
                'td[@class="i"]/*/strong[@class="end"]/text()'
            ).get()
            generation_item["start_year"], generation_item["end_year"] = generation_years.split(' - ') if generation_years else ('','')
            generation_item["body_type"] = generation.xpath(
                'td[@class="i"]/*/strong[@class="chas"]/text()').get()
            generation_item["details"] = generation.xpath(
                'td[@class="i"]/*/span/text()').getall()
            yield generation_item
            generation_url = generation.xpath('*/a/@href').get()
            yield response.follow(f"{self.BASE_URL}{generation_url}", callback=self.parse_modifications)

    def parse_modifications(self, response):
        modifications_trs = response.xpath(
            '//table[@class="carlist"]/tr[@class="i lred"]')
        for mod in modifications_trs:
            mod_item = ModificationItem()
            mod_item["name"] = mod.xpath(
                'th[@class="i"]/*/*/span[@class="tit"]/text()').get()
            mod_item["start_year"], mod_item["end_year"] = mod.xpath(
                'th[@class="i"]/*/*/span[@class="end"]/text()'
            ).get().split(' - ')
            mod_item["details"] = ' | '.join(
                mod.xpath('td[@class="i"]/a[@rel="nofollow"]/text()').getall())
            yield mod_item
            mod_url = mod.xpath('th/a/@href').get()
            yield response.follow(f"{self.BASE_URL}{mod_url}", callback=self.parse_car_details)

    def parse_car_details(self, response):
        car_details_trs = response.xpath(
            '//table[@class="cardetailsout car2"]/tr[not(@class)]')
        car_det_item = CarDetailsItem()
        car_det_item["images"] = [ self.BASE_URL+ "/images/" +line.split('"')[1] for line in response.xpath('//div[@id="outer"]/script[not(@src)]/text()').get().split('\n') if "bigs" in line and "jpg" in line]
        for car_det_tr in car_details_trs:
            car_det_th = car_det_tr.xpath("th/text()").get()
            car_det_td = car_det_tr.xpath("td")[0]
            if car_det_th in detailsMapper.keys():
                car_det_item[detailsMapper[car_det_th]] = ' | '.join(
                    car_det_td.xpath("text() | */text()").getall()
                    ).replace('\r\n', '').replace('\t', '').strip()
        return car_det_item
