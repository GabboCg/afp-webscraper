# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:07:34 2020

@author: Habac
"""

import os
import time
import camelot
import pandas as pd 

#%%
'''::::::::::::::::::::::::: Preliminares ::::::::::::::::::::::::::::::::::'''

CWD = os.getcwd()

fecha_informe = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 
                 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 
                 'diciembre']

year_informe = [2010, 2011, 2012, 2013, 2014, 
                2015, 2016, 2017, 2018, 2019, 
                2020]

page_table = [8, 8, 11, 11, 11, 11, 11, 15, 15, 15, 15]

tables_finale = []

os.chdir(os.path.join(CWD, "informes"))

#%%
'''::::::::::::::::::::::: Extraccion tablas pdfs :::::::::::::::::::::::::::'''

for i in range(11):
    for j in range(len(fecha_informe)):     
        print("Leyendo informe de "+fecha_informe[j]+" del "+str(year_informe[i])+"...")
        if year_informe[i] == 2019: 
            tables = camelot.read_pdf("informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf", flavor='stream', pages=str(page_table[i])) 
            pdf = tables[0].df
            tables_finale.append(pdf)
        elif year_informe[i] == 2020: 
            if (fecha_informe[j] == "abril"):
                break
            else:
                tables = camelot.read_pdf("informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf", flavor='stream', pages=str(page_table[i])) 
                pdf = tables[0].df
                tables_finale.append(pdf)
        else:
            if ((year_informe[i] == 2011) & (fecha_informe[j] == 'noviembre') | (year_informe[i] == 2011) & (fecha_informe[j] == 'diciembre')):
                tables = camelot.read_pdf("informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf", flavor='stream', pages="10")
                pdf = tables[0].df

                tables_finale.append(pdf)
            elif ((year_informe[i] == 2012) & (fecha_informe[j] == 'octubre') | (year_informe[i] == 2014) & (fecha_informe[j] == 'octubre')):
                tables = camelot.read_pdf("informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf", flavor='stream', pages="12")
                pdf = tables[0].df
                tables_finale.append(pdf)
            elif ((year_informe[i] == 2017) & (fecha_informe[j] == 'enero')):
                tables = camelot.read_pdf("informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf", flavor='stream', pages="11")
                pdf = tables[0].df
                tables_finale.append(pdf)
            else:
                tables = camelot.read_pdf("informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf", flavor='stream', pages=str(page_table[i]))
                pdf = tables[0].df
                tables_finale.append(pdf)
                
#%%
'''::::::::::::::::::::::::::: Tablas a DF :::::::::::::::::::::::::::::::::'''

def pdf_clean(df, row, col, index_col):
    index_df = df.iloc[row:,index_col]
    df = df.iloc[row:,col]
    df.index = index_df
    df = df.loc[~df.index.duplicated(keep='first')]
    df.columns = ["A", "B", "C", "D", "E"]   
    df = df.loc[:"TOTAL ACTIVOS",:]
    
    if len(df) == 22 or len(df) == 24:
        df = df.iloc[1:,:]
        
    return(df)
   
clean_tables = []   
    
for i in range(len(tables_finale)):
    if i in list(range(85,103)):
        informe_df = pdf_clean(tables_finale[i], 2, [1, 3, 5, 7, 9], 0)
        clean_tables.append(informe_df)
    elif i == 103:
        nforme_df = pdf_clean(tables_finale[i], 2, [1, 3, 4, 6, 8], 0)
        clean_tables.append(informe_df)
    elif i in list(range(4,6)):
        informe_df = pdf_clean(tables_finale[i], 2, [2, 4, 6, 8, 10], 1)
        clean_tables.append(informe_df)
    else:
        informe_df = pdf_clean(tables_finale[i], 4, [1, 3, 5, 7, 9], 0)
        clean_tables.append(informe_df)

float_tables = []   

for df in range(len(clean_tables)):
    print(df)
    afp_df = clean_tables[df].copy()
    m, n = afp_df.shape        
    for i in range(m):
        for j in range(n):
            if afp_df.iloc[i,j] == '-' or afp_df.iloc[i,j] == '‐':
                afp_df.iloc[i,j] = afp_df.iloc[i,j].replace('-', 'NaN').replace('‐', 'NaN')
            else:
                afp_df.iloc[i,j] = afp_df.iloc[i,j].replace(' ','').replace('.','').replace(',','.')
                afp_df.iloc[i,j] = afp_df.iloc[i,j].replace('100.0%','')
                afp_df.iloc[i,j] = afp_df.iloc[i,j].replace('‐','-')
                afp_df.iloc[i,j] = afp_df.iloc[i,j].split("\n")[0]
                
    for i in range(n):
        afp_df.iloc[:,i] = afp_df.iloc[:,i].astype(float)
    
    float_tables.append(afp_df)
    
#%%
import locale

index_match = list(float_tables[0].index)

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
dates = pd.date_range('2010-01-01','2020-03-01', freq='MS').strftime("%Y-%m-%d")

fondo_A_df = pd.DataFrame(columns = index_match)
fondo_B_df = pd.DataFrame(columns = index_match)
fondo_C_df = pd.DataFrame(columns = index_match)
fondo_D_df = pd.DataFrame(columns = index_match)
fondo_E_df = pd.DataFrame(columns = index_match)

afp_datos_informe = [fondo_A_df, fondo_B_df, fondo_C_df, fondo_D_df, fondo_E_df]

for t in range(len(afp_datos_informe)):
    for ite, df in enumerate(float_tables):
        afp_df = df.loc[index_match,:]
        afp_df = df.iloc[:, t]
        afp_datos_informe[t] = afp_datos_informe[t].append(afp_df)

afp_datos_informe = [k.set_index(dates) for k in afp_datos_informe]

#%%
writer = pd.ExcelWriter('datos_informe_enero_2010_marzo_2020.xlsx', engine='xlsxwriter')
sheet_name = ["Fondo A", "Fondo B", "Fondo C", "Fondo D", "Fondo E"]

for i, df in enumerate(afp_datos_informe):
    df.to_excel(writer, sheet_name=sheet_name[i])

writer.save()
