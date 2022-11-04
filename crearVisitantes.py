# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 02/11/2022 07:45 pm
# Última modificación: 03/11/2022 02:10 pm
# Versión: 3.10.8
import re
matrizvisitantes=[]
def validarCedula(cedula):
    """
    Funcionalidad: valida que la cédula cumpla con el formato
    Entradas: cedula (str)
    Salidas: True/False (bool)
    """
    if re.match("[1-9]{1}\d{8}", cedula): # Si cumple el formato de cédula en
                                          # en CR, retorna True
        return True
    return False

def validarNombre(nombre):
    nombre=list(nombre)
    for i in nombre:
        if re.findall("[^a-zA-ZáéíóúÁÉÍÓÚ]", i):
            print("El nombre, primero apellido o segundo apellido tiene carctéres no validos")
            return recibirNombreES()
    return tuple(nombre)

def recibirCedulaAux(cedula):
    global matrizvisitantes
    if validarCedula(cedula)==True:
        return cedula
    else:
        print("La cédula introducida tiene un formato incorrecto")
        return recibirCedulaES()


def recibirCedulaES():
    cedula=input("Digite su número de cédula: ")
    return recibirCedulaAux(cedula)


def recibirNombreAux(nombre):
    listanombre=nombre.split(" ")
    tuplanombre=validarNombre(tuple(listanombre))
    return tuplanombre

def recibirNombreES():
    nombre=input("Digite su nombre completo: ")
    return recibirNombreAux(nombre)


def crearVisitante():
    global matrizvisitantes
    listavisitante=[recibirCedulaES(), recibirNombreES(), [], [], True]
    matrizvisitantes.append(listavisitante)
    return matrizvisitantes

print(crearVisitante())


