'''
Created on 14 de abr de 2017

@author: rubemkalebe
'''

from ..places.place import Place

class MunicipalSchool(Place):
    '''
    A municipal school
    We store the teachers by their education
    A school here can support different modalities of teaching (Infantil, Fundamental e EJA)
    '''


    def __init__(self, name, address = '', neighborhood = '', district = '',
                 latitude = 0.0, longitude = 0.0, employees = 0, teachers = {}):
        '''
        Constructor with name
        '''
        Place.__init__(self, name, address, neighborhood, 
                       latitude, longitude, employees)
        self.__teachers = teachers
        self.__district = district
    
    
    def addTeachers(self, modality, education, quantity):
        self.employees += int(quantity)
        if modality not in self.__teachers:
            d = {}
            d[education] = int(quantity)
            self.__teachers[modality] = d 
        else:
            dd = self.__teachers[modality]
            dd[education] = int(quantity)

        
    def get_teachers(self):
        return self.__teachers
    
    
    def get_district(self):
        return self.__district

    def set_district(self, value):
        self.__district = value


    def place_as_dict(self):
        d = Place.place_as_dict(self)
        d['district'] = self.__district
        d['teachers'] = self.__teachers
        return d

    teachers = property(get_teachers, None, None, None)
    district = property(get_district, set_district, None, None)
