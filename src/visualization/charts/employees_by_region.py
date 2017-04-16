'''
Created on 16 de abr de 2017

@author: rubemkalebe
'''

from bokeh.charts import Bar
from bokeh.charts.operations import blend
from bokeh.charts.attributes import cat

class EmployeesByRegion(object):
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
                d['NÃO DEFINIDO'] += p.employees
            elif p.district == '' and 'NÃO DEFINIDO' not in d:
                d['NÃO DEFINIDO'] = p.employees
            elif p.district.upper() in d:
                d[p.district.upper()] += p.employees
            else:
                d[p.district.upper()] = p.employees
        return d
    
    
    def plot(self, title = 'Employees by region'):
        data = self.processData()
        table = {
            'regions' : [x for x in sorted(data.keys())],
            'employees' : [data[x] for x in sorted(data.keys())]
        }
        
        bar = Bar(
                table,
                values = blend('employees', name = 'employees', labels_name = 'employees'),
                label = cat(columns = 'regions'),
                stack = cat(columns = 'employees'),
                agg = 'mean',
                title = title,
                legend = False,
                tooltips = [('Employees', '@employees')])
        return bar
        
    