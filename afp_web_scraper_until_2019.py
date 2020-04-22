# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 01:06:50 2019

@author: Habac
"""

import os
import time
import camelot
from glob import glob
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

root_dir = os.getcwd()

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": root_dir + '\\informes',
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    }
)

# preliminares para el css selector
id_informe = [5918, 5917, 5916, 6502, 9472, 9517, 9533, 9562, 10127, 10257]
fecha_informe = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
path_id_b = [2,1,2,1,2,1,2,1,2,1,2,1] # ultimo 1 por estar solo un mes
path_id_a = [6,6,5,5,4,4,3,3,2,2,1,1] # ultimo 1 por estar solo un mes
year_informe = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
page_table = [8, 8, 11, 11, 11, 11, 11, 15, 15, 15]
tables_finale = []

for i in range(len(id_informe)):
    # webdriver usando chrome
    driver = webdriver.Chrome(executable_path = root_dir + "\\chromedriver.exe", options=chrome_options)
    # se obtiene el link en el webdriver
    driver.get("https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-10089.html#recuadrosxAno_group_pvid_" + str(id_informe[i]))
               
    for j in range(len(fecha_informe)):
        try:            
            if year_informe[i] == 2019: 
                # "truco" cuando el elemento presenta w3
                driver.execute_script("window.scrollTo(1000, 0);")
                # click sobre el css selector del pdf 
                driver.find_element_by_css_selector('#recuadrosxAno_group_pvid_' + str(id_informe[i]) + ' > div:nth-child(' + str(path_id_a[j]) + ') > div:nth-child(' + str(path_id_b[j]) + ') > div.media-body > h3 > a').click()
                # permite "dormir" por 5 segundos
                time.sleep(2)
                # click sobre el xpath del pdf 
                driver.find_element_by_xpath('//*[@id="article_i__SP_ar_articulo_portada_publicacion_1"]/div[1]').click()
                # se vuelve al inicio
                driver.back()
                # se cambia el directo a la carpeta de informes 
                os.chdir(root_dir + '\\informes')
                # se vuelve al inicio
                time.sleep(2)
                # se busca el archivo pdf cuyo nombre parte con 'artilces*'
                last_file = glob('articles*')
                # se renombra el informe seleccionado por last_file con el mes y año
                os.rename(last_file[0], "informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf")
                # extrae la tabla respectiva de la página 
                tables = camelot.read_pdf("informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf", flavor='stream', pages=str(page_table[i])) 
                # se extrae el dataframe
                pdf = tables[0].df
                # se agrega a la lista
                tables_finale.append(pdf)
                # se vuelve al directorio de origen
                os.chdir(root_dir)
             
            else:
                # "truco" cuando el elemento presenta w3
                driver.execute_script("window.scrollTo(1000, 0);")
                # click sobre el css selector del pdf 
                driver.find_element_by_css_selector('#recuadrosxAno_group_pvid_' + str(id_informe[i]) + ' > div:nth-child(' + str(path_id_a[j]) + ') > div:nth-child(' + str(path_id_b[j]) + ') > div.media-body > h3 > a').click()
                # permite "dormir" por 5 segundos
                time.sleep(2)
                # click sobre el xpath del pdf 
                driver.find_element_by_xpath('//*[@id="article_i__SP_ar_articulo_portada_publicacion_1"]/div[1]').click()
                # se vuelve al inicio
                driver.back()
                # se cambia el directo a la carpeta de informes 
                os.chdir(root_dir + '\\informes')
                # se vuelve al inicio
                time.sleep(2)
                
                if ((year_informe[i] == 2011) & (fecha_informe[j] == 'noviembre') | (year_informe[i] == 2011) & (fecha_informe[j] == 'diciembre')):
                    # se busca el archivo pdf cuyo nombre parte con 'artilces*'
                    last_file = glob('articles*')
                    # se renombra el informe seleccionado por last_file con el mes y año
                    os.rename(last_file[0], "informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf")
                    # extrae la tabla respectiva de la página 
                    tables = camelot.read_pdf("informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf", flavor='stream', pages="10")
                    # se extrae el dataframe
                    pdf = tables[0].df
                    # se agrega a la lista
                    tables_finale.append(pdf)
                    # se vuelve al directorio de origen
                    os.chdir(root_dir)
                    
                elif ((year_informe[i] == 2012) & (fecha_informe[j] == 'octubre') | (year_informe[i] == 2014) & (fecha_informe[j] == 'octubre')):
                    # se busca el archivo pdf cuyo nombre parte con 'artilces*'
                    last_file = glob('articles*')
                    # se renombra el informe seleccionado por last_file con el mes y año
                    os.rename(last_file[0], "informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf")
                    # extrae la tabla respectiva de la página 
                    tables = camelot.read_pdf("informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf", flavor='stream', pages="12")
                    # se extrae el dataframe
                    pdf = tables[0].df
                    # se agrega a la lista
                    tables_finale.append(pdf)
                    # se vuelve al directorio de origen
                    os.chdir(root_dir)
              
                elif ((year_informe[i] == 2017) & (fecha_informe[j] == 'enero')):
                    # se busca el archivo pdf cuyo nombre parte con 'artilces*'
                    last_file = glob('articles*')
                    # se renombra el informe seleccionado por last_file con el mes y año
                    os.rename(last_file[0], "informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf")
                    # extrae la tabla respectiva de la página 
                    tables = camelot.read_pdf("informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf", flavor='stream', pages="11")
                    # se extrae el dataframe
                    pdf = tables[0].df
                    # se agrega a la lista
                    tables_finale.append(pdf)
                    # se vuelve al directorio de origen
                    os.chdir(root_dir)
                
                else:
                    # se busca el archivo pdf cuyo nombre parte con 'artilces*'
                    last_file = glob('articles*')
                    # se renombra el informe seleccionado por last_file con el mes y año
                    os.rename(last_file[0], "informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf")
                    # extrae la tabla respectiva de la página 
                    tables = camelot.read_pdf("informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf", flavor='stream', pages=str(page_table[i]))
                    # se extrae el dataframe
                    pdf = tables[0].df
                    # se agrega a la lista
                    tables_finale.append(pdf)
                    # se vuelve al directorio de origen
                    os.chdir(root_dir)
            
        except:
            print("Informe de " + fecha_informe[j] + " " + str(year_informe[i]) + ".pdf no existe")
            
    # cierra el webdriver
    driver.close()

#%%
''' Construyendo las series ''' 

import numpy as np
import pandas as pd 
import locale

np.save('tablas_apf_until_2019.npy', tables_finale)    
tables = np.load('tablas_apf_until_2019.npy', allow_pickle=True)    

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
    
# Renta Variable internacional A
renta_variable_A = []

for i in range(len(tables)):
    afp_rendimiento = pd.DataFrame(tables[i])
    m, n = afp_rendimiento.shape
    
    if n <= 13:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[0] == 'RENTA VARIABLE'].iloc[1,:]
        ret_var_A = afp_rendimiento.iloc[1,]
        renta_variable_A.append(ret_var_A)
    
    elif (i == 4) | (i == 5):
        afp_rendimiento = afp_rendimiento[afp_rendimiento[1] == 'RENTA VARIABLE'].iloc[1,:]
        ret_var_A = afp_rendimiento.iloc[2,]
        renta_variable_A.append(ret_var_A)
    
    elif n == 14:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[1] == 'RENTA VARIABLE'].iloc[1,:]
        ret_var_A = afp_rendimiento.iloc[1,]
        renta_variable_A.append(ret_var_A)
        
# Renta Variable internacional E
renta_variable_E = []

for i in range(len(tables)):
    afp_rendimiento = pd.DataFrame(tables[i])
    m, n = afp_rendimiento.shape
    
    if n == 13:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[0] == 'RENTA VARIABLE'].iloc[1,:]
        ret_var_E = afp_rendimiento.iloc[9,]
        renta_variable_E.append(ret_var_E)
        
    elif n == 12:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[0] == 'RENTA VARIABLE'].iloc[1,:]
        ret_var_E = afp_rendimiento.iloc[8,]
        renta_variable_E.append(ret_var_E)
    
    elif (i == 4) | (i == 5):
        afp_rendimiento = afp_rendimiento[afp_rendimiento[1] == 'RENTA VARIABLE'].iloc[1,:]
        ret_var_E = afp_rendimiento.iloc[10,]
        renta_variable_E.append(ret_var_E)
    
    elif n == 14:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[1] == 'RENTA VARIABLE'].iloc[1,:]
        ret_var_E = afp_rendimiento.iloc[9,]
        renta_variable_E.append(ret_var_E)
        
# Renta fija internacional A
renta_fija_A = []

for i in range(len(tables)):
    afp_rendimiento = pd.DataFrame(tables[i])
    m, n = afp_rendimiento.shape
    
    if n <= 13:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[0] == 'RENTA FIJA'].iloc[1,:]
        ret_fija_A = afp_rendimiento.iloc[1,]
        renta_fija_A.append(ret_fija_A)
    
    elif (i == 4) | (i == 5):
        afp_rendimiento = afp_rendimiento[afp_rendimiento[1] == 'RENTA FIJA'].iloc[1,:]
        ret_fija_A = afp_rendimiento.iloc[2,]
        renta_fija_A.append(ret_fija_A)
    
    elif n == 14:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[1] == 'RENTA FIJA'].iloc[1,:]
        ret_fija_A = afp_rendimiento.iloc[1,]
        renta_fija_A.append(ret_fija_A)

# Renta fija internacional E
renta_fija_E = []

for i in range(len(tables)):
    afp_rendimiento = pd.DataFrame(tables[i])
    m, n = afp_rendimiento.shape
    
    if n == 13:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[0] == 'RENTA FIJA'].iloc[1,:]
        ret_fija_E = afp_rendimiento.iloc[9,]
        renta_fija_E.append(ret_fija_E)
        
    elif n == 12:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[0] == 'RENTA FIJA'].iloc[1,:]
        ret_fija_E = afp_rendimiento.iloc[8,]
        renta_fija_E.append(ret_fija_E)
    
    elif (i == 4) | (i == 5):
        afp_rendimiento = afp_rendimiento[afp_rendimiento[1] == 'RENTA FIJA'].iloc[1,:]
        ret_fija_E = afp_rendimiento.iloc[10,]
        renta_fija_E.append(ret_fija_E)
    
    elif n == 14:
        afp_rendimiento = afp_rendimiento[afp_rendimiento[1] == 'RENTA FIJA'].iloc[1,:]
        ret_fija_E = afp_rendimiento.iloc[9,]
        renta_fija_E.append(ret_fija_E)

#%%
''' construccion DataFrame '''

indicadores_afp = pd.concat([pd.DataFrame(total_activos_A), pd.DataFrame(total_activos_E), 
                             pd.DataFrame(renta_variable_A), pd.DataFrame(renta_variable_E),
                             pd.DataFrame(renta_fija_A), pd.DataFrame(renta_fija_E)], axis = 1)
    
indicadores_afp.columns = ['renta A', 'renta E', 'int var A', 'int var E', 'rf A', 'rf E']
    
for i in range(6):
    indicadores_afp.iloc[:,i] = indicadores_afp.iloc[:,i].str.replace('.','').str.replace(',','.').astype(float)
    
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
dates = pd.date_range('2010-01-01','2019-12-01', freq='MS').strftime("%Y-%m-%d %H:%M:%S")

indicadores_afp.index = dates

# dolar observado
dolar_obs = pd.read_csv('bcch_F073.TCO.PRE.Z.D.csv',
                        names = ['fecha', 'dolar_observado'],
                        index_col = 0)

dolar_obs.index = pd.to_datetime(dolar_obs.index, format='%d-%m-%Y')
dolar_obs['month'] = dolar_obs.index.month
dolar_obs['year'] = dolar_obs.index.year

dolar_obs_monthly = dolar_obs.loc[:,['dolar_observado','year', 'month']].groupby(['year', 'month'])['dolar_observado'].mean().reset_index()
dolar_obs_monthly.index = (pd.to_datetime(dolar_obs_monthly.assign(Day=1).
                                          loc[:, ['Day', 'month', 'year']]).
                                          dt.strftime('%d-%m-%Y'))
dolar_obs_monthly.index =  pd.to_datetime(dolar_obs_monthly.index, format='%d-%m-%Y')
dolar_obs_monthly = dolar_obs_monthly[dolar_obs_monthly.index >= '2010-01-01 00:00:00']

# union de dolar con la base 
indicadores_afp = pd.merge(indicadores_afp, dolar_obs_monthly, left_index=True, right_index=True)

# construccion variables
indicadores_afp['ratio A dolar'] = (indicadores_afp['renta A'] / indicadores_afp['dolar_observado']) * 1000000
indicadores_afp['ratio E dolar'] = (indicadores_afp['renta E'] / indicadores_afp['dolar_observado']) * 1000000
indicadores_afp['ratio A/E'] = indicadores_afp['renta A'] / indicadores_afp['renta E']
indicadores_afp['renta int/A'] = indicadores_afp['int var A'] / indicadores_afp['renta A']
indicadores_afp['renta int/E'] = indicadores_afp['int var E'] / indicadores_afp['renta E']
indicadores_afp['rf/A'] = indicadores_afp['rf A'] / indicadores_afp['renta A']
indicadores_afp['rf/E'] = indicadores_afp['rf E'] / indicadores_afp['renta E']

indicadores_afp.to_excel('indicadores_afp_until_2019.xlsx')
