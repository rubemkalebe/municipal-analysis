'''
Created on 14 de abr de 2017

@author: rubemkalebe
'''
from ..data.helpers import health_unit_helper
from ..places.health_unit import HealthUnit
from ..localization.locate_place import LocatePlace

class HealthUnitProcessor(object):
    '''
    classdocs
    '''


    def __init__(self, data):
        '''
        Constructor
        '''
        self.__data = data
        
    def processHealthUnitsByDistrict(self, units, district):
        for unid in self.__data.UNIDADE.unique():
            h = HealthUnit(unid, district)
            series = self.__data[self.__data[health_unit_helper.fields['unid']]
                                == unid][health_unit_helper.fields['esp']]
            dic = series.value_counts().to_dict()
            for k in sorted(dic.keys()):
                dic[k.title()] = int(dic.pop(k))
            h.practitioners = dic
            h.employees = sum(h.practitioners.values())
            units.add(h)