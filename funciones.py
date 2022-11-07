# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 13/10/2022 11:30 am
# Última modificación: 06/11/2022 10:20 pm
# Versión: 3.10.8

# Importar libreías
from bs4 import BeautifulSoup
import requests
from random import *
from tkinter import messagebox
import nasapy
from datetime import date
from names import *

# Función archivos HTML
def crearArchivoHtml(pNombre, pInfo):
    """
    Funcionalidad: crea el archivo HTML
    Entradas: pNombre (str)
              pInfo (str)
    Salidas: N/A
    """
    archivo = open(pNombre + ".html", 'w', encoding="utf-8")
    archivo.write(pInfo)
    archivo.close
    return

# Funciones de apoyo
def esEntero(pNum):
    """
    Funcionalidad: comprueba que sea un número entero
    Entradas: pNum (int)
    Salidas: True/False (bool)
    """
    try:
        pNum = int(pNum)
        return True
    except:
        return False

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

def obtenerNombre(pNombre):
    """
    Funcionalidad: toma los datos de la tupla correspondiente
                   al nombre y los devuelve
    Entradas: pNombre (tuple)
    Salidas: nombre de la persona (str)
    """
    return pNombre[0] + " " + pNombre[1] + " " + pNombre[2]

# Funciones del programa
# 1. Función importar 
def retornarHtml(pLink):
    """
    Funcionalidad: se obtiene el código HTML de la página
    Entradas: pLink (str)
    Salidas: codHtml (bs4.BeautifulSoup)
    """
    peticion = requests.get(pLink).text
    codHtml = BeautifulSoup(peticion, 'lxml')
    return codHtml

def obtieneAnno(pStringAnno):
    """
    Funcionalidad: obtiene solamente los número hasta encontrar
                   algo diferente
    Entradas: pStringAnno (str)
    Salidas: annoDigitos (str)
    """
    annoDigitos = ""
    for caracter in pStringAnno:
        if not caracter.isdigit(): # Para parar cuando se 
                                   # encuentra a. C. por ej 
            break
        annoDigitos += caracter
    return annoDigitos

def importarAstronomos():
    """
    Funcionalidad: crea dos listas, una con los datos de los astrónomos
                   y otra con los códigos. Los 50 son extraídos 
    Entradas: N/A
    Salidas: llavesAstro (list)
             valoresAstro (list)
    """
    llavesAstro = []
    valoresAstro = []
    htmlAstro = retornarHtml('https://atlasdeastronomia.com/astronomos/')
    astronomos = htmlAstro.find_all('div', class_="articlebox")
    for persona in astronomos:
        nombre = persona.find('h2', class_="articletitle").text
        datosNacimientoAstro = persona.find('strong', style="font-size: small").text.split(",") # Separa en lista
        if "-" in datosNacimientoAstro[1]: # Si tiene dos fechas
            nacimientoFecha = tuple(datosNacimientoAstro[1].replace(" ", "").split("-")) # Lo separa en tupla
        else:
            nacimientoFecha = (datosNacimientoAstro[1].replace(" ", ""), "")
        linkDescrip = persona.find('a')['href']
        htmlDescrip = retornarHtml(linkDescrip)
        descripAstro = htmlDescrip.find('p').text.replace("\r\n", " ").replace("\n\r\n", " ").replace("\n", " ")
        llavesAstro.append(nombre[0] + obtieneAnno(nacimientoFecha[0]))
        valoresAstro.append([nombre, datosNacimientoAstro[0], nacimientoFecha, descripAstro]) # Añade los datos a las listas
    return llavesAstro, valoresAstro

def crearDiccAstronomos(cantAstros, diccAstros):
    """
    Funcionalidad: crea un diccionario con la cantidad de astrónomos
                   requerida y en diferente orden que la página
    Entradas: cantAstros (int): 1 <= cantAstros <= 50
              diccAstros (dict)
              impAstros (bool)
    Salidas: diccAstros (dict) (act)
    """
    if len(diccAstros) != 0:
        diccAstros = {} # Para que solo sean la cantidad que se pide
    numAstro = 1
    llavesAstro, valoresAstro = importarAstronomos()
    while cantAstros >= numAstro:
        posAstro = randint(0, len(llavesAstro)-1)
        diccAstros[llavesAstro[posAstro]] = valoresAstro[posAstro]
        llavesAstro.pop(posAstro)
        valoresAstro.pop(posAstro)
        numAstro += 1
    print(diccAstros)
    return diccAstros

# Función 2. Crear un visitante

def crearVisitante(matrizvisitantes, cedula, nombre):
    """
    Funcionalidad: Añade el nuevo visitante a la matriz existente
    Entradas: matrizvisitantes(list), cedula (int), nombre (int)
    Salidas: matrizvisitantes
    """
    listavisitante=[cedula, nombre, [], [], True]
    matrizvisitantes.append(listavisitante)
    print(matrizvisitantes)
    return matrizvisitantes

# Función 3. Crear BD de visitantes

def insertarVisitantes(matrizvisitantes, cant):
    """
    Funcionalidad: crea una matriz de visitantes
    Entradas: matrizvisitantes (list), cant (int)
    Salidas: matrizvisitantes (list)
    """
    listavisitantes=[]
    for i in range(cant):
        numCed=(random.randint(1, 999))+(10000*random.randint(1, 999))+(100000000*random.randint(1,9))
        listavisitantes=[str(numCed), (get_first_name(), get_last_name(), get_last_name()), 
        [], [], bool(random.getrandbits(1))]
        matrizvisitantes.append(listavisitantes)
    print(matrizvisitantes)
    return matrizvisitantes

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
        visitante[2] = asignarAstros(int(visitante[0])//100000000, codAstros) # Se le asinga un dict
                                                                         # con códigos a cada 
                                                                         # visitante
    print(pVisitantes)
    return pVisitantes

# Función 5. Cargar biblioteca principal
def importarDatosNasa():
    """
    F: retorna una lista con 100 datos de la API de la NASA
    E: N/A
    S: datosNasa (list): contiene los datos
    """
    clave="f24nnkOORGnEmbG7B7Bp01g6jL4UXQKLRh1kFn6s"
    nasa = nasapy.Nasa(key=clave)
    datosNasa = []
    for num in range(100):
        d = date(randint(2015,2021), randint(1, 12), randint(1,28)).strftime('%Y-%m-%d')
        try:
            apod= nasa.picture_of_the_day(date=d, hd=True)
            datosNasa.append((apod["title"], apod["date"], apod["explanation"], apod["media_type"], apod["url"]))
        except:
            continue
        print(num)
    print(datosNasa)
    return datosNasa

def asignarBibliotecaDigital(pNumUlt, datosNasa):
    """
    Funcionalidad: retorna una lista con la cantidad de datos de la NASA igual
                   a pNumUlt
    Entradas: pNumUlt (int)
              datosNasa (list)
    Salidas: datosNasaPersona (list)
    """
    cantDatosNasa = 1
    datosNasaPersona = []
    while pNumUlt >= cantDatosNasa:
        posNasa = randint(0, (len(datosNasa)-1))
        datosNasaPersona.append(datosNasa[posNasa])
        cantDatosNasa += 1
    return datosNasaPersona

def bibliotecaDigital(matrizVisitantes, datosNasa):
    """
    F: función que introduce los datos de la NASA a cada visitante
    E: matrizVisitantes (list)
       datosNasa (list): contiene los datos de NASA
    S: matrizVisitante (list) (actualizada)
    """
    cont = 1
    for visitante in matrizVisitantes:
        if len(visitante[3]) == 0:
            visitante[3] = asignarBibliotecaDigital(int(visitante[0])%10, datosNasa)
        print(cont)
        cont +=1
    return matrizVisitantes

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
    print(pVisitantes)
    return pVisitantes

# Funciones 7. Reportes
def tablaAstros(pAstronomos):
    """
    Funcionalidad: crea la tabla de los astrónomos en HTML
    Entradas: pAstronomos (dict)
    Salidas: código HTML con los datos de la tabla astrónomos (str)
    """
    strTabla = "<table><tr><th>Nombre</th><th>Lugar de nacimiento</th><th>Época</th><th>Descripción</th></tr>"
    for datosAstro in pAstronomos.values():
        strElementos = ("<tr><td>"+datosAstro[0]+"</td><td>"+ datosAstro[1]+"</td>"+
        "<td>"+ datosAstro[2][0]+" - "+ datosAstro[2][1]+"</td><td>"+ datosAstro[3]+"</td></tr>")
        strTabla += strElementos
    return strTabla + "</table>"

def tablaContenidoNasa(pBiblioteca):
    """
    Funcionalidad: crea la tabla de la biblioteca en HTML
    Entradas: pBiblioteca (list)
    Salidas: código HTML con los datos de la tabla biblioteca (str)
    """
    strTabla = ("<table><tr><th>Fecha</th><th>Título</th><th>Descripción</th>"+
    "<th>Tipo de medio</th><th>Link</th></tr>")
    for datosContenido in pBiblioteca:
        strElementos = ("<tr><td>"+datosContenido[1]+"</td><td>"+ datosContenido[0]+"</td>"+
        "<td>"+ datosContenido[2]+"</td><td>"+ datosContenido[3]+"</td><td><a target='_blank'"+
        "href="+datosContenido[4]+">"+datosContenido[4]+"</a>.</td></tr>")
        strTabla += strElementos
    return strTabla + "</table>"

# Perfil de visitante
def astronomosFansVisit(pVisitante, pAstronomos):
    """
    Funcionalidad: devuelve un diccionario con solamente los
                   datos de los astrónomos que sigue el visitante
    Entradas: pVisitante (list) 
              pAstronomos (dict)
    Salidas: astrosVisitInfo (dict)
    """
    astrosVisitInfo = {}
    for codAstro in pVisitante[2]:
        astrosVisitInfo[codAstro] = pAstronomos[codAstro]
    return astrosVisitInfo

def reporteVisitante(pVisitante, pAstronomos):
    """
    Funcionalidad: crea el archivo HTML con la información del
                   visitante
    Entradas: pVisitante (list) 
              pAstronomos (dict)
    Salidas: resultado crearArchivoHtml("Reporte " + cedula, htmlVisit) (archivo HTML)
    """
    cedula = pVisitante[0]
    htmlVisit = ("<html>\n<head>\n<title> \nReporte " + cedula +
    "</title>\n</head> <body><h2>Reporte visitante" + "</h2>"
    "<h3>Cedula</h3> \n<p>"+ cedula +"</p>"
    "<h3>Nombre</h3> \n<p>"+str(obtenerNombre(pVisitante[1]))+"</p>")
    htmlVisit += "\n</body>" + tablaAstros(astronomosFansVisit(pVisitante, pAstronomos))
    htmlVisit += tablaContenidoNasa(pVisitante[3])
    htmlVisit += "</html>"
    return crearArchivoHtml("Reporte " + cedula, htmlVisit)

# Estadísticas astrónomos
def crearContadorAstro(pVisitantes):
    """
    Funcionalidad: crea una matriz con listas con el código del astrónomos que tienen
                   fans y un número 0 que sirve de contador
    Entradas: pVisitante (list) 
    Salidas: contAstros (list)
    """
    contAstros = []
    for visitante in pVisitantes:
        for codAstro in visitante[2]:
            astroCant = [codAstro, 0]
            if astroCant not in contAstros: # Si ya existe, no se agrega
                contAstros.append(astroCant)
    return contAstros

def estadisticasAstros(pVisitantes):
    """
    Funcionalidad: cuenta la cantidad de apariciones de cada astrónomo
                   y suma en el elemento [1] de cada lista
    Entradas: pVisitante (list) 
    Salidas: contAstros (list) (actualizado)
    """
    contAstros = crearContadorAstro(pVisitantes)
    for astronomo in contAstros:
        for visitante in pVisitantes:
            if astronomo[0] in visitante[2]:
                astronomo[1] += 1
        astronomo = astronomo
    return contAstros

def reporteStatsAstros(pVisitantes, pAstronomos):
    """
    Funcionalidad: crea el archivo HTML con la información de las estadísticas
                   de los fanáticos de astrónomos
    Entradas: pVisitante (list) 
              pAstronomos (dict)
    Salidas: resultado crearArchivoHtml("Reporte estadísticas astronónomos", strTabla)
    """
    strTabla = "<html>\n<head>\n<title> \nEstadísticas astrónomos \n\
                </title>\n</head><body><h1>Estadísticas astrónomos fans</h1> \
                <table><tr><th>Nombres</th><th>Cantidad de admiradores</th></tr>"
    statsAstros = estadisticasAstros(pVisitantes)
    for astronomo in statsAstros:
        strElementos = ("<tr><td>"+pAstronomos[astronomo[0]][0]+"</td><td>"+ str(astronomo[1])+"</td></tr>")
        strTabla += strElementos
    strTabla += "</table></html>"
    return crearArchivoHtml("Reporte estadísticas astronónomos", strTabla)

# Biblioteca digital
def obtenerBibliotecaCompleta(pVisitantes):
    """
    Funcionalidad: crea una lista con los datos de la API utilizados en
                   los visitantes
    Entradas: pVisitante (list) 
    Salidas: biblioteca (list)
    """
    biblioteca = []
    for visitante in pVisitantes:
        for contenido in visitante[3]:
            if contenido not in biblioteca:
                biblioteca.append(contenido)
    return biblioteca

def reporteBiblioteca(pVisitantes):
    """
    Funcionalidad: crea el archivo HTML con la información de las estadísticas
                   de los fanáticos de astrónomos
    Entradas: pVisitante (list) 
    Salidas: resultado crearArchivoHtml("Reporte bilioteca", htmlBiblio)
    """
    htmlBiblio = ("<html>\n<head>\n<title> \nReporte biblioteca" +
    "</title>\n</head> <body><h2>Reporte biblioteca" + "</h2>")
    biblioteca = obtenerBibliotecaCompleta(pVisitantes)
    htmlBiblio += "\n</body>" + tablaContenidoNasa(biblioteca)
    htmlBiblio += "</html>"
    return crearArchivoHtml("Reporte biblioteca", htmlBiblio)

# Reporte astrónomos
def obtenerRangoAstros(pAstronomos, pPrimerAnno, pSegundoAnno):
    """
    Funcionalidad: crea una lista con los datos de la API utilizados en
                   los visitantes
    Entradas: pVisitante (list)
              pPrimerAnno (int)
              pSegundoAnno (int)
    Salidas: biblioteca (list)
    """
    rangoAnnos = range(pPrimerAnno, pSegundoAnno)
    astrosRango = {}
    for codAstro, datosAstro in pAstronomos.items():
        if int(codAstro[1:]) in rangoAnnos:
            astrosRango[codAstro] = datosAstro
    return astrosRango

def reporteAstrosRango(pAstronomos, pPrimerAnno, pSegundoAnno):
    """
    Funcionalidad: crea el archivo HTML con la información de los astrónomos
                   en el rango de años inscrito
    Entradas: pVisitante (list) 
              pPrimerAnno (int)
              pSegundoAnno (int)
    Salidas: resultado crearArchivoHtml("Reporte astronónomos " + 
    str(pPrimerAnno) + " - " + str(pSegundoAnno), strTabla)
    """
    strTabla = "<html>\n<head>\n<title>Astrónomos en rango\n\
                </title>\n</head><body><h1>Astrónomos desde "+str(pPrimerAnno)+" hasta "+str(pSegundoAnno)+"</h1>"
    astrosRango = obtenerRangoAstros(pAstronomos, pPrimerAnno, pSegundoAnno)
    strTabla += tablaAstros(astrosRango)
    strTabla += "</html>"
    return crearArchivoHtml("Reporte astronónomos " + str(pPrimerAnno) + " - " + str(pSegundoAnno), strTabla)

# Visitantes de baja
def reporteVisitBaja(pVisitantes):
    """
    Funcionalidad: crea el archivo HTML con la información de los datos de
                   las personas dadas de baja
    Entradas: pVisitante (list) 
    Salidas: resultado crearArchivoHtml("Reporte bajas visitantes", strTabla)
    """
    strTabla = "<html>\n<head>\n<title> \nBajas visitantes \n\
                </title>\n</head><body><h1>Visitantes dados de baja</h1> \
                <table><tr><th>Cédula</th><th>Nombres</th></tr>"
    for visitante in pVisitantes:
        if visitante[4] == False:
            strElementos = ("<tr><td>"+str(visitante[0])+"</td><td>"+ obtenerNombre(visitante[1])+"</td></tr>")
            strTabla += strElementos
    strTabla += "</table></html>"
    return crearArchivoHtml("Reporte bajas visitantes", strTabla)

# Recursos de un tipo
def obtenerBibliotecaTipo(pTipo, pVisitantes):
    """
    Funcionalidad: crea una lista con los tipos iguales a pTipo
    Entradas: pVisitante (list)
              pTipo (str)
    Salidas: bibliotecaTipo (list)
    """
    biblioteca = obtenerBibliotecaCompleta(pVisitantes)
    bibliotecaTipo = []
    for datosContenido in biblioteca:
        if datosContenido[3] == pTipo:
            bibliotecaTipo.append(datosContenido)
    return bibliotecaTipo

def reporteBibliotecaTipo(pTipo, pVisitantes):
    """
    Funcionalidad: crea el archivo HTML con la información de la biblioteca
                   de acuerdo al tipo
    Entradas: pVisitante (list)
              pTipo (str)
    Salidas: resultado crearArchivoHtml("Reporte biblioteca " + pTipo, htmlBiblioTipo)
    """
    htmlBiblioTipo = ("<html>\n<head>\n<title> \nReporte biblioteca "+ pTipo +
    "</title>\n</head> <body><h2>Reporte biblioteca " + pTipo + "</h2>")
    htmlBiblioTipo += "\n</body>" + tablaContenidoNasa(obtenerBibliotecaTipo(pTipo, pVisitantes))
    htmlBiblioTipo += "</html>"
    messagebox.showinfo("Reporte creado", 
        "Se ha creado el reporte de la biblioteca de tipo " + pTipo + ".")
    return crearArchivoHtml("Reporte biblioteca " + pTipo, htmlBiblioTipo)
