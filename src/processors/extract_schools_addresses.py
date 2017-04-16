'''
Created on 14 de abr de 2017

@author: rubemkalebe
'''
from ..localization.locate_place import LocatePlace
from ..data.helpers import mun_school_helper

from tqdm import tqdm

class ExtractSchoolsAddresses(object):
    '''
    classdocs
    '''


    def __init__(self, data_esc, data_cmei):
        '''
        Constructor
        '''
        self.__data_esc = data_esc
        self.__data_cmei = data_cmei
        
    def extractAddresses(self, schools):
        for s in tqdm(list(schools)):
            data = None
            if s.name.startswith('CMEI'):
                data = self.__data_cmei
            else:
                data = self.__data_esc
            for reg, est, end, neighb in zip(
                    data[mun_school_helper.fields['reg']],
                    data[mun_school_helper.fields['est']],
                    data[mun_school_helper.fields['end']],
                    data[mun_school_helper.fields['bai']]):
                if s.name == 'CMEI PROFA MARIA DOS MARTIRIOS LISBOA DE MENEZES' and\
                        'DOS MARTIRIOS' in est and est.startswith('CMEI'):
                    s.district = reg
                    s.address = end
                    s.neighborhood = neighb
                    break
                elif s.name == 'CMEI PROFA MARIA DE FÁTIMA MEDEIROS DE ARAÚJO' and\
                        'DE FÁTIMA MEDEIROS DE ARAÚJO' in est and est.startswith('CMEI'):
                    s.district = reg
                    s.address = end
                    s.neighborhood = neighb
                    break
                if s.name == est:
                    s.district = reg
                    s.address = end
                    s.neighborhood = neighb
                    break
    
    def getLatLng(self, schools):
        for u in tqdm(list(schools)):
            u.latitude, u.longitude = LocatePlace.locate(u)