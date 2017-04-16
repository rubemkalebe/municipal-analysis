'''
Created on 14 de abr de 2017

@author: rubemkalebe
'''
from ..data.helpers import mun_school_helper
from ..places.mun_school import MunicipalSchool

class SchoolProcessor(object):
    '''
    classdocs
    '''


    def __init__(self, data):
        '''
        Constructor
        '''
        self.__data = data
        
        
    def processSchoolsByModality(self, schools, modality):
        for name, fund, mag, med, sup, esp, mes, dou, nen in zip(
                    self.__data[mun_school_helper.fields['name']],
                    self.__data[mun_school_helper.fields['fund']],
                    self.__data[mun_school_helper.fields['mag']],
                    self.__data[mun_school_helper.fields['med']],
                    self.__data[mun_school_helper.fields['sup']],
                    self.__data[mun_school_helper.fields['esp']],
                    self.__data[mun_school_helper.fields['mes']],
                    self.__data[mun_school_helper.fields['dou']],
                    self.__data[mun_school_helper.fields['nen']]):
            s = MunicipalSchool(name)
            if s in schools:
                s = self.retrieveSchool(s, schools)
                
            s.addTeachers(modality, mun_school_helper.education['fund'], fund)
            s.addTeachers(modality, mun_school_helper.education['mag'], mag)
            s.addTeachers(modality, mun_school_helper.education['med'], med)
            s.addTeachers(modality, mun_school_helper.education['sup'], sup)
            s.addTeachers(modality, mun_school_helper.education['esp'], esp)
            s.addTeachers(modality, mun_school_helper.education['mes'], mes)
            s.addTeachers(modality, mun_school_helper.education['dou'], dou)
            s.addTeachers(modality, mun_school_helper.education['nen'], nen)
            
            if s not in schools:
                schools.add(s)
            
    def retrieveSchool(self, s, schools):
        for i in schools:
            if i == s:
                return i