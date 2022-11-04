# Creado por: Ian Steven Coto Soto
# Fecha de creación: 03/11/2022 11:00 am
# Última modificación: 03/11/2022 10:20 pm
# Versión: 3.10.8

# Importar librerías
import tkinter as tk
import customtkinter as ctk

# Ventanas
def menuVentana():
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
                                 command=lambda: print(1))
    boton1.grid(row = 3, column = 0, padx=5, pady=5, ipadx=15, ipady=10)
    boton2 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="2. Crear un visitante",
                                 command=lambda: print(2))
    boton2.grid(row =3, column = 1, padx=5, pady=5, ipadx=15, ipady=10)
    boton3 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="3. Crear BD de visitantes",
                                 command=lambda: print(3))
    boton3.grid(row = 4, column = 0, padx=5, pady=5, ipadx=15, ipady=10)
    boton4 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="4. Asignar Astrónomos Fans",
                                 command=lambda: print(4))
    boton4.grid(row = 4, column=1, padx=5, pady=5, ipadx=15, ipady=10)
    boton5 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="5. Cargar biblioteca digital",
                                 command=lambda: print(5))
    boton5.grid(row = 5, column=0, padx=5, pady=5, ipadx=15, ipady=10)
    boton6 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="6. Dar de baja",
                                 command=lambda: print(6))
    boton6.grid(row = 5, column=1, padx=5, pady=5, ipadx=15, ipady=10)
    boton7 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=("Helvetica", 12),
                                 text="7. Reportes",
                                 command=lambda: print(7))
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
                                 command=lambda: print("Bye"))
    boton8.grid(row = 8, column=0, padx=5, pady=5, ipadx=15, ipady=15, columnspan=2)
    app.mainloop()

menuVentana()