'''
Created on 14 de abr de 2017

@author: rubemkalebe
'''

from places.place import Place

class MunicipalSchool(Place):
    '''
    A municipal school
    We store the teachers by their education
    A school here can support different modalities of teaching (Infantil, Fundamental e EJA)
    '''


    def __init__(self, name, latitude = 0.0, longitude = 0.0, employees = 0):
        '''
        Constructor with name
        '''
        Place.__init__(self, name, latitude, longitude, employees)
        self.__teachers = {}
        self.__modalities = set()


    def addModality(self, modality):
        self.__modalities.add(modality)
    
    
    def addTeachers(self, education, quantity):
        self.employees += quantity
        if education not in self.__teachers:
            self.__teachers[education] = quantity
        else:
            self.__teachers[education] += quantity

        
    def get_teachers(self):
        return self.__teachers

    def get_modalities(self):
        return self.__modalities

    teachers = property(get_teachers, None, None, None)
    modalities = property(get_modalities, None, None, None)
