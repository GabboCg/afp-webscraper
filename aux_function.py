# -*- coding: utf-8 -*-
"""
Created on Thu May 16 22:33:02 2019

@author: COJ
"""
import pandas as pd
import datetime as dt
from zeep import Client

def date_form(fecha_str):
    
    """ 
    
    input:   '04-02-2019' d-m-Y
    output: '2019-02-04'  Y-m-d
    para la api anti-intuitiva del bcch...
    
    """
    
    return dt.date(int(fecha_str[-4:]), 
                   int(fecha_str[3:5]), 
                   int(fecha_str[0:2]))

def call_data(seriesId, firstdate, lastdate):
    
    """ CONSULTA API BCCH, DESCARGA DATA TONTAMENTE --> FUERZA BRUTA
    
    seriesId = 'F029.FS.STO.80.D'
    firstdate = '03-02-2019'   # dia, mes, año
    lastdate = '02-03-2019'     
    
    """
    
    client = Client('https://si3.bcentral.cl/SieteWS/sietews.asmx?wsdl')
    user ='150985854'
    passw ='kS5NUeUYJ09J8Vf'
    
#    #re formatea la fecha para la API # año, mes, dia 
#    firstdate= date_form(firstdate)
#    lastdate= date_form(lastdate)
    
    # call API
    respuesta= client.service.GetSeries(user, 
                                        passw,
                                        firstdate,
                                        lastdate, 
                                        [{"string": seriesId}]) 
    
    """ STORE DATA BCCH EN DICCIONARIO """
    d={}
    for serie in respuesta.Series.fameSeries:
        for obs in serie.obs:
            d[obs.indexDateString] = obs.value

    """ TRANSFORMA DICCIONARIO A DATAFRAME """
    seriesId = respuesta.Series.fameSeries[0].header
    
    if len(d) == 1:
        return pd.DataFrame.from_dict(d,
                                      orient='index',
                                      columns=[seriesId])
        
    else:
        df= pd.DataFrame.from_dict(d,
                                   orient='index',
                                   columns=[seriesId]).squeeze()
        return df.dropna()

