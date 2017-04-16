'''
Created on 15 de abr de 2017

@author: rubemkalebe
'''
import folium
from tqdm import tqdm

class MunicipalSchoolsMap(object):
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
        
        # Create map object
        map_osm = folium.Map(location = mapc, zoom_start = zoom)
        
        # Plot each of the locations that we geocoded
        for s in tqdm(list(self.__schools)):
            if 'CMEI' in s.name:
                folium.Marker([s.latitude, s.longitude],
                    popup = s.name,
                    icon = folium.Icon(color = 'green')
                    ).add_to(map_osm)
            else:
                folium.Marker([s.latitude, s.longitude],
                    popup = s.name,
                    icon = folium.Icon(color = 'blue')
                    ).add_to(map_osm)
        
        # Return the map
        return map_osm