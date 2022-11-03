# Creado por: Ian Steven Coto Soto
# Fecha de creación: 03/11/2022 11:00 am
# Última modificación: 03/11/2022 11:05 am
# Versión: 3.10.8

# Importar librerías
import re

visitantes = [[305430092, ("Ian", "Coto", "Soto"), ["I1642", "A1933"], [("La venganza","13/02/2022","Muy lejos", "Uno bonito", "https://www.google.com")], True], [987654321, ("Pedro", "Moto", "Zote"), ["A1933", "V1928"], [("La venganza","14/02/2022","Muy lejos", "Uno bonito", "https://www.google.com")], True], 
[696969699, ("Esteban", "Mi", "Novio"), ["I1642"], [("La venganza","13/02/2022","Muy lejos", "Uno bonito", "https://www.google.com")], False]]


# Función auxiliar
def esVisitante(pCedula, pVisitantes):
    for visitante in pVisitantes:
        if pCedula == visitante[0]:
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
    for posicion, visitante in enumerate(pVisitantes):
        if pCedula == visitante[0]:
            pVisitantes[posicion][4] = False
            break
    return pVisitantes

def darBajaVisitAux(pCedula, pVisitantes):
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