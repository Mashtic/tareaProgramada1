# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 02/11/2022 07:45 pm
# Última modificación: 03/11/2022 02:10 pm
# Versión: 3.10.8
from names import *
import random

def insertarVisitantes(cant):
    """
    Funcionalidad: crea una matriz de visitantes
    Entradas: cant (int)
    Salidas: matrizvisitantes (list)
    """
    matrizvisitantes=[]
    for i in range(cant):
        listavisitantes=[random.randint(100000000,999999999), (get_first_name(), get_last_name(), get_last_name()), 
        [], [], bool(random.getrandbits(1))]
        matrizvisitantes.append(listavisitantes)
    print("\nLos visitantes han sido creados exitosamente.")
    return matrizvisitantes

def insertarVisitantesAux(cant):
    """
    Funcionalidad: valida datos de entrada
    Entradas: cant (int) (cant > 0 o cant <=1000)
    Salidas: resultado insertarVisitantes(cant) (list)
    """
    try:
        cant=int(cant)
        if (0 < cant <= 1000): # Equipos tradicionales de máximo 50 personas y mínimo 1
            return "Debe digitar una cantidad de miembros entre 1 y 50."
        return insertarVisitantes(cant)
    except:
        return "La cantidad de visitantes debe ser un número entero positivo."

def insertarVisitantesES():
    """
    Funcionalidad: entrada y salida de datos
    Entradas: cant (str)
    Salidas: resultado insertarVisitantesAux (list) o mensaje de retroalimentación
             para realizar corrección (str)
    """
    cant=input("\nDigite la cantidad de visitantes: ")
    return insertarVisitantesAux(cant)
