# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 02/11/2022 07:45 pm
# Última modificación: 02/11/2022 08:15 pm
# Versión: 3.10.8

# Importar módulos
from random import *

# Variable prueba
visitantes = [[305430092, ("Ian", "Coto", "Soto"), [], [], True], [987654321, ("Pedro", "Moto", "Zote"), [], [], True], 
[696969699, ("Loco", "Es", "Poco"), [], [], True]]

astronomos = {"T624":[],"S1986":[], "A211":[], "A432":[], "K4311":[], "P892":[], "S123":[], "R89":[]}

"""
Faltan comentarios
Falta validaciones (se espera hasta tener todo listo para 
pensar cómo hacerla la GUI de tkinter)
"""

# Funciones auxiliares
def obtenerListasLlaves(pDicc):
    """
    Funcionalidad: obtener llaves de un diccionario como listas
    Entradas: pDicc (dict)
    Salidas: listaLlaves (list)
    """
    listaLlaves = []
    for llave in pDicc.keys():
        listaLlaves.append(llave) 
    return listaLlaves

# Función 4. Asignar astrónomos fans
def asignarAstros(pNumProvincia, codAstros):
    astrosCant = 1
    astrosFans = []
    if pNumProvincia > len(codAstros):
        pNumProvincia = len(codAstros)
    while pNumProvincia >= astrosCant:
        posAstro = randint(0, len(codAstros)-1)
        astrosFans.append(codAstros[posAstro])
        codAstros.pop(posAstro)
        astrosCant += 1
    return astrosFans

def asignarAstroFans(pVisitantes, pAstronomos):
    for visitante in pVisitantes:
        numProvincia = visitante[0]//100000000
        codAstros = obtenerListasLlaves(pAstronomos)
        visitante[2] = asignarAstros(numProvincia, codAstros)
    return pVisitantes

# Prueba
#print(asignarAstroFans(visitantes, astronomos))
