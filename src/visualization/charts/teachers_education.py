'''
Created on 16 de abr de 2017

@author: rubemkalebe
'''
from bokeh.charts import Donut

class TeachersEducationPlot(object):
    '''
    classdocs
    '''


    def __init__(self, schools):
        '''
        Constructor
        '''
        self.__schools = schools
        
    def processData(self):
        d = {}
        for s in self.__schools:
            for m in s.teachers: # 'eja' : {}, 'inf' : {}, 'fund' : {}
                for e in s.teachers[m]: # {'med' : x, 'sup' : y}
                    if e in d and s.teachers[m][e] != 0:
                        d[e] += s.teachers[m][e]
                    elif e not in d and s.teachers[m][e] != 0:
                        d[e] = s.teachers[m][e]
        return d
        
    def plot(self):
        data = self.processData()
        table = {
            'education' : [x for x in sorted(data.keys())],
            'quantity' : [data[x] for x in sorted(data.keys())]
        }
        return Donut(
                    table,
                    label = ['education'],
                    values = 'quantity',
                    text_font_size = '10pt',
                    hover_text = 'quantity'
                )