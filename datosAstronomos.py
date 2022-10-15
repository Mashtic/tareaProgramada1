from bs4 import BeautifulSoup
import requests

htmlAstro = requests.get('https://atlasdeastronomia.com/astronomos/').text
htmlAstroUlt = BeautifulSoup(htmlAstro, 'lxml')
astronomos = htmlAstroUlt.find_all('div', class_="articlebox")
for indice, persona in enumerate(astronomos):
    nombre = persona.find('h2', class_="articletitle").text
    #linkPersona = persona.
    lugarFecha = persona.find('strong', style="font-size: small").text
    descrip = persona.find('div', class_ = "articledescrip").text
    print(indice, nombre)
    print("Lugar/Fecha: ", lugarFecha)
    print("Descripción:", descrip, "\n")
