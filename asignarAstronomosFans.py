# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 02/11/2022 07:45 pm
# Última modificación: 03/11/2022 02:10 pm
# Versión: 3.10.8

# Importar módulos
from random import *

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
    """
    Funcionalidad: agrega una cantidad de códigos de astrónomos 
                   equivalente a pNumProvincia y los devuelve en lista
    Entradas: pNumProvincia (int)
              codAstros (list): lista de códigos de astrónomos
    Salidas: astrosFans (list)
    """
    astrosCant = 1
    astrosFans = []
    if pNumProvincia > len(codAstros): # Si pNumProvincia es mayor a codAstros,
                                       # se agrega una cantidad equivalente a los
                                       # codAstros disponibles
        pNumProvincia = len(codAstros)
    while pNumProvincia >= astrosCant:
        posAstro = randint(0, len(codAstros)-1) # Para hacerlo de manera aleatoria
        astrosFans.append(codAstros[posAstro])
        codAstros.pop(posAstro) # Para no volver a elegirlo
        astrosCant += 1
    return astrosFans

def asignarAstroFans(pVisitantes, pAstronomos):
    """
    Funcionalidad: se agrega una cantidad de astrónomos equivalente al
                   número inicial de la cédula de cada visitante 
    Entradas: pVisitantes (list)
              pAstronomos (dict)
    Salidas: pVisitantes (list) (actualizada)
    """
    for visitante in pVisitantes:
        codAstros = obtenerListasLlaves(pAstronomos)
        visitante[2] = asignarAstros(visitante[0]//100000000, codAstros) # Se le asinga un dict
                                                                         # con códigos a cada 
                                                                         # visitante
    return pVisitantes

# Prueba
#print(asignarAstroFans(visitantes, astronomos))
