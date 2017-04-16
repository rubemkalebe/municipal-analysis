'''
Created on 16 de abr de 2017

@author: rubemkalebe
'''

from bokeh.charts import Bar
from bokeh.charts.operations import blend
from bokeh.charts.attributes import cat

class PlacesByRegion(object):
    '''
    classdocs
    '''


    def __init__(self, places):
        '''
        Constructor
        '''
        self.__places = places    
    
    
    def processData(self):
        d = {}
        for p in self.__places:
            if p.district == '' and 'NÃO DEFINIDO' in d:
                d['NÃO DEFINIDO'] += 1
            elif p.district == '' and 'NÃO DEFINIDO' not in d:
                d['NÃO DEFINIDO'] = 1
            elif p.district.upper() in d:
                d[p.district.upper()] += 1
            else:
                d[p.district.upper()] = 1
        return d
    
    
    def plot(self, title = 'Units by region'):
        data = self.processData()
        table = {
            'regions' : [x for x in sorted(data.keys())],
            'units' : [data[x] for x in sorted(data.keys())]
        }
        
        bar = Bar(
                table,
                values = blend('units', name = 'units', labels_name = 'units'),
                label = cat(columns = 'regions'),
                stack = cat(columns = 'units'),
                agg = 'mean',
                title = title,
                legend = False,
                tooltips = [('Units', '@units')])
        return bar
        
    