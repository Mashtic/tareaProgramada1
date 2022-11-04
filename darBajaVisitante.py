# Creado por: Ian Steven Coto Soto
# Fecha de creación: 03/11/2022 11:00 am
# Última modificación: 03/11/2022 11:25 am
# Versión: 3.10.8

# Importar librerías
import re

# Función auxiliar
def esVisitante(pCedula, pVisitantes):
    """
    Funcionalidad: comrpueba que la cédula esté en el registro de visitantes,
                   si lo está, retorna True
    Entradas: pCedula (int)
              pVisitantes (dict)
    Salidas: True/False (bool)
    """
    for visitante in pVisitantes:
        if pCedula == visitante[0]: # Si se encuentra
            return True
    return False

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


# Función 6. Dar de baja
def darBajaVisit(pCedula, pVisitantes):
    """
    Funcionalidad: cambia el estado de admisibilidad de la persona ingresada
    Entradas: pCedula (int)
              pVisitantes (dict)
    Salidas: pVisitantes (dict) (actualizado)
    """
    for posicion, visitante in enumerate(pVisitantes): # Da la posición y la lista
                                                       # con los datos del visitante
        if pCedula == visitante[0]:
            pVisitantes[posicion][4] = False # Para esa cédula, cambia el estado a False
            break
    return pVisitantes

def darBajaVisitAux(pCedula, pVisitantes):
    """
    Funcionalidad: comprueba datos de entrada
    Entradas: pCedula (str)
              pVisitantes (dict)
    Salidas: resultado darBajaVisit(int(pCedula), pVisitantes)
    """
    if not esCedula(pCedula):
        return "Introduzca un número de cédula correcto." # Cambiar por mensajes en tkinter
    elif not esVisitante(int(pCedula), pVisitantes):
        return "Ingrese la cédula de un visitante registrado."
    return darBajaVisit(int(pCedula), pVisitantes)

# Pruebas
#print(darBajaVisitAux("305430092", visitantes))
#print(darBajaVisitAux("cedula", visitantes))
#print(darBajaVisitAux("abcdefghj", visitantes))
#print(darBajaVisitAux("903450875", visitantes))