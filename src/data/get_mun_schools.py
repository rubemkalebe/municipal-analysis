'''
Created on 15 de abr de 2017

@author: rubemkalebe
'''
from ..data.extract_data import ExtractData
from ..data.helpers import mun_school_helper
from ..processors.school_processor import SchoolProcessor
from ..processors.extract_schools_addresses import ExtractSchoolsAddresses
from ..database import connectDB
from ..database.mun_school_dao import MunicipalSchoolDAO

from tqdm import tqdm

class GetMunicipalSchools(object):
    '''
    classdocs
    '''

    @staticmethod
    def get():
        schools = set()
        db = connectDB.connect()
        scDAO = MunicipalSchoolDAO(db)
        #scDAO.clear()
        #print('Count: ' + str(db.municipal_schools.count()))

        if db.municipal_schools.count() > 0:
            schools = scDAO.fetchall()
        else:            
            for mod in tqdm(['fund', 'inf', 'eja']):
                if mod == 'eja':
                    data = ExtractData.read_csv(mun_school_helper.dataset_2014['eja'], ',')
                    p = SchoolProcessor(data)
                    p.processSchoolsByModality(schools, mun_school_helper.modalities['eja'])
                else:
                    data = ExtractData.read_csv(mun_school_helper.dataset_2014[mod], ';')
                    p = SchoolProcessor(data)
                    p.processSchoolsByModality(schools, mun_school_helper.modalities[mod])
                
            e = ExtractSchoolsAddresses(ExtractData.read_csv(mun_school_helper.dataset_2014['addrs_esc'], ';'),
                                       ExtractData.read_csv(mun_school_helper.dataset_2014['addrs_cmei'], ';'))
            e.extractAddresses(schools)
            e.getLatLng(schools)
            for s in tqdm(list(schools)):
                scDAO.insert(s)
        
        return schools