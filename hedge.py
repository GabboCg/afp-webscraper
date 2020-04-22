# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 18:20:43 2020

@author: Habac
"""
import os
import camelot
import pandas as pd 

root_dir = os.getcwd()

fecha_informe = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
year_informe = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
page_table = [8, 8, 11, 11, 11, 11, 11, 15, 15, 15, 15]
tables_finale = []

os.chdir(os.path.join(root_dir, "informes"))

for i in range(11):
    for j in range(len(fecha_informe)):       
        if year_informe[i] == 2019: 
            # extrae la tabla respectiva de la página 
            tables = camelot.read_pdf("informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf", flavor='stream', pages=str(page_table[i])) 
            # se extrae el dataframe
            pdf = tables[0].df
            # se agrega a la lista
            tables_finale.append(pdf)
        elif year_informe[i] == 2020: 
            if (fecha_informe[j] == "marzo"):
                break
            else:
                # extrae la tabla respectiva de la página 
                tables = camelot.read_pdf("informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf", flavor='stream', pages=str(page_table[i])) 
                # se extrae el dataframe
                pdf = tables[0].df
                # se agrega a la lista
                tables_finale.append(pdf)
        else:
            if ((year_informe[i] == 2011) & (fecha_informe[j] == 'noviembre') | (year_informe[i] == 2011) & (fecha_informe[j] == 'diciembre')):
                # extrae la tabla respectiva de la página 
                tables = camelot.read_pdf("informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf", flavor='stream', pages="10")
                # se extrae el dataframe
                pdf = tables[0].df
                # se agrega a la lista
                tables_finale.append(pdf)
            elif ((year_informe[i] == 2012) & (fecha_informe[j] == 'octubre') | (year_informe[i] == 2014) & (fecha_informe[j] == 'octubre')):
                # extrae la tabla respectiva de la página 
                tables = camelot.read_pdf("informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf", flavor='stream', pages="12")
                # se extrae el dataframe
                pdf = tables[0].df
                # se agrega a la lista
                tables_finale.append(pdf)
            elif ((year_informe[i] == 2017) & (fecha_informe[j] == 'enero')):
                # extrae la tabla respectiva de la página 
                tables = camelot.read_pdf("informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf", flavor='stream', pages="11")
                # se extrae el dataframe
                pdf = tables[0].df
                # se agrega a la lista
                tables_finale.append(pdf)
            else:
                # extrae la tabla respectiva de la página 
                tables = camelot.read_pdf("informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf", flavor='stream', pages=str(page_table[i]))
                # se extrae el dataframe
                pdf = tables[0].df
                # se agrega a la lista
                tables_finale.append(pdf)

#%%
''' Tablas a DataFrame '''                

import numpy as np
import locale

os.chdir(root_dir)

# np.save('tablas_afp_until_2020.npy', tables_finale)    
# tables = np.load("tablas_apf_until_2020.npy", allow_pickle=True)    

tables = tables_finale

# total activos A
total_activos_A = []

for i in range(len(tables)):
    afp_rendimiento = pd.DataFrame(tables[i])
    m, n = afp_rendimiento.shape
    
    if n <= 13:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[0] == 'TOTAL ACTIVOS'].iloc[0,:]
        tot_activos_A  = afp_rendimiento.iloc[1,]
        total_activos_A.append(tot_activos_A)
    
    elif n == 14:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[1] == 'TOTAL ACTIVOS'].iloc[0,:]
        tot_activos_A  = afp_rendimiento.iloc[2,]
        total_activos_A.append(tot_activos_A)

# total activos B
total_activos_B = []

for i in range(len(tables)):
    afp_rendimiento = pd.DataFrame(tables[i])
    m, n = afp_rendimiento.shape
    
    if i == 103:    
        afp_rendimiento = afp_rendimiento[afp_rendimiento[0] == 'TOTAL ACTIVOS'].iloc[0,:]
        tot_activos_B = afp_rendimiento.iloc[3,]
        tot_activos_B = str(tot_activos_B).replace("\n100%", "")
        total_activos_B.append(tot_activos_B)
    
    elif n <= 13:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[0] == 'TOTAL ACTIVOS'].iloc[0,:]
        tot_activos_B  = afp_rendimiento.iloc[3,]
        total_activos_B.append(tot_activos_B)
    
    elif n == 14:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[1] == 'TOTAL ACTIVOS'].iloc[0,:]
        tot_activos_B = afp_rendimiento.iloc[4,]
        total_activos_B.append(tot_activos_B)
    
# total activos D
total_activos_D = []

for i in range(len(tables)):
    afp_rendimiento = pd.DataFrame(tables[i])
    m, n = afp_rendimiento.shape
    
    if (i == 14 and n ==13):
        afp_rendimiento = afp_rendimiento[afp_rendimiento[0] == 'TOTAL ACTIVOS'].iloc[:,7] 
        tot_activos_D  = afp_rendimiento.iloc[1,]
        total_activos_D.append(tot_activos_D)
    
    elif n == 13:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[0] == 'TOTAL ACTIVOS'].iloc[:,7]
        tot_activos_D  = afp_rendimiento.iloc[0,]
        total_activos_D.append(tot_activos_D)
            
    elif n == 12:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[0] == 'TOTAL ACTIVOS'].iloc[:,6]
        tot_activos_D = afp_rendimiento.iloc[0,]
        total_activos_D.append(tot_activos_D)
    
    elif n == 14:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[1] == 'TOTAL ACTIVOS'].iloc[:,8]
        tot_activos_D  = afp_rendimiento.iloc[0,]
        total_activos_D.append(tot_activos_D)
        
# total activos E
total_activos_E = []

for i in range(len(tables)):
    afp_rendimiento = pd.DataFrame(tables[i])
    m, n = afp_rendimiento.shape
    
    if n == 13:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[0] == 'TOTAL ACTIVOS'].iloc[:,9]
        tot_activos_E  = afp_rendimiento.iloc[0,]
        total_activos_E.append(tot_activos_E)
    
    elif n == 12:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[0] == 'TOTAL ACTIVOS'].iloc[:,8]
        tot_activos_E  = afp_rendimiento.iloc[0,]
        total_activos_E.append(tot_activos_E)
    
    elif n == 14:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[1] == 'TOTAL ACTIVOS'].iloc[:,10]
        tot_activos_E  = afp_rendimiento.iloc[0,]
        total_activos_E.append(tot_activos_E)

indicadores_afp = pd.concat([pd.DataFrame(total_activos_A), pd.DataFrame(total_activos_B), 
                             pd.DataFrame(total_activos_D), pd.DataFrame(total_activos_E)], axis = 1)

indicadores_afp.columns = ['A', 'B', 'D', 'E']    

for i in range(4):
    indicadores_afp.iloc[:,i] = indicadores_afp.iloc[:,i].str.replace('.','').str.replace(',','.').astype(float)

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
dates = pd.date_range('2010-01-01','2020-02-01', freq='MS').strftime("%Y-%m-%d")

indicadores_afp.index = dates

indicadores_afp['total_AUM'] = indicadores_afp['A'] + indicadores_afp['B'] + indicadores_afp['D'] + indicadores_afp['E'] 
indicadores_afp['A_plus_B'] = indicadores_afp['A'] + indicadores_afp['B']
indicadores_afp['D_plus_E'] = indicadores_afp['D'] + indicadores_afp['E']

total_return_index = indicadores_afp.loc[:,['A_plus_B', 'D_plus_E']]

total_return_index['ret_A_plus_B'] = (total_return_index['A_plus_B'])/total_return_index['A_plus_B'].shift(1)
total_return_index['ret_A_plus_B'] = total_return_index['ret_A_plus_B']*total_return_index['ret_A_plus_B'].shift(1) 
total_return_index['ret_D_plus_E'] = (total_return_index['D_plus_E'])/total_return_index['D_plus_E'].shift(1)
total_return_index['ret_D_plus_E'] = total_return_index['ret_D_plus_E']*total_return_index['ret_D_plus_E'].shift(1) 

total_return_index = total_return_index[total_return_index.index > "2012-12-01"]

base_a_plus_b = float(total_return_index[total_return_index.index ==  "2013-01-01"]['ret_A_plus_B'])
base_d_plus_e = float(total_return_index[total_return_index.index ==  "2013-01-01"]['ret_D_plus_E'])

total_return_index['ret_A_plus_B_base'] = (total_return_index['ret_A_plus_B']/base_a_plus_b)*100
total_return_index['ret_D_plus_E_base'] = (total_return_index['ret_D_plus_E']/base_d_plus_e)*100

total_return_index = total_return_index.loc[:,["ret_A_plus_B_base", "ret_D_plus_E_base"]]
total_return_index = total_return_index[total_return_index.index >= "2019-01-01"]
total_return_index.plot()

indicadores_afp = indicadores_afp[indicadores_afp.index >= "2019-01-01"]
indicadores_afp['relative_size'] = ((indicadores_afp['D_plus_E'] - indicadores_afp['A_plus_B']) / indicadores_afp['total_AUM']) * 100 
indicadores_afp['relative_size'].plot()

#%%
output_df = pd.concat([total_return_index, indicadores_afp.loc[:,['relative_size']]], axis = 1)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('plots_afp.xlsx', engine='xlsxwriter')

output_df.loc[:,["ret_A_plus_B_base", "ret_D_plus_E_base"]].to_excel(writer, sheet_name='relative_size')
output_df.loc[:,["relative_size"]].to_excel(writer, sheet_name='total_returns_index')

writer.save()
