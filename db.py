
from tracemalloc import start
from sqlalchemy import ForeignKey, create_engine, null, true
from sqlalchemy import Column, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


engine = create_engine('sqlite:///autodata.db')#, echo=True)

base = declarative_base()


# Our Tables
class Brands(base):
    __tablename__ = 'brands'

    bid = Column(String, primary_key=true)
    name = Column(String, nullable=True)
    logo = Column(String, nullable=True)

    def __init__(self, bid, name, logo):
        self.bid = bid
        self.name = name
        self.logo = logo


class Models(base):
    __tablename__ = 'models'

    mid = Column(String, primary_key=true)
    bid = Column(String, ForeignKey('brands.bid'))
    name = Column(String, nullable=True)
    thumbnail = Column(String, nullable=True)
    parent = relationship(Brands, backref='children')

    def __init__(self, mid, name, thumbnail, bid, brand_name=None):
        self.mid = mid
        self.name = name
        self.thumbnail = thumbnail
        self.bid = bid


class Generations(base):

    __tablename__ = 'generations'

    gid = Column(String, primary_key=true)
    mid = Column(String, ForeignKey('models.mid'))
    name = Column(String, nullable=True)
    thumbnail = Column(String, nullable=True)
    start_year = Column(String, nullable=True)
    end_year = Column(String, nullable=True)
    body_type = Column(String, nullable=True)
    details = Column(String,  nullable=True)
    parent = relationship(Models, backref='children')

    def __init__(self, gid, name, thumbnail, start_year, end_year, body_type, details, mid, model_name=None):
        self.gid = gid
        self.name = name
        self.thumbnail = thumbnail
        self.start_year = start_year
        self.end_year = end_year
        self.body_type = body_type
        self.details = details
        self.mid = mid

class Modifications(base):
    __tablename__ = 'modifications'

    moid = Column(String, primary_key = true)
    gid = Column(String, ForeignKey('generations.gid'))
    name = Column(String, nullable=True)
    start_year = Column(String, nullable=True)
    end_year = Column(String, nullable=True)
    details = Column(String, nullable=True)
    parent = relationship(Generations, backref='children')

    def __init__(self, moid, name, start_year, end_year, details, gid, generation_name=None):
        self.gid = gid
        self.moid = moid
        self.name = name
        self.start_year = start_year
        self.end_year = end_year
        self.details = details


class Details(base):

    __tablename__ = 'details'

    did = Column(String, primary_key = true)
    moid = Column(String, ForeignKey('modifications.moid'))
    
    images = Column(String, nullable=True)

    # general
    brand = Column(String, nullable=True)
    model = Column(String, nullable=True)
    generation = Column(String, nullable=True)
    modification = Column(String, nullable=True)
    start_production = Column(String, nullable=True)
    end_production = Column(String, nullable=True)
    powertrain_architecture = Column(String, nullable=True)
    body_type = Column(String, nullable=True)
    number_of_seats = Column(String, nullable=True)
    number_of_doors = Column(String, nullable=True)


    #Performance
    nedc_fuel_consumption_urban_l = Column(String, nullable=True)
    nedc_fuel_consumption_extra_urban_l = Column(String, nullable=True)
    nedc_fuel_consumption_combined_l = Column(String, nullable=True)
    nedc_co2_g = Column(String, nullable=True)
    fuel_type = Column(String, nullable=True)
    acceleration_s = Column(String, nullable=True)
    max_speed_km_h = Column(String, nullable=True)

    #Engine
    torque_nm = Column(String, nullable=True)
    number_of_cylinders = Column(String, nullable=True)
    bore_mm = Column(String, nullable=True)
    stroke_mm = Column(String, nullable=True)
    compression_ratio = Column(String, nullable=True)
    number_of_valves_per_cylinder = Column(String, nullable=True)
    engine_oil_capacity_l = Column(String, nullable=True)

    #Space
    curb_weight_kg = Column(String, nullable=True)
    max_weigh_kg = Column(String, nullable=True)
    max_load_kg = Column(String, nullable=True)
    fuel_tank_capacity_l = Column(String, nullable=True)

    #Dimensions
    length_mm = Column(String, nullable=True)
    width_mm = Column(String, nullable=True)
    height_mm = Column(String, nullable=True)
    wheelbase_mm = Column(String, nullable=True)
    front_track_mm = Column(String, nullable=True)
    rear_track_mm = Column(String, nullable=True)
    front_overhang_mm = Column(String, nullable=True)
    rear_overhang_mm = Column(String, nullable=True)

    # Drivetrain, brakes and suspension specs
    number_of_gears = Column(String, nullable=True)

    parent = relationship(Modifications, backref='children')

    def __init__ (self,did=None, moid =None,images=None, brand=None, model=None, generation=None, modification=None, start_production=None, end_production=None, powertrain_architecture=None, body_type=None, number_of_seats=None, number_of_doors=None, nedc_fuel_consumption_urban_l=None, nedc_fuel_consumption_extra_urban_l=None, nedc_fuel_consumption_combined_l=None, nedc_co2_g=None, fuel_type=None, acceleration_s=None, max_speed_km_h=None, torque_nm=None, number_of_cylinders=None, bore_mm=None, stroke_mm=None, compression_ratio=None, number_of_valves_per_cylinder=None, engine_oil_capacity_l=None, curb_weight_kg=None, max_weigh_kg=None, max_load_kg=None, fuel_tank_capacity_l=None, length_mm=None, width_mm=None, height_mm=None, wheelbase_mm=None, front_track_mm=None, rear_track_mm=None, front_overhang_mm=None, rear_overhang_mm=None, number_of_gears=None, modification_name=None):
           
            self.did = did
            self.moid = moid

           # images
            self.images =  images

            # general
            self.brand =  brand
            self.model =  model
            self.generation =  generation
            self.modification =  modification
            self.start_production =  start_production
            self.end_production =  end_production
            self.powertrain_architecture =  powertrain_architecture
            self.body_type =  body_type
            self.number_of_seats =  number_of_seats
            self.number_of_doors =  number_of_doors


            #Performance
            self.nedc_fuel_consumption_urban_l =  nedc_fuel_consumption_urban_l
            self.nedc_fuel_consumption_extra_urban_l =  nedc_fuel_consumption_extra_urban_l
            self.nedc_fuel_consumption_combined_l =  nedc_fuel_consumption_combined_l
            self.nedc_co2_g =  nedc_co2_g
            self.fuel_type =  fuel_type
            self.acceleration_s =  acceleration_s
            self.max_speed_km_h =  max_speed_km_h

            #Engine
            self.torque_nm =  torque_nm
            self.number_of_cylinders =  number_of_cylinders
            self.bore_mm =  bore_mm
            self.stroke_mm =  stroke_mm
            self.compression_ratio =  compression_ratio
            self.number_of_valves_per_cylinder =  number_of_valves_per_cylinder
            self.engine_oil_capacity_l =  engine_oil_capacity_l

            #Space
            self.curb_weight_kg =  curb_weight_kg
            self.max_weigh_kg =  max_weigh_kg
            self.max_load_kg =  max_load_kg
            self.fuel_tank_capacity_l =  fuel_tank_capacity_l

            #Dimensions
            self.length_mm =  length_mm
            self.width_mm =  width_mm
            self.height_mm =  height_mm
            self.wheelbase_mm =  wheelbase_mm
            self.front_track_mm =  front_track_mm
            self.rear_track_mm =  rear_track_mm
            self.front_overhang_mm =  front_overhang_mm
            self.rear_overhang_mm =  rear_overhang_mm

            # Drivetrain, brakes and suspension specs
            self.number_of_gears =  number_of_gears

        
base.metadata.create_all(engine)
