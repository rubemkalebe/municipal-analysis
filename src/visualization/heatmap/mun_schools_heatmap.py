'''
Created on 15 de abr de 2017

@author: rubemkalebe
'''

from folium.plugins import HeatMap
import folium
from tqdm import tqdm

class MunicipalSchoolsHeatmap(object):
    '''
    classdocs
    '''


    def __init__(self, schools):
        '''
        Constructor
        '''
        self.__schools = schools
        
    def generateMap(self):
        # Set map center and zoom level
        mapc = [-5.797757, -35.245127]
        zoom = 12
        
        coordinates = []

        for s in tqdm(list(self.__schools)):
            coordinates.append([s.latitude, s.longitude, s.employees])
        
        # Create map object
        m = folium.Map(location = mapc, zoom_start = zoom)
        
        HeatMap(coordinates).add_to(m)
        
        return m