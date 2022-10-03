# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field



class BrandsItem(scrapy.Item):
    name = scrapy.Field()
    logo = scrapy.Field()
    pass

class ModelsItem(scrapy.Item):
    name = scrapy.Field()
    thumbnail = scrapy.Field()
    pass

class GenerationItem(scrapy.Item):
    name = scrapy.Field()
    thumbnail_url = scrapy.Field()
    start_year = scrapy.Field()
    end_year = scrapy.Field()
    body_type = scrapy.Field()
    details = scrapy.Field()
    pass

class SpecsItem(scrapy.Item):
    name = scrapy.Field()
    start_year = scrapy.Field()
    end_year = scrapy.Field()
    details = scrapy.Field()
    pass

class CarDetailsItem(scrapy.Item):

    # general
    brand = scrapy.Field()
    model = scrapy.Field()
    generation = scrapy.Field()
    modification = scrapy.Field()
    start_production = scrapy.Field()
    end_production = scrapy.Field()
    powertrain_architecture = scrapy.Field()
    body_type = scrapy.Field()
    number_of_seats = scrapy.Field()
    number_of_doors = scrapy.Field()


    #Performance
    nedc_fuel_consumption_urban_l = scrapy.Field()
    nedc_fuel_consumption_extra_urban_l = scrapy.Field()
    nedc_fuel_consumption_combined_l = scrapy.Field()
    nedc_co2_g = scrapy.Field()
    fuel_type = scrapy.Field()
    acceleration_s = scrapy.Field()
    max_speed_km_h = scrapy.Field()

    #Engine
    torque_nm = scrapy.Field()
    number_of_cylinders = scrapy.Field()
    bore_mm = scrapy.Field()
    stroke_mm = scrapy.Field()
    compression_ratio = scrapy.Field()
    number_of_valves_per_cylinder = scrapy.Field()
    engine_oil_capacity_l = scrapy.Field()

    #Space
    curb_weight_kg = scrapy.Field()
    max_weigh_kg = scrapy.Field()
    max_load_kg = scrapy.Field()
    fuel_tank_capacity_l = scrapy.Field()

    #Dimensions
    length_mm = scrapy.Field()
    width_mm = scrapy.Field()
    height_mm = scrapy.Field()
    wheelbase_mm = scrapy.Field()
    front_track_mm = scrapy.Field()
    rear_track_mm = scrapy.Field()
    front_overhang_mm = scrapy.Field()
    rear_overhang_mm = scrapy.Field()

    # Drivetrain, brakes and suspension specs
    number_of_gears = scrapy.Field()


