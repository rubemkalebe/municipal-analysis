'''
Created on 14 de abr de 2017

@author: rubemkalebe
'''

import numpy

class Place(object):
    '''
    It represents a general place which is identified by a name
    It is localized by its geographical position
    '''


    def __init__(self, name, address = '', neighborhood = '',
                 latitude = 0.0, longitude = 0.0, employees = 0):
        '''
        Constructor with the place name
        '''
        self.__name = name
        self.__address = address
        self.__neighborhood = neighborhood
        self.__latitude = latitude
        self.__longitude = longitude
        self.__employees = employees

        
    def __hash__(self):
        return hash((self.__name))

    def __eq__(self, other):
        return self.__name == other.name
    
    
    def get_neighborhood(self):
        return self.__neighborhood

    def set_neighborhood(self, value):
        self.__neighborhood = value
        
    
    def get_address(self):
        return self.__address

    def set_address(self, value):
        self.__address = value
    
    
    def get_employees(self):
        return self.__employees

    def set_employees(self, value):
        self.__employees = int(value)
        

    def get_latitude(self):
        return self.__latitude

    def get_longitude(self):
        return self.__longitude


    def set_latitude(self, value):
        self.__latitude = value

    def set_longitude(self, value):
        self.__longitude = value


    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value


    def place_as_dict(self):
        return {
            'name' : self.__name,
            'latitude' : self.__latitude,
            'longitude' : self.__longitude,
            'employees' : self.__employees,
            'address' : self.__address,
            'neighborhood' : self.__neighborhood 
        }

    name = property(get_name, set_name, None, None)
    latitude = property(get_latitude, set_latitude, None, None)
    longitude = property(get_longitude, set_longitude, None, None)
    employees = property(get_employees, set_employees, None, None)
    address = property(get_address, set_address, None, None)
    neighborhood = property(get_neighborhood, set_neighborhood, None, None)
