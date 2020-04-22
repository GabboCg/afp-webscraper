# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:39:22 2020

@author: Habac
"""

import pandas as pd
import datetime as dt
from aux_function import call_data

# df grande, importa master de series bcch
dfg = pd.read_excel("series.xls")

# df chico, con solo las series bcch seleccionadas
dfc = dfg[dfg.pull==1].drop_duplicates(subset = 'Código')

# params
hoy = dt.date.today()

for ind, row in dfc.iterrows():
    
    print(row['Nombre de la serie'], '\n', row['Código'], '\n', row['firstdate'])
    # print(row['englishTitle'],'\n',row['seriesId'],'\n',row['firstObservation'] )
    file= 'bcch_' + row['Código'] + '.csv'
    
    # transformacion fecha 
    new_date = str(row['firstdate']).replace(" 00:00:00","")
    
    date_posted = row['firstdate']

    dfy = call_data(row['Código'], 
                    new_date.replace(" 00:00:00",""),  
                    str(hoy.strftime('%Y-%m-%d %H:%M:%S')).replace(" 00:00:00", ""))
    dfy.to_csv(file)

