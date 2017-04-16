'''
Created on 15 de abr de 2017

@author: rubemkalebe
'''
from ..places.health_unit import HealthUnit



class HealthUnitDAO(object):
    '''
    classdocs
    '''


    def __init__(self, db):
        '''
        Constructor
        '''
        self.__db = db
        
    def insert(self, _unit):
        self.__db.health_units.insert_one(_unit.place_as_dict())
    
    def fetchall(self):
        units = set()
        empCol = self.__db.health_units.find()
        for emp in empCol:
            u = HealthUnit(
                name = emp['name'],
                district = emp['district'],
                address = emp['address'],
                neighborhood = emp['neighborhood'],
                latitude = emp['latitude'],
                longitude = emp['longitude'],
                employees = int(emp['employees']),
                practitioners = emp['practitioners']
            )
            units.add(u)
        return units
    
    def clear(self):
        self.__db.health_units.remove({})
    
    