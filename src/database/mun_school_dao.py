'''
Created on 15 de abr de 2017

@author: rubemkalebe
'''
from ..places.mun_school import MunicipalSchool

class MunicipalSchoolDAO(object):
    '''
    classdocs
    '''


    def __init__(self, db):
        '''
        Constructor
        '''
        self.__db = db
        
    def insert(self, _school):
        self.__db.municipal_schools.insert_one(_school.place_as_dict())
    
    def fetchall(self):
        schools = set()
        empCol = self.__db.municipal_schools.find()
        for emp in empCol:
            s = MunicipalSchool(
                name = emp['name'],
                address = emp['address'],
                neighborhood = emp['neighborhood'],
                district = emp['district'],
                latitude = emp['latitude'],
                longitude = emp['longitude'],
                employees = int(emp['employees']),
                teachers = emp['teachers']
            )
            schools.add(s)
        return schools
    
    def clear(self):
        self.__db.municipal_schools.remove({})