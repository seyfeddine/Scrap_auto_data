from db import Brands, Details, Generations, Models, Modifications
from .items import *
from sqlalchemy.orm import sessionmaker
import db
import uuid


class AutoDataPipeline:

    def open_spider(self, spider):
        Session = sessionmaker(bind=db.engine)
        self.session = Session()
        self.brandname_map = {}
        self.modelname_map = {}
        self.generationname_map = {}
        self.modification_map = {}

        # counters to show the data progress
        self.brands_count = 0
        self.models_count = 0
        self.generations_count = 0
        self.modification_count =0
        self.details_count = 0

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        if item.__class__ == BrandsItem:
            bid = str(uuid.uuid4())
            brand = Brands(**{**item, "bid": bid})
            self.brandname_map[brand.name] = bid
            self.session.add(brand)
            self.session.commit()
            self.brands_count += 1

        elif item.__class__ == ModelsItem:
            brand_name = item.get("brand_name")
            bid = self.brandname_map[brand_name]
            mid = str(uuid.uuid4())
            model = Models(**{**item, "bid": bid, "mid": mid})
            self.modelname_map["-".join([brand_name,model.name])] = mid #added
            self.session.add(model)
            self.session.commit()
            self.models_count += 1

        elif item.__class__ == GenerationItem:
            model_name = item.get("model_name")
            mid = self.modelname_map[model_name]
            gid = str(uuid.uuid4())
            generation = Generations(**{**item, "gid": gid, "mid": mid})
            self.generationname_map["-".join([model_name, generation.name])] = gid
            self.session.add(generation)
            self.session.commit()
            self.generations_count += 1
        
           
            
        elif item.__class__ == ModificationItem:
            generation_name = item.get("generation_name")
            gid = self.generationname_map[generation_name]
            moid = str(uuid.uuid4())
            modification = Modifications(**{**item, "gid": gid, "moid": moid})
            self.modification_map["-".join([generation_name, modification.name])] = moid
            self.session.add(modification)
            self.session.commit()
            self.modification_count += 1

        elif item.__class__ == CarDetailsItem:
            modification_name = item.get("modification_name")
            moid = self.modification_map[modification_name]
            did = str(uuid.uuid4())
            detail = Details(**{**item, "did": did, "moid": moid})
            self.session.add(detail)
            self.session.commit()
            self.details_count +=1
            
             

        print(
            f"Created {self.brands_count} brands, {self.models_count} models, {self.generations_count} generations, {self.modification_count} modifications, {self.details_count} details"
            , end="\r")