'''
Created on 15 de abr de 2017

@author: rubemkalebe
'''
import folium
from tqdm import tqdm

class HealthUnitsMap(object):
    '''
    classdocs
    '''


    def __init__(self, units):
        '''
        Constructor
        '''
        self.__units = units
        
    def generateMap(self):
        # Set map center and zoom level
        mapc = [-5.797757, -35.245127]
        zoom = 12
        
        # Create map object
        map_osm = folium.Map(location = mapc, zoom_start = zoom)
        
        # Plot each of the locations that we geocoded
        for u in tqdm(list(self.__units)):
            folium.Marker([u.latitude, u.longitude],
                popup = 'USF ' + u.name,
                icon = folium.Icon(color = 'green')
                ).add_to(map_osm)
        
        # Return the map
        return map_osm