from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import time

class VistaMinijuego:

    # Constructor ventana root
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina el número secreto 🕹️")

        self.root.geometry("1000x640")

        # Agregar imagen de fondo
        image_original = Image.open("Diseño/fondoJuego2.png").resize((1000, 640))
        image_tk = ImageTk.PhotoImage(image_original)

        # Configurar imagen de fondo
        self.label_imagen = tk.Label(root, image=image_tk)
        self.label_imagen.imagen = image_tk
        self.label_imagen.pack()

    def iniciar_juego(self):
        return
    
    # Configuar el menú principal
    def menu(self):
        # Configurar blackground
        self.menu_frame = tk.Frame(self.root)

        self.menu_frame.config(width=300,
            height=250)
        
        self.menu_frame.place(x=350, y=340)
        self.menu_frame.pack_propagate(False)

        # Configurar imagen de fondo de los botones
        imagen_original = Image.open("Diseño/texturaMenu.jpg").resize((300, 40))
        image_tk = ImageTk.PhotoImage(imagen_original)

        self.menu = tk.Label(self.menu_frame,
                             text="⚔ MENÚ DE JUEGO", font=18, fg="white",
                             image=image_tk,
                             compound="center",
                             border=3, bg="dark slate blue")
        self.menu.pack()

        # Crear botones
        self.b_jugar = tk.Button(self.menu_frame,
                                 text="Nueva Partida", font=16, fg="white",
                                 border=3, bg="dark slate blue",
                                 image=image_tk,
                                 compound="center",
                                 command=self.iniciar_juego())
        self.b_jugar.image = image_tk
        self.b_jugar.pack(fill="x")

        self.b_top = tk.Button(self.menu_frame,
                               text="Ver TOP 5", font=16, fg="white",
                                 border=3, bg="dark slate blue",
                                 image=image_tk,
                                 compound="center",
                               command=self.ver_top_5())
        self.b_top.image = image_tk
        self.b_top.pack(fill="x")

        self.b_reiniciar = tk.Button(self.menu_frame,
                                     text="Reiniciar archivos", font=16, fg="white",
                                 border=3, bg="dark slate blue",
                                 image=image_tk,
                                 compound="center",
                                     command=self.reiniciar_archivos())
        self.b_reiniciar.image = image_tk
        self.b_reiniciar.pack(fill="x")

        self.b_salir = tk.Button(self.menu_frame,
                                 text="Salir", font=16, fg="white",
                                 border=3, bg="dark slate blue",
                                 image=image_tk,
                                 compound="center",
                                 command=self.salir())
        self.b_salir.image = image_tk
        self.b_salir.pack(fill="x")

    def reiniciar_archivos(self):
        return
    
    def salir(self):
        self.fm_close = tk.Frame(self.root)
        self.fm_close.config(width=460,
            height=300,
            bg="DarkOrchid4",
            relief="sunken")
        
        self.barra = ttk.Progressbar(self.fm_close, orient="horizontal", mode="indeterminate", length=250)
        self.barra.pack(400)
        time.sleep(2)

        self.root.destroy()
        return
    
    def ver_top_5(self):
        return