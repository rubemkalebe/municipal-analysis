'''
Created on 17 de abr de 2017

@author: rubemkalebe
'''
from bokeh.charts import Bar
from bokeh.charts.operations import blend
from bokeh.charts.attributes import cat

class EmployeesPlot(object):
    '''
    classdocs
    '''


    def __init__(self, health_units, municipal_schools):
        '''
        Constructor
        '''
        self.__health_units = health_units
        self.__municipal_schools = municipal_schools
        
    def processData(self):
        d = {'Schools' : 0, 'Health units' : 0}
        for s in self.__municipal_schools:
            d['Schools'] += s.employees
        for u in self.__health_units:
            d['Health units'] += u.employees
        return d
        
    def plot(self, title = 'Municipal Schools and Health Units (Total of employees)'):
        data = self.processData()
        table = {
            'places' : [x for x in sorted(data.keys())],
            'employees' : [data[x] for x in sorted(data.keys())]
        }
        
        bar = Bar(
                table,
                values = blend('employees', name = 'employees', labels_name = 'employees'),
                label = cat(columns = 'places'),
                stack = cat(columns = 'employees'),
                agg = 'mean',
                title = title,
                legend = False,
                tooltips = [('Employees', '@employees')])
        return bar