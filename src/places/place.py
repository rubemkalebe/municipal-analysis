'''
Created on 14 de abr de 2017

@author: rubemkalebe
'''

class Place(object):
    '''
    It represents a general place which is identified by a name
    It is localized by its geographical position
    '''


    def __init__(self, name, latitude = 0.0, longitude = 0.0, employees = 0):
        '''
        Constructor with the place name
        '''
        self.__name = name
        self.__latitude = latitude
        self.__longitude = longitude
        self.__employees = employees


    def get_employees(self):
        return self.__employees

    def set_employees(self, value):
        self.__employees = value
        

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


    name = property(get_name, set_name, None, None)
    latitude = property(get_latitude, set_latitude, None, None)
    longitude = property(get_longitude, set_longitude, None, None)
    employees = property(get_employees, set_employees, None, None)
