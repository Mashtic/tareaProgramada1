# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 02/11/2022 09:00 pm
# Última modificación: 05/11/2022 10:28 pm
# Versión: 3.10.8

# Función auxliares
def obtenerNombre(pVisitante):
    """
    Funcionalidad: toma los datos de la tupla correspondiente
                   al nombre y los devuelve
    Entradas: pVisitante (list)
    Salidas: nombre de la persona (str)
    """
    return pVisitante[1][0] + " " + pVisitante[1][1] + " " + pVisitante[1][2]

def crearArchivoHtml(pNombre, pInfo):
    """
    Funcionalidad: crea el archivo HTML
    Entradas: pNombre (str)
              pInfo (str)
    Salidas: N/A
    """
    archivo = open(pNombre + ".html", 'w')
    archivo.write(pInfo)
    archivo.close
    return

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
        "<td>"+ datosContenido[2]+"</td><td>"+ datosContenido[3]+"</td><td><a target='_blank' href="+datosContenido[4]+">"+datosContenido[4]+"</a>.</td></tr>")
        strTabla += strElementos
    return strTabla + "</table>"

# 7. Reportes

# Perfil 
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
    cedula = str(pVisitante[0])
    htmlVisit = ("<html>\n<head>\n<title> \nReporte " + cedula +
    "</title>\n</head> <body><h2>Reporte visitante" + "</h2>"
    "<h3>Cedula</h3> \n<p>"+ cedula +"</p>"
    "<h3>Nombre</h3> \n<p>"+str(obtenerNombre(pVisitante))+"</p>")
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
    return crearArchivoHtml("Reporte bilioteca", htmlBiblio)

# Reporte astrónomos
def astrosRango(pAstronomos, pPrimerAnno, pSegundoAnno):
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

def reporteAstrosRango(pAstronomos, pPrimerAnno, pSegundoAnno=2022):
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
    astrosRango = astrosRango(pAstronomos, pPrimerAnno, pSegundoAnno)
    strTabla += tablaAstros(astrosRango)
    strTabla += "</html>"
    return crearArchivoHtml("Reporte astronónomos " + str(pPrimerAnno) + " - " + str(pSegundoAnno), strTabla)

# Visitantes baja
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
            strElementos = ("<tr><td>"+str(visitante[0])+"</td><td>"+ obtenerNombre(visitante)+"</td></tr>")
            strTabla += strElementos
    strTabla += "</table></html>"
    return crearArchivoHtml("Reporte bajas visitantes", strTabla)

# Recursos tipo
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
    return crearArchivoHtml("Reporte biblioteca " + pTipo, htmlBiblioTipo)

# Pruebas funciones
#contAstros = crearContadorAstro(visitantes)

#print(estadisticasAstros(visitantes))

#for visitante in visitantes:
  #  reporteVisitante(visitante, astronomos)

#reporteStatsAstros(visitantes, astronomos)

#reporteAstrosRango(astronomos, 1900)

#reporteVisitBaja(visitantes)

#reporteBiblioteca(visitantes)

#reporteBibliotecaTipo("Uno bonito", visitantes)