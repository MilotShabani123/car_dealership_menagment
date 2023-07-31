# prepared import of enumerations
from model import Color, FuelType, Manufacturer, Transmission, Vehicle
# prepared csv module import
import csv
from typing import List

class VehicleFileManager:
    def __init__(self, file_path):
        self.file_path = file_path



    def import_vehicles_from_file(self, file_path):
        # TODO read vehicle-list.csv and transform to String array
        open_file = open(file_path, newline= "") 
        read_csv_file = csv.reader(open_file)
        data = []
        
        for row in read_csv_file:
            data.append("," .join(row))
        return data
            

    def rewrite_file(self, vehicle_list):
        # TODO write back into vehicle-list.csv and transform to String array
	    # TODO call method prepare_the_vehicle_for_rewriting(String, Vehicle)
        vehicle_string = ""
        
        for vehicle in vehicle_list :
            vehicle_string = self.prepare_the_vehicle_for_rewriting(vehicle_string, vehicle)
            vehicle_string += "\n"
        try:
            with open(self.file_path, "w" ,  newline= "" ) as csv_file:
                csv_file.write(vehicle_string)
        except IOError:
            print("An error occurred while writing the file")

    def prepare_the_vehicle_for_rewriting(self, vehicle_string_for_rewrite, vehicle):
        vehicle_values = [
            str(vehicle.get_id()) ,
            str(vehicle.get_manufacture().name),
            str(vehicle.get_model()),
            str(vehicle.get_horse_power()),
            str(vehicle.get_price()),
            str(vehicle.get_color().name),
            str(vehicle.get_price()),
            str(vehicle.get_producition_year()),
            str(vehicle.get_fuel_type().name),
            str(vehicle.get_transmission().name)
        ]
        vehicle_string_for_rewrite += "," .join(vehicle_values)
        return vehicle_string_for_rewrite
        

class VehicleShopPrinter:
    
    def print_available_vehicles(self, vehicle_list):
        # TODO Implement print available vehicle
        for vehicle in vehicle_list:
            print(self.prepare_vehicle_for_printing(vehicle))
        
    def prepare_vehicle_for_printing(self, vehicle):
        vehicle_string = [
            str(vehicle.get_id()) + "." ,
            "\t", 
            str(vehicle.get_manufacture().name),
            "\t",
            str(vehicle.get_model()),
            "\t",
            str(vehicle.get_horse_power()),
            "\t",
            str(vehicle.get_price()),
            "\t",
            str(vehicle.get_color().name),
            "\t",
            str(vehicle.get_price()),
            "\t",
            str(vehicle.get_producition_year()),
            "\t",
            str(vehicle.get_fuel_type().name),
            "\t",
            str(vehicle.get_transmission().name)
        ]
        return '' .join(vehicle_string)
        
    
    def print_vehicle_sold_message(self, vehicle_chosen_id):
        print("\nVehicle with ID", vehicle_chosen_id, "was sold.")
    
    def print_vehicle_id_to_sell_message(self):
        print("\n\n Please enter the number (ID) of the vehicle you want to sell: ")



class VehicleShopProcessor:

    # responsible to sell a specified vehicle by id

    def sell_vehicle(self, vehicles_list, vehicle_chosen_id):
        
    # TODO selling a vehicle means to remove it from the available vehicle list
    # Hint: use while loop to safely remove an oject from a list
        iterator = vehicles_list.__iter__()
        while True:
            try:
                vehicle = iterator.__next__()
                vehicle_id = vehicle.get_id()
                if vehicle_id == vehicle_chosen_id:
                    vehicles_list.remove(vehicle)
            except StopIteration:
                break
            

class VehicleTransformer:

    # transforms a data array into a {@link Vehicle} list 
	# @param vehicle data array
	# @return list of {@link Vehicle} objects

    def transform_data_array_to_vehicle_objects(self, vehicle_data_array: List[str]) -> List[Vehicle]:
        # TODO take data from String list and transform to list of vehicle objects
        # TODO call method transformToVehicleObject
        # Hint: use for loop
        vehicle_list = []
        for vehicle_as_string in vehicle_data_array:
            vehicle = self.transform_to_vehicle_object(vehicle_as_string)
            vehicle_list.append(vehicle)
        return vehicle_list

    # transforms a vehicle data record as String into a {@link Vehicle} object
	# @param vehicle data record as String 
	# @return {@link Vehicle} object 
    
    def transform_to_vehicle_object(self, vehicle_as_string: str) -> Vehicle:
        vehicle_as_array = vehicle_as_string.split(",")
        vehicle_id = int(vehicle_as_array[0])
        manufacture = self.get_manufacture_from_string(vehicle_as_array[1])
        model = vehicle_as_array[2]
        horse_power = int(vehicle_as_array[3])
        price = int(vehicle_as_array[4])
        color = self.get_color_from_string(vehicle_as_array[5])
        milage = int(vehicle_as_array[6])
        producition_year = int(vehicle_as_array[7])
        fuel_type= self.get_fuel_type_from_string(vehicle_as_array[8])
        transmission = self.get_transmission_from_string(vehicle_as_array[9])
        
        vehicle = Vehicle(vehicle_id, manufacture, model, horse_power, price, color, milage, producition_year, fuel_type, transmission)
        return vehicle
    
    def get_manufacture_from_string(self, manufacture_as_string):
        for manufacture in Manufacturer:
            if manufacture.name == manufacture_as_string:
                return manufacture
        raise ValueError("Manufacture is not suported: " + manufacture_as_string )
    
            
    def get_color_from_string(self, color_as_string):
        for color in Color:
            if color.name == color_as_string:
                return color
        raise ValueError(" Color is not suported: " + color_as_string)
    
        
    def get_fuel_type_from_string(self, fuel_type_as_string):
        for fuel_type in FuelType:
            if fuel_type.name == fuel_type_as_string:
                return fuel_type
        raise ValueError("Fuel type is not suported: " + fuel_type_as_string)
    
        
    def get_transmission_from_string(self, transmission_as_string):
        for transmission in Transmission:
            if transmission.name == transmission_as_string:
                return transmission
        raise ValueError("Transmission is not suported: " + transmission_as_string)
    

