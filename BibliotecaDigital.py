# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 03/11/2022 0:45 pm
# Última modificación: 05/11/2022 03:48 pm
# Versión: 3.10.8

import nasapy
from datetime import date
from BDVisitantes import *
from entradas import *
from random import *

def importarDatosNasa():
    """
    F: retorna una lista con 100 datos de la API de la NASA
    E: N/A
    S: datosNasa (list): contiene los datos
    """
    clave="f24nnkOORGnEmbG7B7Bp01g6jL4UXQKLRh1kFn6s"
    nasa = nasapy.Nasa(key=clave)
    datosNasa = []
    for num in range(100):
        d = date(randint(2015,2021), randint(1, 12), randint(1,28)).strftime('%Y-%m-%d')
        try:
            apod= nasa.picture_of_the_day(date=d, hd=True)
            datosNasa.append((apod["title"], apod["date"], apod["explanation"], apod["media_type"], apod["url"]))
            print((apod["title"], apod["date"], apod["explanation"], apod["media_type"], apod["url"]))
        except:
            continue
    return datosNasa

def asignarBibliotecaDigital(pNumUlt, datosNasa):
    """
    Funcionalidad: retorna una lista con la cantidad de datos de la NASA igual
                   a pNumUlt
    Entradas: pNumUlt (int)
              datosNasa (list)
    Salidas: datosNasaPersona (list)
    """
    cantDatosNasa = 1
    datosNasaPersona = []
    while pNumUlt >= cantDatosNasa:
        posNasa = randint(0, (len(datosNasa)-1))
        datosNasaPersona.append(datosNasa[posNasa])
        datosNasa.pop(posNasa)
        cantDatosNasa += 1
    return datosNasaPersona

def bibliotecaDigital(matrizVisitantes, datosNasa):
    """
    F: función que introduce los datos de la NASA a cada visitante
    E: matrizVisitantes (list)
       datosNasa (list): contiene los datos de NASA
    S: matrizVisitante (list) (actualizada)
    """
    for visitante in matrizVisitantes:
        visitante[3] = asignarBibliotecaDigital(visitante[0]%10, datosNasa)
    return matrizVisitantes
