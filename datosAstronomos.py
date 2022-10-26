# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 13/10/2022 11:30 am
# Última modificación: 26/10/2022 03:43 pm
# Versión: 3.10.8

# Importar libreías
from bs4 import BeautifulSoup
import requests

# 1. Función importar astrónomos
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

def importarAstronomos(astroTotales):
    numAstro = 1
    diccAstros = {}
    htmlAstro = retornarHtml('https://atlasdeastronomia.com/astronomos/')
    astronomos = htmlAstro.find_all('div', class_="articlebox")
    for persona in astronomos:
        if astroTotales < numAstro:
            break
        nombre = persona.find('h2', class_="articletitle").text
        datosNacimientoAstro = persona.find('strong', style="font-size: small").text.split(",")
        if "-" in datosNacimientoAstro[1]:
            nacimientoFecha = tuple(datosNacimientoAstro[1].replace(" ", "").split("-"))
        else:
            nacimientoFecha = (datosNacimientoAstro[1].replace(" ", ""), "")
        linkDescrip = persona.find('a')['href']
        htmlDescrip = retornarHtml(linkDescrip)
        descripAstro = htmlDescrip.find('p').text.replace("\r", " ").replace("\n", " ")
        diccAstros[nombre[0] + obtieneAnno(nacimientoFecha[0])] = [nombre, 
        datosNacimientoAstro[0], nacimientoFecha, descripAstro]
        numAstro += 1
    return diccAstros

# Para comprobar que sirve

diccAstros = importarAstronomos(10)
print(diccAstros)
