# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 02/11/2022 09:00 pm
# Última modificación: 03/11/2022 10:50 am
# Versión: 3.10.8

# Ejemplo entrada
visitantes = [[305430092, ("Ian", "Coto", "Soto"), ["I1642", "A1933"], [("La venganza","13/02/2022","Muy lejos", "Uno feo", "https://www.google.com")], False], [987654321, ("Pedro", "Moto", "Zote"), ["A1933", "V1928"], [("La venganza","14/02/2022","Muy lejos", "Uno bonito", "https://www.google.com")], True], 
[696969699, ("Esteban", "Mi", "Novio"), ["I1642"], [("La venganza","13/02/2022","Muy lejos", "Uno bonito", "https://www.google.com")], False]]

astronomos = {'I1642': ['Isaac Newton', 'Woolsthorpe Manor', ('1642', '1727'), 'Newton descubrió las leyes de la gravitación culminando la revolución científica que comenzó Copérnico. En su obra Principia Mathematica expuso las leyes que rigen la gravitación. De estas leyes dedujo la órbita de los cometas y explicó las mareas, además de establecer las bases de la física nuclear por la interacción de las fuerzas de atracción de las partículas. '], 'A1933': ['Arno Allan Penzias', 'Munich', ('1933', ''), 'El aporte sustancial de Arno Penzias y Robert Wilson a la ciencia fue el descubrimiento de la Radiación de Fondo de Microondas. Esta radiación es una consecuencia de la explosión del Big Bang. En sus experimentos descubrieron una radiación constante que no venía de la Tierra ni de la Vía Láctea, sino de fuera. Este descubrimiento les valió un Premio Nobel en 1978. Cuando la información salió a la luz creó grandes disputas, porque todavía existían muchos astrónomos que no creían en la existencia del Big Bang, y esta investigación probó que estaban errados.'], 'V1928': ['Vera Rubin', 'Filadelfia', ('1928', '2016'), 'Observando que existía un alto índice de agrupación en la distribución de las galaxias, conjeturó que éstas se concentraban en ciertas zonas dejando espacios vacíos entre ellas.  Estos resultados no despertaron casi ningún interés en el momento de su publicación, pero fueron confirmados quince años más tarde y ahora constituyen la base del estudio de la estructura a gran escala del Universo.  pionera en la medición de la rotación de las estrellas dentro de una galaxia. Sus mediciones pusieron de manifiesto que las curvas de rotación galácticas se mantenían planas, contradiciendo el modelo teórico, siendo la evidencia más directa y robusta de la existencia de materia oscura.']} 

# Función 
def obtenerNombre(pVisitante):
    return pVisitante[1][0] + " " + pVisitante[1][1] + " " + pVisitante[1][2]

def crearArchivoHtml(pNombre, pInfo):
    archivo = open(pNombre + ".html", 'w')
    archivo.write(pInfo)
    archivo.close
    return

def tablaAstros(pAstronomos):
    strTabla = "<table><tr><th>Nombre</th><th>Lugar de nacimiento</th><th>Época</th><th>Descripción</th></tr>"
    for datosAstro in pAstronomos.values():
        strElementos = ("<tr><td>"+datosAstro[0]+"</td><td>"+ datosAstro[1]+"</td>"+
        "<td>"+ datosAstro[2][0]+" - "+ datosAstro[2][1]+"</td><td>"+ datosAstro[3]+"</td></tr>")
        strTabla += strElementos
    return strTabla + "</table>"

def tablaContenidoNasa(pBiblioteca):
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
    astrosVisitInfo = {}
    for codAstro in pVisitante[2]:
        astrosVisitInfo[codAstro] = pAstronomos[codAstro]
    return astrosVisitInfo

def reporteVisitante(pVisitante, pAstronomos):
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
    contAstros = []
    for visitante in pVisitantes:
        for codAstro in visitante[2]:
            astroCant = [codAstro, 0]
            if astroCant not in contAstros:
                contAstros.append(astroCant)
    return contAstros

def estadisticasAstros(pVisitantes):
    contAstros = crearContadorAstro(pVisitantes)
    for astronomo in contAstros:
        for visitante in pVisitantes:
            if astronomo[0] in visitante[2]:
                astronomo[1] += 1
        astronomo = astronomo
    return contAstros

def reporteStatsAstros(pVisitantes, pAstronomos):
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
    biblioteca = []
    for visitante in pVisitantes:
        for contenido in visitante[3]:
            if contenido not in biblioteca:
                biblioteca.append(contenido)
    return biblioteca

def reporteBiblioteca(pVisitantes):
    htmlBiblio = ("<html>\n<head>\n<title> \nReporte biblioteca" +
    "</title>\n</head> <body><h2>Reporte biblioteca" + "</h2>")
    biblioteca = obtenerBibliotecaCompleta(pVisitantes)
    htmlBiblio += "\n</body>" + tablaContenidoNasa(biblioteca)
    htmlBiblio += "</html>"
    return crearArchivoHtml("Reporte bilioteca", htmlBiblio)

# Reporte astrónomos

def astrosRango(pAstronomos, pPrimerAnno, pSegundoAnno):
    rangoAnnos = range(pPrimerAnno, pSegundoAnno)
    astrosRango = {}
    for codAstro, datosAstro in pAstronomos.items():
        if int(codAstro[1:]) in rangoAnnos:
            astrosRango[codAstro] = datosAstro
    return astrosRango

def reporteAstrosRango(pAstronomos, pPrimerAnno, pSegundoAnno=2022):
    strTabla = "<html>\n<head>\n<title>Astrónomos en rango\n\
                </title>\n</head><body><h1>Astrónomos desde "+str(pPrimerAnno)+" hasta "+str(pSegundoAnno)+"</h1>"
    strTabla += tablaAstros(pAstronomos)
    strTabla += "</html>"
    return crearArchivoHtml("Reporte astronónomos " + str(pPrimerAnno) + " - " + str(pSegundoAnno), strTabla)

# Visitantes baja

def reporteVisitBaja(pVisitantes):
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
    biblioteca = obtenerBibliotecaCompleta(pVisitantes)
    bibliotecaTipo = []
    for datosContenido in biblioteca:
        if datosContenido[3] == pTipo:
            bibliotecaTipo.append(datosContenido)
    return bibliotecaTipo

def reporteBibliotecaTipo(pTipo, pVisitantes):
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