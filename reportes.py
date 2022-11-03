# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 02/11/2022 09:00 pm
# Última modificación: 02/11/2022 09:45 pm
# Versión: 3.10.8

# Ejemplo entrada
visitantes = [[305430092, ("Ian", "Coto", "Soto"), [], [], False], [987654321, ("Pedro", "Moto", "Zote"), [], [], True], 
[696969699, ("Esteban", "Mi", "Novio"), [], [], False]]

# Función auxiliar
def crearArchivoHtml(pNombre, pInfo):
    archivo = open(pNombre + ".html", 'w')
    archivo.write(pInfo)
    archivo.close
    return

# 7. Reportes

# Perfil visitante

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

def reporteVisitBaja():
    strTabla = "<html>\n<head>\n<title> \nBaja visitantes \n\
                </title>\n</head><body><h1>Visitantes dados de baja</h1> \
                <table><tr><th>Cédula</th><th>Nombres</th></tr>"
    visitBaja = obtenerVisitBaja(visitantes)
    for visitante in visitBaja:
        strElementos = "<tr><td>"+str(visitante[0])+"</td><td>"+ visitante[1][0]+" "+visitante[1][1]+" "+ visitante[1][2]+"</td></tr>"
        strTabla += strElementos
    strTabla += "</table></html>"
    return crearArchivoHtml("Bajas visitantes", strTabla)

# Recursos tipo

