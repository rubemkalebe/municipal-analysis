'''
Created on 14 de abr de 2017

@author: rubemkalebe
'''

from places.place import Place

class HealthUnit(Place):
    '''
    A health unit
    We store the practitioners by their fields of expertise
    A health unit belongs to a district (Leste, Norte I, Norte II, Oeste, Sul)
    '''


    def __init__(self, name, district, latitude = 0.0, longitude = 0.0, employees = 0):
        '''
        Constructor with name and district
        '''
        Place.__init__(self, name, latitude, longitude, employees)
        self.__district = district
        self.__practitioners = {}
        
        
    def addPractitioners(self, field, quantity):
        self.employees += quantity
        if field not in self.__practitioners:
            self.__practitioners[field] = quantity
        else:
            self.__practitioners[field] += quantity
        
        
    def get_district(self):
        return self.__district


    def get_practitioners(self):
        return self.__practitioners


    def set_district(self, value):
        self.__district = value

    district = property(get_district, set_district, None, None)
    practitioners = property(get_practitioners, None, None, None)
