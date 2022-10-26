# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 13/10/2022 11:30 am
# Última modificación: 26/10/2022 04:40 pm
# Versión: 3.10.8

# Importar libreías
from bs4 import BeautifulSoup
import requests
from random import *

# 1. Función importar 
"""
Faltan comentarios
Falta validaciones (se espera hasta tener todo listo para 
pensar cómo hacerla la GUI de tkinter)

"""
def retornarHtml(pLink):
    peticion = requests.get(pLink).text
    codHtml = BeautifulSoup(peticion, 'lxml')
    return codHtml

def obtieneAnno(pStringAnno):
    annoDigitos = ""
    for caracter in pStringAnno:
        if not caracter.isdigit():
            break
        annoDigitos += caracter
    return annoDigitos

def importarAstronomos():
    llavesAstro = []
    valoresAstro = []
    htmlAstro = retornarHtml('https://atlasdeastronomia.com/astronomos/')
    astronomos = htmlAstro.find_all('div', class_="articlebox")
    for persona in astronomos:
        nombre = persona.find('h2', class_="articletitle").text
        datosNacimientoAstro = persona.find('strong', style="font-size: small").text.split(",")
        if "-" in datosNacimientoAstro[1]:
            nacimientoFecha = tuple(datosNacimientoAstro[1].replace(" ", "").split("-"))
        else:
            nacimientoFecha = (datosNacimientoAstro[1].replace(" ", ""), "")
        linkDescrip = persona.find('a')['href']
        htmlDescrip = retornarHtml(linkDescrip)
        descripAstro = htmlDescrip.find('p').text.replace("\r", " ").replace("\n", " ")
        llavesAstro.append(nombre[0] + obtieneAnno(nacimientoFecha[0]))
        valoresAstro.append([nombre, datosNacimientoAstro[0], nacimientoFecha, descripAstro])
    return llavesAstro, valoresAstro

def crearDiccAstronomos(cantAstros): # 1 <= cantAstros <= 50
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
diccAstro = crearDiccAstronomos(49)
for indice, llave in enumerate(diccAstro):
    print(indice+1, llave, "\n")