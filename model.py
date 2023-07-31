from enum import Enum

class Vehicle:
    def __init__(self, id, manufacture, model, horse_power, price, color, milage,  producition_year, fuel_type, transmission ) -> None:
        
    # TODO Vehicle implementation
	# TODO add attributes and Getters / Setters
       self.__id = id
       self.__manufacture = manufacture
       self.__model = model
       self.__horse_power = horse_power
       self.__price = price
       self.__color = color
       self.__milage = milage
       self.__producition_year = producition_year
       self.__fuel_type = fuel_type
       self.__transmission = transmission
       
    def get_id(self):
        return self.__id
    
    def set_id(self,id):
        self.__id = id
    
    def get_manufacture(self):
        return self.__manufacture
    
    def set_manufacture(self,manufacture):
        self.__manufacture = manufacture
    
    def get_model(self):
        return self.__model
    
    def set_model(self,model):
        self.__model = model
        
    def get_model(self):
        return self.__model
    
    def set_model(self,model):
        self.__model = model
        
    def get_horse_power(self):
        return self.__horse_power
    
    def set_horse_power(self,horse_power):
        self.__horse_power = horse_power
        
    def get_price(self):
        return self.__price
    
    def set_price(self,price):
        self.__price = price
        
    def get_color(self):
        return self.__color
    
    def set_color(self,color):
        self.__id = color
    
    def get_milage(self):
        return self.__milage
    
    def set_milage(self, milage):
        self.__milage = milage
        
    def get_producition_year(self):
        return self.__producition_year
    
    def set_producition_year(self,producition_year):
        self.__producition_year = producition_year
        
    def get_fuel_type(self):
        return self.__fuel_type
    
    def set_fuel_type(self,fuel_type):
        self.__fuel_type = fuel_type
        
    def get_transmission(self):
        return self.__transmission
    
    def set_transmission(self,transmission):
        self.__transmission = transmission
        
    

class Color(Enum):
    # TODO define color enumeraition literals 
    BLACK = 1
    RED = 2
    WHITE = 3
    BLUE = 4
    GREY = 5
    BROWN = 6
    YELLOW = 7

class FuelType(Enum):
    # TODO define fuel type enumeraition literals
    GASOLINE = 1
    DIESEL_FUEL = 2

class Manufacturer(Enum):
    # TODO define manufacturer enumeraition literals
    AUDI = 1
    BMW = 2
    VW = 3
    HONDA = 4
    SKODA = 5

class Transmission(Enum):
    # TODO define transmission enumeraition literals 
    MANUAL = 1
    AUTOMATIC = 2