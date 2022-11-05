# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 27/10/2022 1:05 pm
# Última modificación: 3/10/2022 10:10 pm
# Versión: 3.10.8
#Bibliotecas Importadas
from names import *
import random
import re
#Funciones
def esCedula(cedula):
    """
    Funcionalidad: valida que la cédula cumpla con el formato
    Entradas: cedula (str)
    Salidas: True/False (bool)
    """
    if re.match(r"^[1-9](0[0-9]{3}){2}", cedula) == None: # Si cumple el formato de cédula en
                                                          # en CR, retorna True
        return False
    return True

def insertarVisitantes(cant):
    """
    Funcionalidad: crea una matriz de visitantes
    Entradas: cant (int)
    Salidas: matrizvisitantes (list)
    """
    matrizvisitantes=[]
    listavisitantes=[]
    for i in range(cant):
        num=(random.randint(1, 999))+(10000*random.randint(1, 999))+(100000000*random.randint(1,9))
        listavisitantes=[num, (get_first_name(), get_last_name(), get_last_name()), 
        [], [], bool(random.getrandbits(1))]
        matrizvisitantes.append(listavisitantes)
        print(matrizvisitantes)
    
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
        if (0 < cant <= 1000): # Equipos tradicionales de máximo 1000 personas y mínimo 1
            return insertarVisitantes(cant)
        return "Debe digitar una cantidad de miembros entre 1 y 1000."
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
    print("holipt1")
    return insertarVisitantesAux(cant)
