
'''
This dictionary maps each detail as specified in the html
to it's specific item
'''
detailsMapper = {

    # General  --------------------------------------------

 'Brand': 'brand',  
 'Model ': 'model',  
 'Generation  ': 'generation',  
 'Modification (Engine) ': 'modification',  
 'Start of production ': 'start_production',  
 'End of production ': 'end_production',  
 'Powertrain Architecture ': 'powertrain_architecture',  
 'Body type': 'body_type',  
 'Seats ': 'number_of_seats',  
 'Doors ': 'number_of_doors',  
 
    # performance --------------------------------------------

 'Fuel consumption (economy) - urban ': 'nedc_fuel_consumption_urban_l',  
 'Fuel consumption (economy) - extra urban': 'nedc_fuel_consumption_extra_urban_l',
 'Fuel consumption (economy) - extra urban (NEDC)': 'nedc_fuel_consumption_combined_l',  
 'CO 2  emissions (NEDC)': 'nedc_co2_g',
 'Fuel Type ': 'fuel_type',  
 'Acceleration 0 - 100 km/h': 'acceleration_s',
#  'Acceleration 0 - 62 mph': '',
#  'Acceleration 0 - 60 mph (Calculated by Auto-Data.net) ': '',
 'Maximum speed ': 'max_speed_km_h', 
 
 # Engine ----------------------------------------------

#  'Emission standard ': '',  
#  'Weight-to-power ratio ': '',  
#  'Weight-to-torque ratio ': '',  
#  'Power ': '',  
#  'Power per litre ': '',  
 'Torque ': 'torque_nm',  
#  'Engine location ': '',  
#  'Engine Model/Code ': '',  
#  'Engine displacement ': '',  
 'Number of cylinders ': 'number_of_cylinders',  
#  'Position of cylinders ': '',  
 'Cylinder Bore ': 'bore_mm',  
 'Piston Stroke ': 'stroke_mm',  
 'Compression ratio ': 'compression_ratio',  
 'Number of valves per cylinder ': 'number_of_valves_per_cylinder',  
#  'Fuel System ': '',  
#  'Engine aspiration ': '',  
#  'Valvetrain  ': '',  
 'Engine oil capacity ': 'engine_oil_capacity_l', 
 
 # Space ---------------------------------------------

#  'Engine oil specification ': '',  
#  'Coolant ': '',  
 'Kerb Weight ': 'curb_weight_kg',  
 'Max. weight ': 'max_weigh_kg',
 'Max load': 'max_load_kg',
#  'Trunk (boot) space - minimum ': '',
#  'Trunk (boot) space - maximum ': '',  
 'Fuel tank capacity ': 'fuel_tank_capacity_l',   
 
 # Dimensions -------------------------------------------------

#  'Permitted trailer load with brakes (12%) ': '',
#  'Permitted trailer load without brakes ': '',
#  'Permitted towbar download ': '',
 'Length ': 'length_mm',  
 'Width ': 'width_mm',  
 'Height ': 'height_mm',  
 'Wheelbase ': 'wheelbase_mm',  
 'Front track ': 'front_track_mm',  
 'Rear (Back) track ': 'rear_track_mm',  
 'Front overhang ': 'front_overhang_mm',  
 'Rear overhang ': 'rear_overhang_mm', 
 
  # Drivetrain, brakes and suspension specs ----------------------------------------------------

#  'Minimum turning circle (turning diameter) ': '',
#  'Drivetrain Architecture ': '',  
#  'Drive wheel ': '',  
 'Number of Gears (automatic transmission) ': 'number_of_gears',  
#  'Front suspension ': '',  
#  'Rear suspension ': '',  
#  'Front brakes': '',  
#  'Rear brakes': '',  
#  'Assisting systems': '',  
#  'Steering type ': '',  
#  'Tires size':'',
#  'Wheel rims size': ''
}
