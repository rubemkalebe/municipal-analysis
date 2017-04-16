'''
Created on 15 de abr de 2017

@author: rubemkalebe
'''
from ..data.helpers import health_unit_helper
from ..data.extract_data import ExtractData
from ..processors.health_unit_processor import HealthUnitProcessor
from ..processors.extract_health_units_addresses import ExtractHealthUnitsAddresses
from ..database import connectDB
from ..database.health_unit_dao import HealthUnitDAO

from tqdm import tqdm

class GetHealthUnits(object):
    '''
    classdocs
    '''

    @staticmethod
    def get():
        
        health_units = set()
        db = connectDB.connect()
        huDAO = HealthUnitDAO(db)
        #huDAO.clear()
        #print('Count: ' + str(db.health_units.count()))
        
        if db.health_units.count() > 0:
            health_units = huDAO.fetchall()
        else:
            for district in tqdm(sorted(health_unit_helper.dataset_2014.keys())):
                data = ExtractData.read_csv(health_unit_helper.dataset_2014[district], ';')
                p = HealthUnitProcessor(data)
                p.processHealthUnitsByDistrict(health_units, district)
            e = ExtractHealthUnitsAddresses(ExtractData.read_csv(health_unit_helper.addr_2014, ';'))
            e.extractAddresses(health_units)
            e.getLatLng(health_units)
            for u in tqdm(list(health_units)):
                huDAO.insert(u)
            
        return health_units