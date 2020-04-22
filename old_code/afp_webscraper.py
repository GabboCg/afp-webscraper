#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:54:19 2019

@author: gabriel
"""

import os
import time
import camelot
from glob import glob
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

root_dir = os.getcwd()

chrome_options = Options()
chrome_options.add_experimental_option('prefs',  {
    "download.default_directory": root_dir + '\\informes',
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    }
)

# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

id_informe = [5918, 5917, 5916, 6502, 9472, 9517, 9533, 9562, 10127, 10257]
fecha_informe = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
year_informe = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

''' Informes desde 2010 hasta 2016 '''

for i in range(len(year_informe)):
    # webdriver usando chrome
    driver = webdriver.Chrome(executable_path = root_dir + "\\chromedriver.exe", options=chrome_options)
    # se obtiene el link en el webdriver
    driver.get("https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-10089.html#recuadrosxAno_group_pvid_" + str(id_informe[i]))
    
    if year_informe[i] >= 2014:
        for j in range(len(fecha_informe)):
            # "truco" cuando el elemento presenta w3
            driver.execute_script("window.scrollTo(1000, 0);")
            # click al nombre del informe 
            driver.find_element_by_link_text("Inversiones y rentabilidad de los Fondos de Pensiones a " + fecha_informe[j] +  " " +  str(year_informe[i])).click()
            # permite "dormir" por 5 segundos
            # handles = driver.window_handles 
            # driver.switch_to.window(handles[1])
            time.sleep(5)
            # click sobre el xpath del pdf 
            driver.find_element_by_xpath('//*[@id="article_i__SP_ar_articulo_portada_publicacion_1"]/div[1]/a/img').click()
            # se vuelve al inicio
            driver.back()
            # se cambia el directo a la carpeta de informes 
            os.chdir(root_dir + '\\informes')
            # se vuelve al inicio
            time.sleep(5)
            # se busca el archivo pdf cuyo nombre parte con 'artilces*'
            last_file = glob('articles*')
            # se renombra el informe seleccionado por last_file con el mes y año
            os.rename(last_file[0], "informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf")
            # se vuelve al directorio de origen
            os.chdir(root_dir)
                        
    else:
        for j in range(len(fecha_informe)):
            # "truco" cuando el elemento presenta w3
            driver.execute_script("window.scrollTo(1000, 0);")
            # click al nombre del informe 
            driver.find_element_by_link_text("Inversiones y rentabilidad de los Fondos de Pensiones a " + fecha_informe[j] +  " de " +  str(year_informe[i])).click()
            # permite "dormir" por 5 segundos
            time.sleep(5)
            # click sobre el xpath del pdf 
            driver.find_element_by_xpath('//*[@id="article_i__SP_ar_articulo_portada_publicacion_1"]/div[1]/a/img').click()
            # se vuelve al inicio
            driver.back()
            # se cambia el directo a la carpeta de informes 
            os.chdir(root_dir + '\\informes')
            # se vuelve al inicio
            time.sleep(5)
            # se busca el archivo pdf cuyo nombre parte con 'artilces*'
            last_file = glob('articles*')
            # se renombra el informe seleccionado por last_file con el mes y año
            os.rename(last_file[0], "informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf")
            # se vuelve al directorio de origen
            os.chdir(root_dir)
    # cierra el webdriver
    driver.close()

''' Informes desde 2017 hasta 2019 '''

id_informe = [5918, 5917, 5916, 6502, 9472, 9517, 9533, 9562, 10127, 10257]
fecha_informe = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
path_id_b = [2,1,2,1,2,1,2,1,2,1,2,1]
path_id_a = [6,6,5,5,4,4,3,3,2,2,1,1]
year_informe = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

for i in range(len(id_informe)):
    # webdriver usando chrome
    driver = webdriver.Chrome(executable_path = root_dir + "\\chromedriver.exe", options=chrome_options)
    # se obtiene el link en el webdriver
    driver.get("https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-10089.html#recuadrosxAno_group_pvid_" + str(id_informe[i]))
               
    for j in range(len(fecha_informe)):
        # click sobre el xpath del pdf 
        driver.find_element_by_css_selector('#recuadrosxAno_group_pvid_' + str(id_informe[i]) + ' > div:nth-child(' + str(path_id_a[j]) + ') > div:nth-child(' + str(path_id_b[j]) + ') > div.media-body > h3 > a').click()
        # permite "dormir" por 5 segundos
        time.sleep(5)
        # click sobre el xpath del pdf 
        driver.find_element_by_xpath('//*[@id="article_i__SP_ar_articulo_portada_publicacion_1"]/div[1]/a/img').click()
        # se vuelve al inicio
        driver.back()
        # se cambia el directo a la carpeta de informes 
        os.chdir(root_dir + '\\informes')
        # se vuelve al inicio
        time.sleep(5)
        # se busca el archivo pdf cuyo nombre parte con 'artilces*'
        last_file = glob('articles*')
        # se renombra el informe seleccionado por last_file con el mes y año
        os.rename(last_file[0], "informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf")
    # se vuelve al directorio de origen
    os.chdir(root_dir)

''' Uso de Camelot '''

page_table = []

tables = camelot.read_pdf("articles-13779_recurso_1.pdf", flavor='stream', pages='15') 
pdf = tables[0].df

      if ((fecha_informe[j] == 'enero') & (year_informe[i] == 2017)) | ((fecha_informe[j] == 'febrero') & (year_informe[i] == 2017)):
            # click sobre el xpath del pdf 
            driver.find_element_by_xpath('//*[@id="article_i__SP_ar_articulo_portada_publicacion_1"]/div[1]/a/img').click()
            # se vuelve al inicio
            driver.back()
            # se cambia el directo a la carpeta de informes 
            os.chdir(root_dir + '\\informes')
            # se vuelve al inicio
            time.sleep(5)
            # se busca el archivo pdf cuyo nombre parte con 'artilces*'
            last_file = glob('articles*')
            # se renombra el informe seleccionado por last_file con el mes y año
            os.rename(last_file[0], "informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf")
            # se vuelve al directorio de origen
            os.chdir(root_dir)
            
        else:
            # se cambia el directo a la carpeta de informes 
            os.chdir(root_dir + '\\informes')
            # se vuelve al inicio
            time.sleep(5)
            # se busca el archivo pdf cuyo nombre parte con 'artilces*'
            last_file = glob('articles*')
            # se renombra el informe seleccionado por last_file con el mes y año
            os.rename(last_file[0], "informe_" + fecha_informe[j] + "_" + str(year_informe[i]) + ".pdf")
            # se vuelve al directorio de origen
            os.chdir(root_dir)

#recuadrosxAno_group_pvid_9562 > div:nth-child(5) > div:nth-child(1) > div.media-body > h3 > a            
#recuadrosxAno_group_pvid_9562 > div:nth-child(5) > div:nth-child(2) > div.media-body > h3 > a            
#recuadrosxAno_group_pvid_9562 > div:nth-child(6) > div:nth-child(1) > div.media-body > h3 > a
#recuadrosxAno_group_pvid_9562 > div:nth-child(6) > div:nth-child(2) > div.media-body > h3 > a