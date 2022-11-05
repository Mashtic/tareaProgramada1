# Creado por: Ian Steven Coto Soto
# Fecha de creación: 03/11/2022 11:00 am
# Última modificación: 04/11/2022 XX:XX pm
# Versión: 3.10.8

# Importar librerías
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from funciones import *
from validaciones import *
from entradas import *

# Funciones globales
crearVisitantes = (True, True)
reportes = ["Perfil de un visitante", "Estadística de astrónomos",
                            "Mostrar biblioteca digital", "Reporte de astrónomos", 
                            "Visitantes dados de baja", "Recurso por tipo"]
diccAstros = {}

#------------ Ventanas ------------#
# Ventana 1. Importar astrónomos

def limpiarDiccAstros(diccAstros):
    messagebox.showinfo("Astrónomos vaciados", "Se ha limpiado los astrónomos."
    "0 astrónomos actualmente")
    return diccAstros.clean()

def impAstrosVent(ventanaMain):
    global diccAstros
    impAstrosVent = ctk.CTkToplevel(ventanaMain)
    impAstrosVent.geometry("400x200")
    impAstrosVent.title("1. Importar astrónomos")
    titulo = ctk.CTkLabel(impAstrosVent, text="Importar astrónomos", text_font=("Helvetica", 20))
    titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    subTitulo = ctk.CTkLabel(impAstrosVent, 
    text="Ingrese la cantidad de astrónomos que desea importar: ",
    text_font=("Helvetica", 8))
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
                                 text_font=("Helvetica", 14),
                                 text="Extraer",
                                 command=lambda: crearDiccAstronomosAux(cantEntry.get(), diccAstros))
    botonExtraer.place(relx=0.30, rely=0.7, anchor=tk.CENTER)
    botonLimpiar = ctk.CTkButton(master=impAstrosVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="Limpiar",
                                 command=lambda: limpiarDiccAstros(diccAstros))
    botonLimpiar.place(relx=0.70, rely=0.7, anchor=tk.CENTER)
    botonSalir = ctk.CTkButton(master=impAstrosVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="Regresar",
                                 command=lambda: impAstrosVent.destroy())
    botonSalir.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Ventana 6. Dar de baja
def confirmarBaja(pCedula):
    confirmar = messagebox.askquestion('Confirmación baja', '¿Está seguro de seguir con el proceso?',
                                        icon='warning')
    if confirmar == 'yes':
        if validaMensajeExito(pCedula, visitantes):
            messagebox.showinfo('Baja realizada', 'El visitante ha sido dado de baja.')
        return darBajaVisitAux(pCedula, visitantes)
    else:
        messagebox.showinfo('Baja no realizada', 'El visitante no ha sido dado de baja.')

def darBajaVent(ventanaMain):
    darBajaVent = ctk.CTkToplevel(ventanaMain)
    darBajaVent.geometry("400x200")
    darBajaVent.title("6. Dar de baja")
    titulo = ctk.CTkLabel(darBajaVent, text="Dar de baja", text_font=("Helvetica", 20))
    titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    subTitulo = ctk.CTkLabel(darBajaVent, 
    text="Digite el número de cédula: ",
    text_font=("Helvetica", 12))
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
                                 text_font=("Helvetica", 12),
                                 text="Baja",
                                 command=lambda: confirmarBaja(cantEntry.get()))
    botonBaja.place(relx=0.30, rely=0.7, anchor=tk.CENTER)
    botonSalir = ctk.CTkButton(master=darBajaVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="Regresar",
                                 command=darBajaVent.destroy)
    botonSalir.place(relx=0.70, rely=0.7, anchor=tk.CENTER)

# Ventana 7. Reportes
def cambiarOpcionInt(pOpcion):
    return reportes.index(pOpcion)

def devuelveReporte(pOpcion):
    global visitantes
    if pOpcion == 0:
        return # Ventana
    elif pOpcion == 1:
        messagebox.showinfo("Reporte creado", "El reporte estadísticas de astrónomos ha sido creado.")
        return reporteStatsAstros(visitantes)
    elif pOpcion == 2:
        messagebox.showinfo("Reporte creado", "El reporte biblioteca digital ha sido creado.")
        return reporteBiblioteca(visitantes)
    elif pOpcion == 3:
        messagebox.showinfo("Reporte creado", "El reporte reporte de astrónomos ha sido creado.")
        return # Ventana
    elif pOpcion == 4:
        messagebox.showinfo("Reporte creado", "El reporte visitantes dados de baja ha sido creado.")
        return # Ventana
    else:
        return # Ventana

def reportesVent(ventanaMain):
    reportesVent = ctk.CTkToplevel(ventanaMain)
    reportesVent.geometry("400x200")
    reportesVent.title("7. Reportes")
    titulo = ctk.CTkLabel(reportesVent, text="Reportes", text_font=("Helvetica", 20))
    titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    subTitulo = ctk.CTkLabel(reportesVent, 
    text="Seleccione el reporte que quiere obtener",
    text_font=("Helvetica", 12))
    subTitulo.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    opcionReportes = ctk.StringVar(value="Visitantes dados de baja")  # set initial value
    opcionesSeleccion = ctk.CTkComboBox(master=reportesVent,
                            values=reportes,
                            variable=opcionReportes)
    opcionesSeleccion.place(relx=0.50, rely=0.4, anchor=tk.CENTER)
    botonReporte = ctk.CTkButton(master=reportesVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="Crear / Ir",
                                 command=lambda: devuelveReporte(cambiarOpcionInt(opcionReportes.get())))
    botonReporte.place(relx=0.30, rely=0.7, anchor=tk.CENTER)
    botonSalir = ctk.CTkButton(master=reportesVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="Regresar",
                                 command=reportesVent.destroy)
    botonSalir.place(relx=0.70, rely=0.7, anchor=tk.CENTER)

# Bloque/Desbloqueo botones
def bloqueoImpAstros(pOpcion, ventMain, diccAstros):
    if len(diccAstros) == 0:
        messagebox.showinfo("Bloqueo importar astrónomos", "Debe primero importar los astrónomos para acceder a esta opción")
    elif pOpcion == 2:
        return 2 # Función de cada uno
    elif pOpcion == 3:
        return 3
    else:
        return darBajaVent(ventMain)

def bloqueoVisitantes(pOpcion, ventMain):
    global diccAstros, visitantes
    crearVisitantes = (True, True)
    if crearVisitantes[0] == False or crearVisitantes[1] == False:
        messagebox.showinfo("Bloqueo visitantes", "Debe primero crear los visitantes del botón 2 y 3")
    elif pOpcion == 4:
        messagebox.showinfo("Astrónomos fans", "Los astrónomos han sido agregados exitosamente")
        return asignarAstroFans(visitantes, diccAstros)
    elif pOpcion == 5:
        return 5
    else:
        return reportesVent(ventMain)

# Ventana menú
def menuVentana():
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
                                 text_font=("Helvetica", 12),
                                 text="1. Importar astrónomos",
                                 command=lambda: impAstrosVent(app))
    boton1.grid(row = 3, column = 0, padx=5, pady=5, ipadx=15, ipady=10)
    boton2 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="2. Crear un visitante",
                                 command=lambda: bloqueoImpAstros(2, app, diccAstros))
    boton2.grid(row =3, column = 1, padx=5, pady=5, ipadx=15, ipady=10)
    boton3 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="3. Crear BD de visitantes",
                                 command=lambda: bloqueoImpAstros(3, app, diccAstros))
    boton3.grid(row = 4, column = 0, padx=5, pady=5, ipadx=15, ipady=10)
    boton4 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="4. Asignar Astrónomos Fans",
                                 command=lambda: bloqueoVisitantes(4, app))
    boton4.grid(row = 4, column=1, padx=5, pady=5, ipadx=15, ipady=10)
    boton5 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="5. Cargar biblioteca digital",
                                 command=lambda: bloqueoVisitantes(5, app))
    boton5.grid(row = 5, column=0, padx=5, pady=5, ipadx=15, ipady=10)
    boton6 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="6. Dar de baja",
                                 command=lambda: bloqueoImpAstros(6, app, diccAstros))
    boton6.grid(row = 5, column=1, padx=5, pady=5, ipadx=15, ipady=10)
    boton7 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
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
                                 text_font=("Helvetica", 12),
                                 text="Salir",
                                 command=lambda: print(len(diccAstros), visitantes))
    boton8.grid(row = 8, column=0, padx=5, pady=5, ipadx=15, ipady=15, columnspan=2)
    app.mainloop()

menuVentana()