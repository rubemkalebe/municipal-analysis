'''
Created on 14 de abr de 2017

@author: rubemkalebe
'''

import geocoder
from ..places.health_unit import HealthUnit
from ..places.mun_school import MunicipalSchool

class LocatePlace(object):
    '''
    classdocs
    '''


    @staticmethod
    def locate(place):
        if isinstance(place, MunicipalSchool):
            g = geocoder.google(place.name + ' natal')
            if g.latlng == []:
                g = geocoder.google(place.address + ' natal')
            return g.latlng[0], g.latlng[1]
        elif isinstance(place, HealthUnit):
            if place.name == 'PANATIS':
                g = geocoder.google('Unidade de Saúde da Família panatis natal')
                return g.latlng[0], g.latlng[1]
            g = geocoder.google(place.address + ' natal')
            if g.latlng == []:
                g = geocoder.google(place.name + ' posto de saude natal')
            return g.latlng[0], g.latlng[1]