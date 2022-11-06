# Creado por: Ian Steven Coto Soto
# Fecha de creación: 03/11/2022 11:00 am
# Última modificación: 05/11/2022 10:27 pm
# Versión: 3.10.8

# Importar librerías
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from funciones import *
from validaciones import *
from entradas import *

# Funciones globales
crearVisitantes = (False, False)
reportes = ["Perfil de un visitante", "Estadística de astrónomos",
                            "Mostrar biblioteca digital", "Reporte de astrónomos", 
                            "Visitantes dados de baja", "Recurso por tipo"]
diccAstros = {}
fuenteBotones = ("Helvetica", 10)
fuenteBotonesMenu = ("Helvetica", 12)
fuenteTitulo = ("Helvetica", 20)

#------------ Ventanas ------------#
# Ventana 1. Importar astrónomos

def limpiarDiccAstros(diccAstros):
    """
    Funcionalidad: limpia la variable diccAstros (datos astrónomos)
    Entrada: diccAstros (dict)
    Salida: diccAstros (dict) (vacío)
    """
    messagebox.showinfo("Astrónomos vaciados", "Se ha limpiado los astrónomos.")
    return diccAstros.clear()

def impAstrosVent(ventanaMain):
    """
    Funcionalidad: ser la ventana que permite importar astrónomos
    Entrada: ventanaMain (CTK)
    Salida: importar astrónomos / mensaje error
    """
    global diccAstros
    impAstrosVent = ctk.CTkToplevel(ventanaMain)
    impAstrosVent.geometry("400x200")
    impAstrosVent.title("Importar astrónomos")
    titulo = ctk.CTkLabel(impAstrosVent, text="Importar astrónomos", 
    text_font=fuenteTitulo)
    titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    subTitulo = ctk.CTkLabel(impAstrosVent, 
    text="Ingrese la cantidad de astrónomos que desea importar: ",
    text_font=fuenteBotones)
    subTitulo.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    cantEntry = ctk.CTkEntry(master=impAstrosVent,
                               placeholder_text="0 < Cantidad <= 50",
                               width=125,
                               height=35,
                               border_width=2,
                               corner_radius=10)
    cantEntry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
    botonExtraer = ctk.CTkButton(master=impAstrosVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Extraer",
                                 command=lambda: 
                                 crearDiccAstronomosAux(cantEntry.get(), diccAstros))
    botonExtraer.place(relx=0.30, rely=0.7, anchor=tk.CENTER)
    botonLimpiar = ctk.CTkButton(master=impAstrosVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Limpiar",
                                 command=lambda: limpiarDiccAstros(diccAstros))
    botonLimpiar.place(relx=0.70, rely=0.7, anchor=tk.CENTER)
    botonSalir = ctk.CTkButton(master=impAstrosVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Regresar",
                                 command=lambda: impAstrosVent.destroy()) # Sale de la ventana
    botonSalir.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Ventana 6. Dar de baja
def confirmarBaja(pCedula):
    """
    Funcionalidad: confirmar que se quiera dar la baja al visitante
    Entrada: pCedula (str)
    Salida: llamar a darBajaVisitAux(pCedula, visitantes) o mensaje retroalimentación
    """
    confirmar = messagebox.askquestion('Confirmar baja', 
    '¿Está seguro de seguir con el proceso?',
                                        icon='warning')
    if confirmar == 'yes':
        if validaMensajeExito(pCedula, visitantes):
            messagebox.showinfo('Baja realizada', 
            'El visitante ha sido dado de baja.')
        return darBajaVisitAux(pCedula, visitantes)
    else:
        messagebox.showinfo('Baja no realizada', 'El visitante no ha sido dado de baja.')

def darBajaVent(ventanaMain):
    """
    Funcionalidad: ventana que permite dar de baja
    Entrada: ventanaMain (CTK)
    Salida: llamar a confirmarBaja(pCedula) o mensaje retroalimentación
    """
    darBajaVent = ctk.CTkToplevel(ventanaMain)
    darBajaVent.geometry("400x200")
    darBajaVent.title("Dar de baja")
    titulo = ctk.CTkLabel(darBajaVent, text="Dar de baja", 
    text_font=fuenteTitulo)
    titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    subTitulo = ctk.CTkLabel(darBajaVent, 
    text="Digite el número de cédula: ",
    text_font=fuenteBotones)
    subTitulo.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    cantEntry = ctk.CTkEntry(master=darBajaVent,
                               placeholder_text="Cédula",
                               width=125,
                               height=35,
                               border_width=2,
                               corner_radius=10)
    cantEntry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
    botonBaja = ctk.CTkButton(master=darBajaVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Baja",
                                 command=lambda: 
                                 confirmarBaja(cantEntry.get()))
    botonBaja.place(relx=0.30, rely=0.7, anchor=tk.CENTER)
    botonSalir = ctk.CTkButton(master=darBajaVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Regresar",
                                 command=darBajaVent.destroy)
    botonSalir.place(relx=0.70, rely=0.7, anchor=tk.CENTER)

# Ventana 7. Reportes
def cambiarOpcionInt(pOpcion):
    """
    Funcionalidad: cambia la opción en str a un dígito
                   para ser manipulado
    Entrada: pOpcion (str)
    Salida: posición de pOpcion en la lista reportes
    """
    return reportes.index(pOpcion)

def reporteVisitanteVent(visitantes, ventanaMain):
    """
    Funcionalidad: ventana para crear reportes visitante
    Entrada: visitantes (list) 
             ventanaMain (CTK)
    Salida: reporteVisitanteAux(cantEntry.get(), visitantes, diccAstros)
            (archivo HTML) / retroalimentación
    """
    reporteVisitanteVent = ctk.CTkToplevel(ventanaMain)
    reporteVisitanteVent.geometry("400x200")
    reporteVisitanteVent.title("Reporte visitante")
    titulo = ctk.CTkLabel(reporteVisitanteVent, 
    text="Reporte visitante", text_font=fuenteTitulo)
    titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    subTitulo = ctk.CTkLabel(reporteVisitanteVent, 
    text="Digite el número de cédula:",
    text_font=fuenteBotones)
    subTitulo.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    cantEntry = ctk.CTkEntry(master=reporteVisitanteVent,
                               placeholder_text="Cédula",
                               width=125,
                               height=35,
                               border_width=2,
                               corner_radius=10)
    cantEntry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
    botonReporte = ctk.CTkButton(master=reporteVisitanteVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Crear",
                                 command=lambda: 
                                 reporteVisitanteAux(cantEntry.get(), 
                                 visitantes, diccAstros))
    botonReporte.place(relx=0.30, rely=0.7, anchor=tk.CENTER)
    botonSalir = ctk.CTkButton(master=reporteVisitanteVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Regresar",
                                 command=reporteVisitanteVent.destroy)
    botonSalir.place(relx=0.70, rely=0.7, anchor=tk.CENTER)

def reporteAstrosRangoVent(diccAstros, ventanaMain):
    """
    Funcionalidad: ventana para crear reportes astrónomos en rango nacimiento
    Entrada: diccAstros (dict) 
             ventanaMain (CTK)
    Salida: reporteAstrosRangoAux(diccAstros, 
            annoUnoEntry.get(), annoDosEntry.get())
            (archivo HTML) / retroalimentación
    """
    reporteAstrosRangoVent = ctk.CTkToplevel(ventanaMain)
    reporteAstrosRangoVent.geometry("400x200")
    reporteAstrosRangoVent.title("Reporte astrónomos")
    titulo = ctk.CTkLabel(reporteAstrosRangoVent, 
    text="Reporte astrónomos según nacimiento", 
    text_font=fuenteTitulo)
    titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    subTitulo = ctk.CTkLabel(reporteAstrosRangoVent, 
    text="Digite el rango de nacimiento: ",
    text_font=fuenteBotones)
    subTitulo.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    annoUnoEntry = ctk.CTkEntry(master=reporteAstrosRangoVent,
                               placeholder_text="Primer año",
                               width=125,
                               height=35,
                               border_width=2,
                               corner_radius=10)
    annoUnoEntry.place(relx=0.30, rely=0.45, anchor=tk.CENTER)
    annoDosEntry = ctk.CTkEntry(master=reporteAstrosRangoVent,
                               placeholder_text="Último año",
                               width=125,
                               height=35,
                               border_width=2,
                               corner_radius=10)
    annoDosEntry.place(relx=0.70, rely=0.45, anchor=tk.CENTER)
    botonReporte = ctk.CTkButton(master=reporteAstrosRangoVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Crear",
                                 command=lambda: reporteAstrosRangoAux(diccAstros, 
                                 annoUnoEntry.get(), annoDosEntry.get()))
    botonReporte.place(relx=0.30, rely=0.7, anchor=tk.CENTER)
    botonSalir = ctk.CTkButton(master=reporteAstrosRangoVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Regresar",
                                 command=reporteAstrosRangoVent.destroy)
    botonSalir.place(relx=0.70, rely=0.7, anchor=tk.CENTER)

def reporteBibliotecaTipoVent(visitantes, ventanaMain):
    """
    Funcionalidad: ventana para crear reportes de biblioteca
                   por tipo
    Entrada: visitantes (list) 
             ventanaMain (CTK)
    Salida: reporteAstrosRangoAux(diccAstros, 
            annoUnoEntry.get(), annoDosEntry.get())
            (archivo HTML) / retroalimentación
    """
    reporteBibliotecaTipoVent = ctk.CTkToplevel(ventanaMain)
    reporteBibliotecaTipoVent.geometry("400x200")
    reporteBibliotecaTipoVent.title("Reporte biblioteca tipo")
    titulo = ctk.CTkLabel(reporteBibliotecaTipoVent, 
    text="Reporte biblioteca según tipo", 
    text_font=fuenteTitulo)
    titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    subTitulo = ctk.CTkLabel(reporteBibliotecaTipoVent, 
    text="Presione el tipo de contenido que desea:",
    text_font=fuenteBotones)
    subTitulo.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    opcionTipo = ctk.StringVar(value="image")
    imagenTipo = ctk.CTkRadioButton(master=reporteBibliotecaTipoVent, text="Imagen",
                                    variable= opcionTipo, value="image")
    imagenTipo.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    videoTipo = ctk.CTkRadioButton(master=reporteBibliotecaTipoVent, text="Video",
                                    variable= opcionTipo, value="video")
    videoTipo.place(relx=0.5, rely=0.525, anchor=tk.CENTER)
    botonReporte = ctk.CTkButton(master=reporteBibliotecaTipoVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Crear",
                                 command=lambda: reporteBibliotecaTipo(opcionTipo.get(), visitantes))
    botonReporte.place(relx=0.3, rely=0.7, anchor=tk.CENTER)
    botonSalir = ctk.CTkButton(master=reporteBibliotecaTipoVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Regresar",
                                 command=reporteBibliotecaTipoVent.destroy)
    botonSalir.place(relx=0.70, rely=0.7, anchor=tk.CENTER)

def devuelveReporte(pOpcion, ventanaMain):
    """
    Funcionalidad: devuelve una de las funciones de reportes
                   según la opción seleccionada
    Entrada: pOpcion (int) 
             ventanaMain (CTK)
    Salida: llama a las funciones de ventana para crear un reporte o
            lo crea directamente
    """
    global visitantes, diccAstros, visitantesLleno
    if pOpcion == 0:
        return reporteVisitanteVent(visitantes, ventanaMain)
    elif pOpcion == 1:
        messagebox.showinfo("Reporte creado", 
        "El reporte estadísticas de astrónomos ha sido creado.")
        return reporteStatsAstros(visitantes, diccAstros)
    elif pOpcion == 2:
        messagebox.showinfo("Reporte creado", 
        "El reporte biblioteca digital ha sido creado.")
        return reporteBiblioteca(visitantesLleno)
    elif pOpcion == 3:
        return reporteAstrosRangoVent(diccAstros, ventanaMain)
    elif pOpcion == 4:
        messagebox.showinfo("Reporte creado", 
        "El reporte visitantes dados de baja ha sido creado.")
        return reporteVisitBaja(visitantes)
    else:
        return reporteBibliotecaTipoVent(visitantes, ventanaMain)

def reportesVent(ventanaMain):
    """
    Funcionalidad: ventana con las opciones de reportes para crearlos
    Entrada: ventanaMain (CTK)
    Salida: devuelveReporte(cambiarOpcionInt(opcionReportes.get()), ventanaMain) (HTML)
    """
    reportesVent = ctk.CTkToplevel(ventanaMain)
    reportesVent.geometry("400x200")
    reportesVent.title("Reportes")
    titulo = ctk.CTkLabel(reportesVent, text="Reportes HTML", text_font=fuenteTitulo)
    titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    subTitulo = ctk.CTkLabel(reportesVent, 
    text="Seleccione el reporte que quiere obtener",
    text_font=fuenteBotones)
    subTitulo.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    opcionReportes = ctk.StringVar(value="Visitantes dados de baja")
    opcionesSeleccion = ctk.CTkComboBox(master=reportesVent,
                                width=200, height=32,
                                values=reportes,
                                variable=opcionReportes)
    opcionesSeleccion.place(relx=0.50, rely=0.4, anchor=tk.CENTER)
    botonReporte = ctk.CTkButton(master=reportesVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Crear",
                                 command=lambda: devuelveReporte(cambiarOpcionInt(opcionReportes.get()), ventanaMain))
    botonReporte.place(relx=0.30, rely=0.7, anchor=tk.CENTER)
    botonSalir = ctk.CTkButton(master=reportesVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Regresar",
                                 command=reportesVent.destroy)
    botonSalir.place(relx=0.70, rely=0.7, anchor=tk.CENTER)

# Bloque/Desbloqueo botones
def bloqueoImpAstros(pOpcion, ventMain, diccAstros):
    """
    Funcionalidad: bloquea los botones 2, 3, 5 si el 1,
                   no ha sido activado o el diccAstros está vacío
    Entrada: ventMain (CTK)
             pOpcion (int)
             diccAstros (dict)
    Salida: retorna la función de acuerdo a la opción
    """
    if len(diccAstros) == 0:
        return messagebox.showinfo("Bloqueo importar astrónomos", 
        "Debe primero importar los astrónomos para acceder a esta opción.")
    elif pOpcion == 2:
        return 2 # Función de cada uno
    elif pOpcion == 3:
        return 3
    else:
        return darBajaVent(ventMain)

def bloqueoVisitantes(pOpcion, ventMain):
    """
    Funcionalidad: bloquea los botones 4, 5 y 7, si el 2 y 3
                   no ha sido activado o el diccAstros está vacío
    Entrada: ventMain (CTK)
             pOpcion (int)
    Salida: retorna la función de acuerdo a la opción
    """
    global diccAstros, visitantes
    if crearVisitantes[0] == False or crearVisitantes[1] == False:
        messagebox.showinfo("Bloqueo visitantes", 
        "Debe primero crear los visitantes del botón 2 y 3.")
    elif pOpcion == 4:
        messagebox.showinfo("Astrónomos fans", 
        "Los astrónomos han sido agregados exitosamente.")
        return asignarAstroFans(visitantes, diccAstros)
    elif pOpcion == 5:
        return 5
    else:
        return reportesVent(ventMain)

# Ventana menú
def menuVentana():
    """
    Funcionalidad: despliega la ventana con el menú principal
    Entrada: N/A
    Salida: retorna la función de acuerdo a la opción presionada
            por el botón
    """
    global diccAstros, visitantes
    app = ctk.CTk()
    app.geometry(f"{525}x{515}")
    app.title("AstronoTEC")
    titulo = tk.StringVar(value="AstronoTEC")
    tituloLabel = ctk.CTkLabel(master=app,
                               textvariable=titulo,
                               text_color="white",
                               text_font=("Helvetica",35))
    tituloLabel.grid(row = 0, column = 0, columnspan=2)
    subTitulo = tk.StringVar(value="Opciones")
    subTituloLabel = ctk.CTkLabel(master=app,
                               textvariable=subTitulo,
                               text_color="white",
                               text_font=("Helvetica", 15))
    subTituloLabel.grid(row = 1, column = 0, columnspan=2)
    espacioLabel = tk.StringVar(value="------------------------------------")
    espacioLabel = ctk.CTkLabel(master=app,
                                    textvariable=espacioLabel,
                                    text_font=("Helvetica", 30))    
    espacioLabel.grid(row = 2, column = 0, columnspan=2)
    boton1 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotonesMenu,
                                 text="1. Importar astrónomos",
                                 command=lambda: impAstrosVent(app))
    boton1.grid(row = 3, column = 0, padx=5, pady=5, ipadx=15, ipady=10)
    boton2 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotonesMenu,
                                 text="2. Crear un visitante",
                                 command=lambda: bloqueoImpAstros(2, app, diccAstros))
    boton2.grid(row =3, column = 1, padx=5, pady=5, ipadx=15, ipady=10)
    boton3 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotonesMenu,
                                 text="3. Crear BD de visitantes",
                                 command=lambda: bloqueoImpAstros(3, app, diccAstros))
    boton3.grid(row = 4, column = 0, padx=5, pady=5, ipadx=15, ipady=10)
    boton4 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotonesMenu,
                                 text="4. Asignar Astrónomos Fans",
                                 command=lambda: bloqueoVisitantes(4, app))
    boton4.grid(row = 4, column=1, padx=5, pady=5, ipadx=15, ipady=10)
    boton5 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotonesMenu,
                                 text="5. Cargar biblioteca digital",
                                 command=lambda: bloqueoVisitantes(5, app))
    boton5.grid(row = 5, column=0, padx=5, pady=5, ipadx=15, ipady=10)
    boton6 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotonesMenu,
                                 text="6. Dar de baja",
                                 command=lambda: bloqueoImpAstros(6, app, diccAstros))
    boton6.grid(row = 5, column=1, padx=5, pady=5, ipadx=15, ipady=10)
    boton7 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotonesMenu,
                                 text="7. Reportes",
                                 command=lambda: bloqueoVisitantes(7, app))
    boton7.grid(row = 6, column=0, padx=5, pady=5, ipadx=15, ipady=15, columnspan=2)
    espacioLabel = tk.StringVar(value="------------------------------------")
    espacioLabel = ctk.CTkLabel(master=app,
                                    textvariable=espacioLabel,
                                    text_font=("Helvetica", 30))    
    espacioLabel.grid(row = 7, column = 0, columnspan=2)
    boton8 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotonesMenu,
                                 text="Salir",
                                 command=lambda: app.destroy())
    boton8.grid(row = 8, column=0, padx=5, pady=5, ipadx=15, ipady=15, columnspan=2)
    app.mainloop()

menuVentana()