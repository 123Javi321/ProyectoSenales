# Grupo 1
# Librerias a utilizar
# import numpy as np
# Libreria para analizar señales
# prueba1
import os
from tkinter import *
from tkinter import messagebox, Tk, Button, Label, PhotoImage
from thinkdsp import read_wave
from tkinter import filedialog
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import pygame
from PIL import Image, ImageTk

pygame.mixer.init()
m1 = None
m2 = None
m3 = None
w1 = None
w2 = None
w3 = None
wO = None
wF = None
spec = None
af1 = None
co1 = None
v1 = None

# Clase para los graficos
class ventanaGraficos:
    def __init__(self):
        global wO, wF, spec, af1
        ventanaGraficos = Toplevel()
        ventanaGraficos.geometry("700x450")
        ventanaGraficos.title("Graficas")

        ventanaGraficos.etiqueta = Label(ventanaGraficos, text="Seleccione la grafica que desea ver: ",font=('Comic Sans', 16))
        ventanaGraficos.etiqueta.pack(pady=20)

        ventanaGraficos.botonG1 = Button(ventanaGraficos, text="Gráfico en dominio del tiempo sin filtrar",command=self.G1, width=40)
        ventanaGraficos.botonG1.place(x=60, y=60)

        ventanaGraficos.botonG2 = Button(ventanaGraficos, text="Gráfico en dominio de la frecuencia sin filtrar",command=self.G2, width=40)
        ventanaGraficos.botonG2.place(x=60, y=160)

        ventanaGraficos.botonG3 = Button(ventanaGraficos, text="Gráfico en dominio del tiempo filtrado",command=self.G3, width=40)
        ventanaGraficos.botonG3.place(x=360, y=60)

        ventanaGraficos.botonG4 = Button(ventanaGraficos, text="Gráfico en dominio de la frecuencia filtrado",command=self.G4, width=40)
        ventanaGraficos.botonG4.place(x=360, y=160)

        ventanaGraficos.botonS1 = Button(ventanaGraficos, text="Audio sin filtrar", command=self.S1, width=40)
        ventanaGraficos.botonS1.place(x=60, y=260)

        ventanaGraficos.botonS2 = Button(ventanaGraficos, text="Audio filtrado", command=self.S2, width=40)
        ventanaGraficos.botonS2.place(x=360, y=260)

        ventanaGraficos.botonRegresar = Button(ventanaGraficos, text="Regresar", command=self.R, width=20)
        ventanaGraficos.botonRegresar.place(x=280, y=360)

    def G1(self):
        print("Grafico 1")
        fig1 = plt.figure()
        global wO
        wog = wO
        wog.plot()
        plt.draw()
        plt.show()

    def G2(self):
        print("Grafico 2")
        global wO
        fig2 = plt.figure()
        spec1 = wO.make_spectrum()
        spec1.plot()
        plt.draw()
        plt.show()
        # pygame.mixer.music.load(wO)
        # pygame.mixer.music.play(loops=0)

    def G3(self):
        print("Grafico 3")
        fig3 = plt.figure()
        global wF, spec, af1
        af1 = spec.make_wave()
        af1.plot()
        plt.draw()
        plt.show()

    def G4(self):
        print("Grafico 4")
        fig3 = plt.figure()
        global wF, spec
        spec.plot()
        plt.draw()
        plt.show()

    def S1(self):
        print("Audio og")
        if (optAudio == 1):
            pygame.mixer.music.load(m1)
            pygame.mixer.music.play(loops=0)
        elif (optAudio == 2):
            pygame.mixer.music.load(m2)
            pygame.mixer.music.play(loops=0)
        elif (optAudio == 3):
            pygame.mixer.music.load(m3)
            pygame.mixer.music.play(loops=0)

    def S2(self):
        print("Audio filtrado")
        global wF, spec, af1
        af1 = spec.make_wave()
        af1.play()

    def R(self):
        print("Regresar")


# Clase para los filtros
class ventanaFiltros:
    def __init__(self):
        global m1, m2, m3, optAudio, v1
        ventanaFiltros = Toplevel()
        ancho_ventana = 610
        alto_ventana = 340

        x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        ventanaFiltros.geometry(posicion)

        ventanaFiltros.title("Seleccionar filtro")

        imgsalir = PhotoImage(file="Salir.png")

        ventanaFiltros.etiqueta = Label(ventanaFiltros, text="Seleccione el filtro para aplicar: ", font=('Comic Sans', 16))
        ventanaFiltros.etiqueta.place(x=100, y=20)

        ventanaFiltros.botonLP = Button(ventanaFiltros, text="Pasa bajos", command=lambda: [self.SeleccionadorAudio(), self.LP(),ventanaFiltros.destroy()], width=30)
        ventanaFiltros.botonLP.place(x=50, y=70)
        ventanaFiltros.entry1 = Entry(ventanaFiltros, width=10)
        ventanaFiltros.entry1.place(x=300, y=70)

        ventanaFiltros.botonHP = Button(ventanaFiltros, text="Pasa altos", command=lambda: [self.SeleccionadorAudio(), self.HP(), ventanaFiltros.destroy()], width=30)
        ventanaFiltros.botonHP.place(x=50, y=120)
        ventanaFiltros.entry2 = Entry(ventanaFiltros, width=10)
        ventanaFiltros.entry2.place(x=300, y=120)

        ventanaFiltros.botonBP = Button(ventanaFiltros, text="Pasa banda", command=lambda: [self.SeleccionadorAudio(), self.BP(), ventanaFiltros.destroy()], width=30)
        ventanaFiltros.botonBP.place(x=50, y=170)
        ventanaFiltros.entry3a = Entry(ventanaFiltros, width=10)
        ventanaFiltros.entry3a.place(x=300, y=170)
        ventanaFiltros.entry3b = Entry(ventanaFiltros, width=10)
        ventanaFiltros.entry3b.place(x=400, y=170)

        ventanaFiltros.botonE = Button(ventanaFiltros, text="Estudio de grabación", command=lambda: [self.SeleccionadorAudio(), self.E(), ventanaFiltros.destroy()], width=30)
        ventanaFiltros.botonE.place(x=50, y=220)
        ventanaFiltros.entry4 = Entry(ventanaFiltros, width=10)
        ventanaFiltros.entry4.place(x=300, y=220)
        ventanaFiltros.botonsalir = Button(ventanaFiltros, image=imgsalir, command=ventanaFiltros.quit, width=100, height=20).place(x=245, y=300)

    # Metodo para definir el audio normalizado
    def SeleccionadorAudio(self):
        global w1, w2, w3, wO, wF, optAudio
        if (optAudio == 1):
            wO = w1
            wF = w1
        elif (optAudio == 2):
            wO = w2
            wF = w2
        elif (optAudio == 3):
            wO = w3
            wF = w3

    # Metodo para el filtro pasa bajos
    def LP(self):
        global wF, spec
        print('Pasa bajos')
        spec = wF.make_spectrum()
        # Necesita solo 1 frecuencia de corte
        spec.low_pass()
        ventanaGraficos()

    # Metodo para el filtro pasa altos
    def HP(self):
        global wF, spec
        print('Pasa altos')
        spec = wF.make_spectrum()
        # Necesita solo 1 frecuencia de corte
        spec.high_pass()
        ventanaGraficos()

    # Metodo para el filtro pasa banda
    def BP(self):
        global wF, spec
        print('Pasa banda')
        spec = wF.make_spectrum()
        # Necesita 2 frecuencias de corte
        spec.band_stop()
        ventanaGraficos()

    # Metodo para el filtro eliminación
    def E(self):
        global wF, spec
        print('Estudio de grabacion')

        # El filtro aquí es por convolucion con Numpy
        ventanaGraficos()


# Clase para elegir los audios
class ventanaAudios:
    def __init__(self):
        ventanaAudios = Toplevel()
        ancho_ventana = 610
        alto_ventana = 340

        x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        ventanaAudios.geometry(posicion)

        bgreproductor = PhotoImage(file="Fondo2.png")
        lblreproductor = Label(ventanaAudios, image=bgreproductor).place(x=0, y=0)
        imgSalir = PhotoImage(file="Salir.png")
        imgpausa = PhotoImage(file="Pausa.png")
        imgplay = PhotoImage(file="play.png")
        imgsel = PhotoImage(file="Seleccionar.png")

        ventanaAudios.title("Seleccionar audio")

        ventanaAudios.etiqueta = Label(ventanaAudios, text="Seleccione el audio para filtrar: ", font=('Comic Sans', 16),
                                       bg='black', fg='white')
        ventanaAudios.etiqueta.pack()
        # Load y play del primer audio
        ventanaAudios.labelA3 = Label(ventanaAudios, text="Reproducir audio 1", font=('Comic Sans', 12), bg='black', fg='white').place(x=30, y=55)
        ventanaAudios.botonA1 = Button(ventanaAudios, image=imgplay, command=lambda: [self.A1()], width=50, height=50).place(x=70, y=85)

        # Load y play del segundo audio
        ventanaAudios.labelA3 = Label(ventanaAudios, text="Reproducir audio 2", font=('Comic Sans', 12), bg='black', fg='white').place(x=230, y=55)
        ventanaAudios.botonA2 = Button(ventanaAudios, image=imgplay, command=lambda: [self.A2()], width=50, height=50).place(x=270, y=85)

        # Load y play del tercer audio
        ventanaAudios.labelA3 = Label(ventanaAudios, text="Reproducir audio 3", font=('Comic Sans', 12), bg='black',fg='white').place(x=430, y=55)
        ventanaAudios.botonA3 = Button(ventanaAudios, image=imgplay, command=lambda: [self.A3()], width=50,height=50).place(x=470, y=85)
        # Ventana para aplicar filtros
        ventanaAudios.botonSel = Button(ventanaAudios, image=imgsel, command=lambda: [self.Sel(),ventanaAudios.destroy()],width=100, height=20).place(x=245, y=258)
        # Pausar el audio que está cargado
        ventanaAudios.label1 = Label(ventanaAudios, text="Pausa", font=('Comic Sans', 12), bg='black',fg='white').place(x=272, y=150)
        ventanaAudios.botonStop = Button(ventanaAudios, image=imgpausa, command=self.St, width=50,height=50).place(x=270, y=180)
        ventanaAudios.botonsalir = Button(ventanaAudios, image=imgSalir, command=ventanaAudios.quit,width=100, height=20).place(x=245, y=300)

        ventanaAudios.labelA1.pack()
        ventanaAudios.botonA1.pack()
        ventanaAudios.labelA2.pack()
        ventanaAudios.botonA2.pack()
        ventanaAudios.labelA3.pack()
        ventanaAudios.botonA3.pack()
        ventanaAudios.botonSel.pack()
        ventanaAudios.label1.pack()
        ventanaAudios.botonsalir.pack()
        ventanaAudios.botonStop.pack()

    # Metodo para el primer audio
    def A1(self):
        global m1, optAudio
        # Lineas para reproducir el audio
        pygame.mixer.music.load(m1)
        pygame.mixer.music.play(loops=0)
        optAudio = 1

        # Metodo para el segundo audio

    def A2(self):
        global m2, optAudio
        # Lineas para reproducir el audio
        pygame.mixer.music.load(m2)
        pygame.mixer.music.play(loops=0)
        optAudio = 2

    # Metodo para el tercer audio
    def A3(self):
        global m3, optAudio
        # Lineas para reproducir el audio
        pygame.mixer.music.load(m3)
        pygame.mixer.music.play(loops=0)
        optAudio = 3

    # Metodo para seleccionar audio
    def Sel(self):
        print(optAudio)
        ventanaFiltros()

    # Metodo para pausar la musica
    def St(self):
        print('Pausa')
        pygame.mixer.music.stop()


# Clase para importar audios
class ventanaImportar:
    def __init__(self):
        # Creacion de nueva ventana para importar audios
        ventanaImportar = Toplevel()
        ancho_ventana = 500
        alto_ventana = 375

        x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        ventanaImportar.geometry(posicion)

        ventanaImportar.title("Importar audios")

        imgB1 = PhotoImage(file="Importar.png")
        imgB2 = PhotoImage(file="Salir.png")
        bgcreds = PhotoImage(file="Fondo.png")
        lblcreds = Label(ventanaImportar, image=bgcreds).place(x=0, y=0)
        ventanaImportar.etiqueta = Label(ventanaImportar, text="Importación de audios", font=('Comic Sans', 16), bg='black',fg='white').place(x=150, y=60)
        ventanaImportar.botonImportar = Button(ventanaImportar, image=imgB1,command=lambda: [self.importar(), ventanaImportar.destroy()], width=100,height=20).place(x=200, y=175)
        ventanaImportar.botonSalir = Button(ventanaImportar, image=imgB2, command=ventanaImportar.quit, width=100,height=20).place(x=200, y=225)

        ventanaImportar.botonSalir.pack()
        ventanaImportar.botonImportar.pack()

    # Metodo para el boton de importar audios
    def importar(self):
        # Pide al usuario ingresar los audios
        global m1, m2, m3, w1, w2, w3
        for i in range(3):
            if (i == 0):
                print('Primer audio')
                # Linea para importar audio
                m1 = filedialog.askopenfilename(title="Selecciona el audio", filetypes=(("Archivos wav", "*.wav"),))
                messagebox.showinfo(title='Importar Audios', message='Has importado el audio 1 correctamente')
                w1 = read_wave(m1)
                print(type(m1))
                w1.normalize()
            elif (i == 1):
                print('Segundo audio')
                # Linea para importar audio
                m2 = filedialog.askopenfilename(title="Selecciona el audio", filetypes=(("Archivos wav", "*.wav"),))
                messagebox.showinfo(title='Importar Audios', message='Has importado el audio 2 correctamente')
                w2 = read_wave(m1)
                w2.normalize()
            elif (i == 2):
                print('Tercer audio')
                # Linea para importar audio
                m3 = filedialog.askopenfilename(title="Selecciona el audio", filetypes=(("Archivos wav", "*.wav"),))
                messagebox.showinfo(title='Importar Audios', message='Has importado el audio 3 correctamente')
                w3 = read_wave(m1)
                w3.normalize()
        ventanaAudios()


# Clase para mostrar los creditos
class ventanaCreditos:
    def __init__(self):
        # Creacion de nueva ventana para creditos
        ventanaCreditos = Toplevel()
        ancho_ventana = 500
        alto_ventana = 375

        x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        ventanaCreditos.geometry(posicion)
        ventanaCreditos.title("Integrantes")

        imgB1 = PhotoImage(file="Volver.png")
        bgcreds = PhotoImage(file="Fondo.png")
        lblcreds = Label(ventanaCreditos, image=bgcreds).place(x=0, y=0)
        ventanaCreditos.etiqueta = Label(ventanaCreditos, text="Grupo #1", font=('Comic Sans', 16)).place(x=200, y=30)
        ventanaCreditos.etiqueta = Label(ventanaCreditos, text="•Javier Castañeda - 1290520", font=('Comic Sans', 12),bg='black', fg='white').place(x=150, y=90)
        ventanaCreditos.etiqueta = Label(ventanaCreditos, text="•Angel Castillo - 1172920 ", font=('Comic Sans', 12),bg='black', fg='white').place(x=150, y=120)
        ventanaCreditos.etiqueta = Label(ventanaCreditos, text="•Andres Coronado - 1168420 ", font=('Comic Sans', 12),bg='black', fg='white').place(x=150, y=150)
        ventanaCreditos.etiqueta = Label(ventanaCreditos, text="•Pablo Flores - 1164720", font=('Comic Sans', 12),bg='black', fg='white').place(x=150, y=180)
        ventanaCreditos.botonVolver = Button(ventanaCreditos, image=imgB1, command=ventanaCreditos.destroy, width=100,height=20).place(x=200, y=240)
        ventanaCreditos.botonVolver.pack()
        ventanaCreditos.etiqueta.pack()


# clase de ventana principal
class VentanaInicio:
    def __init__(self, master):
        self.master = master
        master.title("Inicio - Proyecto ASS - G1")
        ancho_ventana = 500
        alto_ventana = 250

        x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        master.geometry(posicion)

        root.config(bg="black")

        etiqueta = Label(master, text="Proyecto Analisis de Senales y Sistemas", font=('Comic Sans', 16)).place(x=50, y=15)
        botonInicio = Button(master, text="Iniciar", command=self.iniciar, width=20).place(x=175, y=80)
        botonCreditos = Button(master, text="Créditos", command=self.creditos, width=20).place(x=175, y=120)
        botonSalir = Button(master, text="Salir", command=master.quit, width=20).place(x=175, y=160)

    # Metodo para el boton de inicio
    def iniciar(self):
        print('Importar audios')
        # este comando cierra VentanaInicio
        root.withdraw()
        # Llamado a la clase para la ventana de importar audios
        ventanaImportar()

    # Metodo para el boton de creditos
    def creditos(self):
        print('Grupo 1')
        # Creacion de nueva ventana para los creditos
        ventanaCreditos()
    # Metodo para cerrar pestañas


root = Tk()
optAudio = 0
miVentana = VentanaInicio(root)
root.mainloop()
