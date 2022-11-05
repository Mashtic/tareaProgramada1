# Creado por: Ian Steven Coto Soto
# Fecha de creación: 04/11/2022 16:14 pm
# Última modificación: 04/11/2022 XX:XX pm
# Versión: 3.10.8

# Importar librerías
from funciones import *
from tkinter import messagebox

# Funciones de apoyo
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

def validaMensajeExito(pCedula, pVisitantes):
    if esCedula(pCedula) and esVisitante(int(pCedula), pVisitantes):
        return True
    return False

# Funciones auxiliares
# Función 1. Importar astrotónomos
def crearDiccAstronomosAux(cantAstros, diccAstros):
    """
    Funcionalidad: comprueba datos de entrada
    Entradas: cantAstros (int): 0 < cantAstros <= 50
    Salidas: resultado crearDiccAstronomos(cantAstros)
    """
    if not esEntero(cantAstros):
        return messagebox.showerror("Cantidad astrónomos inválida", 
        "Debe introducir un número entero como cantidad de astrónomos.")
    elif not (0<int(cantAstros)<=50):
        return messagebox.showerror("Cantidad astrónomos inválida", 
        "Debe introducir un número entero mayor a 0 y menor a 51.")
    messagebox.showinfo("Astrónomos creados", 
        "Los " + cantAstros + " astrónomos han sido importados.")
    return crearDiccAstronomos(int(cantAstros), diccAstros)

# Función 2. Crear visitante
# Función 3. Crear DB visitantes
# Función 4. Asignar astrónomos fans 
"""
No se necesita validar ya que el bloqueo del botón ocurre cuando no se han importado
astrónomos, por tanto, no ocurren errores
"""

# Función 5. Biblioteca digital

# Función 6. Dar de baja
def darBajaVisitAux(pCedula, pVisitantes):
    """
    Funcionalidad: comprueba datos de entrada
    Entradas: pCedula (str)
              pVisitantes (dict)
    Salidas: resultado darBajaVisit(int(pCedula), pVisitantes)
    """
    if not esCedula(pCedula):
        return messagebox.showerror("Número de cédula incorrecto", 
        "Introduzca un número de cédula de la forma X0XXX0XXX.")
    elif not esVisitante(int(pCedula), pVisitantes):
        return messagebox.showerror("Visitante no registrado", 
        "Ingrese la cédula de un visitante registrado.")
    return darBajaVisit(int(pCedula), pVisitantes)

# Función 7. Reportes
# Perfil de visitante
def reporteVisitanteAux(pCedula, pVisitantes):
    """
    Funcionalidad: comprueba datos de entrada
    Entradas: pCedula (str)
              pVisitantes (dict)
    Salidas: resultado darBajaVisit(int(pCedula), pVisitantes)
    """
    if not esCedula(pCedula):
        return messagebox.showerror("Número de cédula incorrecto", 
        "Introduzca un número de cédula de la forma X0XXX0XXX.")
    elif not esVisitante(int(pCedula), pVisitantes):
        return messagebox.showerror("Visitante no registrado", 
        "Ingrese la cédula de un visitante registrado.")
    return reporteVisitante(pCedula, pVisitantes)

# Estadísticas astrónomos
"""
No se necesita crear
"""

# Biblioteca digital
"""
No se necesita crear
"""

# Reporte astrónomos
def reporteAstrosRangoAux(pAstronomos, pPrimerAnno, pSegundoAnno):
    if not esEntero(pPrimerAnno):
        return messagebox.showerror("Año incorrecto", 
        "Digite un número de año correcto (mayor a 0).")
    elif int(pPrimerAnno) < 0:
        return messagebox.showerror("Año incorrecto", 
        "El año debe ser mayor a 0.")
    elif pSegundoAnno == "":
        pSegundoAnno = int("2022")
    elif not esEntero(pSegundoAnno):
        return messagebox.showerror("Año incorrecto", 
        "Digite un número de año correcto (mayor a 0).")
    elif int(pSegundoAnno) < 0 or int(pSegundoAnno) > 2022:
        return messagebox.showerror("Año incorrecto", 
        "El año debe ser mayor a 0 o menor a 2022.")
    elif not (pPrimerAnno < pSegundoAnno):
        return messagebox.showerror("Años incorrectos", 
        "El segundo año debe ser mayor al primero.")
    return reporteAstrosRango(pAstronomos, pPrimerAnno, pSegundoAnno)

# Visitantes de baja
"""
No se necesita crear
"""

# Recursos de un tipo
"""
No se necesita crear
"""
