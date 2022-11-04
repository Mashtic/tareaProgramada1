# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 13/10/2022 11:30 am
# Última modificación: 03/11/2022 02:20 pm
# Versión: 3.10.8

# Importar libreías
from bs4 import BeautifulSoup
import requests
from random import *

# 1. Función importar 
def retornarHtml(pLink):
    """
    Funcionalidad: se obtiene el código HTML de la página
    Entradas: pLink (str)
    Salidas: codHtml (bs4.BeautifulSoup)
    """
    peticion = requests.get(pLink).text
    codHtml = BeautifulSoup(peticion, 'lxml')
    return codHtml

def obtieneAnno(pStringAnno):
    """
    Funcionalidad: obtiene solamente los número hasta encontrar
                   algo diferente
    Entradas: pStringAnno (str)
    Salidas: annoDigitos (str)
    """
    annoDigitos = ""
    for caracter in pStringAnno:
        if not caracter.isdigit(): # Para parar cuando se 
                                   # encuentra a. C. por ej 
            break
        annoDigitos += caracter
    return annoDigitos

def importarAstronomos():
    """
    Funcionalidad: crea dos listas, una con los datos de los astrónomos
                   y otra con los códigos. Los 50 son extraídos 
    Entradas: N/A
    Salidas: llavesAstro (list)
             valoresAstro (list)
    """
    llavesAstro = []
    valoresAstro = []
    htmlAstro = retornarHtml('https://atlasdeastronomia.com/astronomos/')
    astronomos = htmlAstro.find_all('div', class_="articlebox")
    for persona in astronomos:
        nombre = persona.find('h2', class_="articletitle").text
        datosNacimientoAstro = persona.find('strong', style="font-size: small").text.split(",") # Separa en lista
        if "-" in datosNacimientoAstro[1]: # Si tiene dos fechas
            nacimientoFecha = tuple(datosNacimientoAstro[1].replace(" ", "").split("-")) # Lo separa en tupla
        else:
            nacimientoFecha = (datosNacimientoAstro[1].replace(" ", ""), "")
        linkDescrip = persona.find('a')['href']
        htmlDescrip = retornarHtml(linkDescrip)
        descripAstro = htmlDescrip.find('p').text.replace("\r", " ").replace("\n", " ").replace("\u200b", "") # Para limipiar info
        llavesAstro.append(nombre[0] + obtieneAnno(nacimientoFecha[0]))
        valoresAstro.append([nombre, datosNacimientoAstro[0], nacimientoFecha, descripAstro]) # Añade los datos a las listas
    return llavesAstro, valoresAstro

def crearDiccAstronomos(cantAstros):
    """
    Funcionalidad: crea un diccionario con la cantidad de astrónomos
                   requerida y en diferente orden que la página
    Entradas: cantAstros (int): 1 <= cantAstros <= 50
    Salidas: diccAstros (dict)
    """
    numAstro = 1
    diccAstros = {}
    llavesAstro, valoresAstro = importarAstronomos()
    while cantAstros >= numAstro:
        posAstro = randint(0, len(llavesAstro)-1)
        diccAstros[llavesAstro[posAstro]] = valoresAstro[posAstro]
        llavesAstro.pop(posAstro)
        valoresAstro.pop(posAstro)
        numAstro += 1
    return diccAstros

# Para comprobar que sirve (solo imprime llaves)
diccAstro = crearDiccAstronomos(10)
print(diccAstro)