# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 13/10/2022 11:30 am
# Última modificación: 06/11/2022 10:20 pm
# Versión: 3.10.8

# Importar librerías
from funciones import *
from tkinter import messagebox
import re

# Funciones de apoyo
def esVisitante(pCedula, pVisitantes):
    """
    Funcionalidad: comrpueba que la cédula esté en el registro de visitantes,
                   si lo está, retorna True
    Entradas: pCedula (str)
              pVisitantes (list)
    Salidas: True/False (bool)
    """
    for visitante in pVisitantes:
        if pCedula == visitante[0]: # Si se encuentra
            return True
    return False

def retornaVisitante(pCedula, pVisitantes):
    """
    Funcionalidad: devueleve al visitante según su cédula
    Entradas: pCedula (str)
              pVisitantes (list of lists)
    Salidas: visitante (list)
    """
    for visitante in pVisitantes:
        if pCedula == visitante[0]: # Si se encuentra, lo retorna
            return visitante
    return []

def esCedula(pCedula):
    """
    Funcionalidad: valida que la cédula cumpla con el formato
    Entradas: pCedula (str)
    Salidas: True/False (bool)
    """
    if re.match(r"^[1-9](0[0-9]{3}){2}", pCedula) == None: # Si cumple el formato de cédula en
                                                          # en CR, retorna True
        return False
    return True

def validaMensajeExito(pCedula, pVisitantes):
    """
    Funcionalidad: comprueba que sea una cédula y que exista en
                   el registro de visitantes
    Entrada: pCedula (str) 
             pVisitantes (list)
    Salida: True/False (bool)
    """
    visitante = retornaVisitante(pCedula, pVisitantes)
    print(visitante) 
    if (esCedula(pCedula) and esVisitante(pCedula, pVisitantes) and 
    visitante[4] == True):
        return True
    return False

def validarNombre(nombre):
    """
    Funcionalidad: valida que el formato del nombre esté correcto
    Entradas: nombre (str)
    Salidas: True/False (bool)
    """
    if re.match("^(\s?[A-ZÁÉÍÓÚ][a-záéíóú]+){3}$", nombre) == None:
        return False
    return True

# Funciones auxiliares
# Función 1. Importar astrotónomos
def crearDiccAstronomosAux(cantAstros, diccAstros):
    """
    Funcionalidad: comprueba datos de entrada
    Entradas: cantAstros (int): 0 < cantAstros <= 50
              diccAstros (dict)
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
def recibirNombreAux(nombre):
    """
    Funcionalidad: valida las entradas
    Entradas: nombre (str)
    Salidas: tuplanombre (tuple)
    """
    listanombre=nombre.strip().split(" ")
    tuplanombre=tuple(listanombre)
    return tuplanombre

def validarCrearVisitantes(matrizvisitantes, cedula, nombre):
    """
    Funcionalidad: valida las entradas
    Entradas: nombre (str), cedula (str), matrizvisitantes(list)
    Salidas: resultado de crearVisitante
    """
    if esCedula(cedula)==False:
        return messagebox.showerror("Formato incorrecto cédula", "La cédula introducida tiene un formato incorrecto")
    elif validarNombre(nombre)==False:
        return messagebox.showerror("Formato incorrecto nombre", "El nombre, primero apellido o segundo apellido tiene carctéres no validos")
    elif esVisitante(cedula, matrizvisitantes):
        return messagebox.showerror("El visitante ya registrado", "El visitante con cedula "+cedula+" ya se encuentra registrado.")
    else:
        messagebox.showinfo("Visitante creado", 
            "El visitante " + nombre +" "+ cedula + " ha sido creado.")
    return crearVisitante(matrizvisitantes, cedula, recibirNombreAux(nombre))

# Función 3. Crear DB visitantes
def insertarVisitantesAux(matrizvisitantes, cant):
    """
    Funcionalidad: valida datos de entrada
    Entradas: matrizvisitantes (list), cant (int) (cant > 0 o cant <=1000)
    Salidas: resultado insertarVisitantes(cant) (list)
    """
    if esEntero(cant):    
        if (0 < int(cant) <= 1000): # Equipos tradicionales de máximo 1000 personas y mínimo 1
            messagebox.showinfo("Se crearon los visitantes", "Se crearon "+cant+" nuevos visitantes.")
            return insertarVisitantes(matrizvisitantes, int(cant))
        return messagebox.showerror("Cantidad de visitantes inválida","Debe digitar una cantidad de miembros entre 1 y 1000.")
    else:
        return messagebox.showerror("Tipo de cantidad inválida","La cantidad de visitantes debe ser un número entero positivo.")

# Función 4. Asignar astrónomos fans 
"""
No se necesita validar ya que el bloqueo del botón ocurre cuando no se han importado
astrónomos, por tanto, no ocurren errores
"""

# Función 5. Biblioteca digital

"""
No se necesita validar ya que la información ya se encuentra validada en la matriz de los visitantes.
"""

# Función 6. Dar de baja
def darBajaVisitAux(pCedula, pVisitantes):
    """
    Funcionalidad: comprueba datos de entrada
    Entradas: pCedula (str)
              pVisitantes (list)
    Salidas: resultado darBajaVisit(int(pCedula), pVisitantes)
    """
    if not esCedula(pCedula):
        return messagebox.showerror("Número de cédula incorrecto", 
        "Introduzca un número de cédula de la forma X0XXX0XXX.")
    elif not esVisitante(pCedula, pVisitantes):
        return messagebox.showerror("Visitante no registrado", 
        "Ingrese la cédula de un visitante registrado.")
    elif (retornaVisitante(pCedula, pVisitantes))[4] == False:
        return messagebox.showerror("Visitante ya dado de baja", 
        "El visitante ya fue dado de baja previamente.")
    return darBajaVisit(pCedula, pVisitantes)

# Función 7. Reportes
# Perfil de visitante
def reporteVisitanteAux(pCedula, pVisitantes, pAstronomos):
    """
    Funcionalidad: comprueba datos de entrada
    Entradas: pCedula (str)
              pVisitantes (list)
    Salidas: resultado darBajaVisit(int(pCedula), pVisitantes)
    """
    if not esCedula(pCedula):
        return messagebox.showerror("Número de cédula incorrecto", 
        "Introduzca un número de cédula de la forma X0XXX0XXX.")
    elif not esVisitante(pCedula, pVisitantes):
        return messagebox.showerror("Visitante no registrado", 
        "Ingrese la cédula de un visitante registrado.")
    messagebox.showinfo("Reporte creado", 
        "Se ha creado el reporte del visitante " + pCedula + ".")
    return reporteVisitante(retornaVisitante(pCedula, pVisitantes), pAstronomos)

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
    """
    Funcionalidad: 
    Entradas: pAstronomos (dict)
              pPrimerAnno (str)
              pSegundoAnno (str)
    Salidas: resultado reporteAstrosRango(pAstronomos, 
    int(pPrimerAnno), int(pSegundoAnno))
    """
    if not esEntero(pPrimerAnno):
        return messagebox.showerror("Año incorrecto", 
        "Digite un número de año correcto (mayor a 0).")
    elif int(pPrimerAnno) < 0:
        return messagebox.showerror("Año incorrecto", 
        "El año debe ser mayor a 0.")
    elif pSegundoAnno == "":
        pSegundoAnno = "2022"
    elif not esEntero(pSegundoAnno):
        return messagebox.showerror("Año incorrecto", 
        "Digite un número de año correcto (mayor a 0).")
    elif int(pSegundoAnno) < 0 or int(pSegundoAnno) > 2022:
        return messagebox.showerror("Año incorrecto", 
        "El año debe ser mayor a 0 o menor a 2022.")
    elif not (int(pPrimerAnno) < int(pSegundoAnno)):
        return messagebox.showerror("Años incorrectos", 
        "El segundo año debe ser mayor al primero.")
    messagebox.showinfo("Reporte creado", 
    "El reporte reporte de astrónomos ha sido creado.")
    return reporteAstrosRango(pAstronomos, int(pPrimerAnno), int(pSegundoAnno))

# Visitantes de baja
"""
No se necesita crear
"""

# Recursos de un tipo
"""
No se necesita crear
"""
