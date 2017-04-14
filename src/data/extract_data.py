'''
Created on 14 de abr de 2017

@author: rubemkalebe
'''

import pandas

class ExtractData(object):
    '''
    Extract data from Natal (Brazil) City Hall (http://ckan.imd.ufrn.br/) 
    '''

    @staticmethod
    def read_csv(url): 
        data = pandas.read_csv(url, sep = ',')
        return data 