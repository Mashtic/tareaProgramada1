# Creado por: Ian Steven Coto Soto
# Fecha de creación: 03/11/2022 11:00 am
# Última modificación: 03/11/2022 11:25 am
# Versión: 3.10.8

# Importar librerías
import tkinter as tk
import customtkinter as ctk
# Ventanas

def menuVentana():
    app = ctk.CTk()
    app.geometry(f"{600}x{500}")
    app.title("AstronoTEC")
    titulo = tk.StringVar(value="AstronoTEC")
    tituloLabel = ctk.CTkLabel(master=app,
                               textvariable=titulo,
                               text_color="white",
                               text_font=("Helvetica", 40))
    tituloLabel.grid(row = 0, column = 0, padx=2)
    subTitulo = tk.StringVar(value="Opciones")
    subTituloLabel = ctk.CTkLabel(master=app,
                               textvariable=subTitulo,
                               text_color="white",
                               text_font=("Helvetica", 20))
    subTituloLabel.grid(row = 1, column = 0, padx=2)
    boton1 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="1. Importar astrónomos",
                                 command=lambda: print(1))
    boton1.grid(row = 2, column = 0)
    boton2 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="2. Crear un visitante",
                                 command=lambda: print(2))
    boton2.grid(row = 2, column = 1)
    boton3 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="3. Crear BD de visitantes",
                                 command=lambda: print(3))
    boton3.grid(row = 3, column = 0)
    boton4 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="4. Asignar Astrónomos Fans",
                                 command=lambda: print(4))
    boton4.grid(row = 3, column = 1)
    
    app.mainloop()

menuVentana()