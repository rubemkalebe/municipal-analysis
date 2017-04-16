'''
Created on 14 de abr de 2017

@author: rubemkalebe
'''

from ..places.place import Place

class HealthUnit(Place):
    '''
    A health unit
    We store the practitioners by their fields of expertise
    A health unit belongs to a district (Leste, Norte I, Norte II, Oeste, Sul)
    '''


    def __init__(self, name, district, address = '', neighborhood = '',
                 latitude = 0.0, longitude = 0.0, employees = 0, practitioners = {}):
        '''
        Constructor with name and district
        '''
        Place.__init__(self, name, address, neighborhood, latitude, longitude, employees)
        self.__district = district
        self.__practitioners = practitioners
        
        
    def addPractitioners(self, field, quantity):
        self.employees += int(quantity)
        if field not in self.__practitioners:
            self.__practitioners[field] = int(quantity)
        else:
            self.__practitioners[field] += int(quantity)
        
        
    def get_district(self):
        return self.__district


    def get_practitioners(self):
        return self.__practitioners


    def set_district(self, value):
        self.__district = value
        
    def set_practitioners(self, value):
        self.__practitioners = value

    
    def place_as_dict(self):
        d = Place.place_as_dict(self)
        d['district'] = self.__district
        d['practitioners'] = self.__practitioners
        return d

    district = property(get_district, set_district, None, None)
    practitioners = property(get_practitioners, set_practitioners, None, None)
