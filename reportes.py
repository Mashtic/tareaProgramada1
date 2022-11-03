# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 02/11/2022 09:00 pm
# Última modificación: 02/11/2022 09:45 pm
# Versión: 3.10.8

# Ejemplo entrada
visitantes = [[305430092, ("Ian", "Coto", "Soto"), [], [], False], [987654321, ("Pedro", "Moto", "Zote"), [], [], True], 
[696969699, ("Esteban", "Mi", "Novio"), [], [], False]]

# Función 
def obtenerNombre(pVisitante):
    return pVisitante[1][0] + " " + pVisitante[1][1] + " " + pVisitante[1][2]

def crearArchivoHtml(pNombre, pInfo):
    archivo = open(pNombre + ".html", 'w')
    archivo.write(pInfo)
    archivo.close
    return

# 7. Reportes

# Perfil 

def reporteVisitante(pVisitante):
    cedula = str(pVisitante[0])
    htmlVisit = ("<html>\n<head>\n<title> \nReporte " + cedula +
    "</title>\n</head> <body><h2>Reporte visitante" + "</h2>"
    "<h3>Cedula</h3> \n<p>"+ cedula +"</p>"
    "<h3>Nombre</h3> \n<p>"+str(obtenerNombre(pVisitante))+"</p>""\n</body></html>")
    return crearArchivoHtml("Reporte " + cedula, htmlVisit)

# Estadísticas astrónomos

# Biblioteca digital

# Reporte astrónomos

# Visitantes baja

def obtenerVisitBaja(pVisitantes):
    visitBaja = []
    for visitante in pVisitantes:
        if visitante[4] == False:
            visitBaja.append(visitante)
    return visitBaja

def reporteVisitBaja(pVisitantes):
    strTabla = "<html>\n<head>\n<title> \nBaja visitantes \n\
                </title>\n</head><body><h1>Visitantes dados de baja</h1> \
                <table><tr><th>Cédula</th><th>Nombres</th></tr>"
    visitBaja = obtenerVisitBaja(pVisitantes)
    for visitante in visitBaja:
        strElementos = ("<tr><td>"+str(visitante[0])+"</td><td>"+ obtenerNombre(visitante)+"</td></tr>")
        strTabla += strElementos
    strTabla += "</table></html>"
    return crearArchivoHtml("Bajas visitantes", strTabla)

# Recursos tipo
for visitante in visitantes:
    reporteVisitante(visitante)