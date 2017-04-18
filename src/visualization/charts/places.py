'''
Created on 17 de abr de 2017

@author: rubemkalebe
'''
from bokeh.charts import Bar
from bokeh.charts.operations import blend
from bokeh.charts.attributes import cat

class PlacesPlot(object):
    '''
    classdocs
    '''


    def __init__(self, health_units, municipal_schools):
        '''
        Constructor
        '''
        self.__health_units = health_units
        self.__municipal_schools = municipal_schools
        
    def plot(self, title = 'Municipal Schools and Health Units (Total of units)'):
        data = {
            'Schools' : len(self.__municipal_schools),
            'Health units' : len(self.__health_units)
        }
        table = {
            'places' : [x for x in sorted(data.keys())],
            'units' : [data[x] for x in sorted(data.keys())]
        }
        
        bar = Bar(
                table,
                values = blend('units', name = 'units', labels_name = 'units'),
                label = cat(columns = 'places'),
                stack = cat(columns = 'units'),
                agg = 'mean',
                title = title,
                legend = False,
                tooltips = [('Units', '@units')])
        return bar