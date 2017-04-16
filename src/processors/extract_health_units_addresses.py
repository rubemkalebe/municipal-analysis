'''
Created on 14 de abr de 2017

@author: rubemkalebe
'''
from ..data.helpers import health_unit_helper
from ..localization.locate_place import LocatePlace

from tqdm import tqdm

class ExtractHealthUnitsAddresses(object):
    '''
    classdocs
    '''


    def __init__(self, data):
        '''
        Constructor
        '''
        self.__data = data
        
    def extractAddresses(self, units):
        for u in tqdm(list(units)):
            for name, addr, neighb in zip(
                    self.__data[health_unit_helper.fields['est']],
                    self.__data[health_unit_helper.fields['end']],
                    self.__data[health_unit_helper.fields['bai']]):
                if u.name == 'PAJUÇARA' and name == 'UBS Pajuçara':
                    u.address = addr
                    u.neighborhood = neighb
                    break
                elif u.name == 'PLANÍCE DAS MANGUEIRAS' and name == 'USF Planíciedas Mangueiras':
                    u.name = 'PLANÍCIE DAS MANGUEIRAS'
                    u.address = addr
                    u.neighborhood = neighb
                    break
                elif name.startswith('USF') and u.name.lower() in name.lower()\
                        and u.name != 'REDINHA':
                    u.address = addr
                    u.neighborhood = neighb
                    break
                elif name.startswith('USF') and u.name.lower() in name.lower()\
                        and u.name == 'REDINHA':
                    u.address = 'Rua do Campo'
                    u.neighborhood = neighb
                    break
                
    def getLatLng(self, units):
        for u in tqdm(list(units)):
            u.latitude, u.longitude = LocatePlace.locate(u)
        