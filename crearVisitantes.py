# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 26/10/2022 07:45 pm
# Última modificación: 3/10/2022 10:15 pm
# Versión: 3.10.8
#Biblioteca Importadas
import re
#Variables Globales
matrizvisitantes=[]
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

def validarNombre(nombre):
    """
    Funcionalidad: valida que el formato del nombre esté correcto
    Entradas: nombre (tuple)
    Salidas: nombre(tuple) o recibirNombreES()
    """
    nombre=list(nombre)
    for i in nombre:
        if re.findall("[^a-zA-ZáéíóúÁÉÍÓÚ]", i):
            print("El nombre, primero apellido o segundo apellido tiene carctéres no validos")
            return recibirNombreES()
    return tuple(nombre)

def recibirCedulaAux(cedula):
    """
    Funcionalidad: valida las entradas
    Entradas: cedula (str)
    Salidas: cedula (int) o recibirCedulaES()
    """
    global matrizvisitantes
    if esCedula(cedula)==True:
        return cedula
    else:
        print("La cédula introducida tiene un formato incorrecto")
        return recibirCedulaES()


def recibirCedulaES():
    """
    Funcionalidad: recibre la cedula
    Entradas: n/a
    Salidas: recibirCedulaAux(cedula)
    """
    cedula=input("Digite su número de cédula: ")
    return recibirCedulaAux(cedula)


def recibirNombreAux(nombre):
    """
    Funcionalidad: valida las entradas
    Entradas: nombre (str)
    Salidas: tuplanombre (tuple)
    """
    listanombre=nombre.split(" ")
    tuplanombre=validarNombre(tuple(listanombre))
    return tuplanombre

def recibirNombreES():
    """
    Funcionalidad: recibre el nombre
    Entradas: n/a
    Salidas: recibirNombreAux(cedula)
    """
    nombre=input("Digite su nombre completo: ")
    return recibirNombreAux(nombre)


def crearVisitante():
    """
    Funcionalidad: Añade el nuevo visitante a la matriz existente
    Entradas: n/a
    Salidas: matrizvisitantes
    """
    global matrizvisitantes
    listavisitante=[recibirCedulaES(), recibirNombreES(), [], [], True]
    matrizvisitantes.append(listavisitante)
    return matrizvisitantes

print(crearVisitante())


