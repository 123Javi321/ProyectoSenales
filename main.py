#Grupo 1
#Librerias a utilizar
#import numpy as np
#Libreria para analizar señales
#prueba1
import os
from tkinter import *
from tkinter import messagebox
from thinkdsp import read_wave
from tkinter import filedialog
import matplotlib.pyplot as plt
import pygame

pygame.mixer.init()
m1=None
m2=None
m3=None
w1=None
w2=None
w3=None
wO=None
wF=None
#Clase para los graficos
class ventanaGraficos:
    def __init__(self):
        global wO, wF
        ventanaGraficos = Toplevel()
        ventanaGraficos.geometry("700x450")
        ventanaGraficos.title("Graficas")

        ventanaGraficos.etiqueta = Label(ventanaGraficos, text="Seleccione la grafica que desea ver: ", font=('Arial', 16))
        ventanaGraficos.etiqueta.pack(pady=20)

        ventanaGraficos.botonG1 = Button(ventanaGraficos, text="Gráfico en dominio del tiempo sin filtrar", command=self.G1, width=40)
        ventanaGraficos.botonG1.place(x=60, y=60)

        ventanaGraficos.botonG2 = Button(ventanaGraficos, text="Gráfico en dominio de la frecuencia sin filtrar", command=self.G2, width=40)
        ventanaGraficos.botonG2.place(x=60, y=160)

        ventanaGraficos.botonG3 = Button(ventanaGraficos, text="Gráfico en dominio del tiempo filtrado", command=self.G3, width=40)
        ventanaGraficos.botonG3.place(x=360, y=60)

        ventanaGraficos.botonG4 = Button(ventanaGraficos, text="Gráfico en dominio de la frecuencia filtrado", command=self.G4, width=40)
        ventanaGraficos.botonG4.place(x=360, y=160)

        ventanaGraficos.botonS1 = Button(ventanaGraficos, text="Audio sin filtrar", command=self.S1, width=40)
        ventanaGraficos.botonS1.place(x=60, y=260)

        ventanaGraficos.botonS2 = Button(ventanaGraficos, text="Audio filtrado", command=self.S2, width=40)
        ventanaGraficos.botonS2.place(x=360, y=260)

        ventanaGraficos.botonRegresar = Button(ventanaGraficos, text="Regresar", command=self.R, width=20)
        ventanaGraficos.botonRegresar.place(x=280, y=360)

    def G1(self):
        print("Grafico 1")

    def G2(self):
        print("Grafico 2")

    def G3(self):
        print("Grafico 3")
    
    def G4(self):
        print("Grafico 4")

    def S1(self):
        print("Audio og")

    def S2(self):
        print("Audio filtrado")

    def R(self):
        global wO
        spec1 = wO.make_spectrum()
        spec1.plot()
        plt.show()
        pygame.mixer.music.load(wO)
        pygame.mixer.music.play(loops=0)
        print("Regresar")

#Clase para los filtros
class ventanaFiltros:
    def __init__(self):
        global m1,m2,m3,optAudio
        ventanaFiltros = Toplevel()
        ventanaFiltros.geometry("500x350")
        ventanaFiltros.title("Seleccionar filtro")

        ventanaFiltros.etiqueta = Label(ventanaFiltros, text="Seleccione el filtro para aplicar: ", font=('Arial', 16))
        ventanaFiltros.etiqueta.pack(pady=20)

        ventanaFiltros.botonLP = Button(ventanaFiltros, text="Pasa bajos", command=lambda:[self.LP(),ventanaFiltros.destroy(),self.SeleccionadorAudio()], width=20)
        ventanaFiltros.botonLP.pack(pady=20)

        ventanaFiltros.botonHP = Button(ventanaFiltros, text="Pasa altos", command=lambda:[self.HP(),ventanaFiltros.destroy(),self.SeleccionadorAudio()], width=20)
        ventanaFiltros.botonHP.pack(pady=20)

        ventanaFiltros.botonBP = Button(ventanaFiltros, text="Pasa banda", command=lambda:[self.BP(),ventanaFiltros.destroy(),self.SeleccionadorAudio()], width=20)
        ventanaFiltros.botonBP.pack(pady=20)

        ventanaFiltros.botonE = Button(ventanaFiltros, text="Eliminación", command=lambda:[self.E(),ventanaFiltros.destroy(),self.SeleccionadorAudio()], width=20)
        ventanaFiltros.botonE.pack(pady=20)
    
    #Metodo para definir el audio normalizado
    def SeleccionadorAudio(self):
        global w1,w2,w3,wO,wF,optAudio
        if(optAudio==1):
            wO=w1
            wF=w1
        elif(optAudio==2):
            wO=w2
            wF=w2
        elif(optAudio==3):
            wO=w3
            wF=w3

    #Metodo para el filtro pasa bajos
    def LP(self):
        global wF
        print('Pasa bajos')
        ventanaGraficos()

    #Metodo para el filtro pasa altos
    def HP(self):
        global wF
        print('Pasa altos')
        ventanaGraficos()

    #Metodo para el filtro pasa banda
    def BP(self):
        global wF
        print('Pasa banda')
        ventanaGraficos()

    #Metodo para el filtro eliminación
    def E(self):
        global wF
        print('Eliminacion')
        ventanaGraficos()

#Clase para elegir los audios
class ventanaAudios:
    def __init__(self):
        ventanaAudios = Toplevel()
        ventanaAudios.geometry("610x200")
        ventanaAudios.title("Seleccionar audio")

        ventanaAudios.etiqueta = Label(ventanaAudios, text="Seleccione el audio para filtrar: ", font=('Arial', 16))
        ventanaAudios.etiqueta.pack()
        #Load y play del primer audio
        ventanaAudios.botonA1 = Button(ventanaAudios, text="Primer audio", command=lambda:[self.A1()], width=20)
        ventanaAudios.botonA1.place(x=30, y=60)
        #Load y play del segundo audio
        ventanaAudios.botonA2 = Button(ventanaAudios, text="Segundo audio", command=lambda:[self.A2()], width=20)
        ventanaAudios.botonA2.place(x=230, y=60)
        #Load y play del tercer audio
        ventanaAudios.botonA3 = Button(ventanaAudios, text="Tercer audio", command=lambda:[self.A3()], width=20)
        ventanaAudios.botonA3.place(x=430, y=60)
        #Ventana para aplicar filtros
        ventanaAudios.botonSel = Button(ventanaAudios, text="Seleccionar", command=lambda:[self.Sel(),ventanaAudios.destroy()], width=20)
        ventanaAudios.botonSel.place(x=230, y=160)
        #Pausar el audio que está cargado
        ventanaAudios.botonStop = Button(ventanaAudios, text="Pausa", command=self.St, width=20)
        ventanaAudios.botonStop.place(x=230, y=120)

    #Metodo para el primer audio
    def A1(self):
        global m1,optAudio
        #Lineas para reproducir el audio
        pygame.mixer.music.load(m1)
        pygame.mixer.music.play(loops=0)
        optAudio=1 

    #Metodo para el segundo audio
    def A2(self):
        global m2,optAudio
        #Lineas para reproducir el audio
        pygame.mixer.music.load(m2)
        pygame.mixer.music.play(loops=0)
        optAudio=2

    #Metodo para el tercer audio
    def A3(self):
        global m3,optAudio
        #Lineas para reproducir el audio
        pygame.mixer.music.load(m3)
        pygame.mixer.music.play(loops=0)
        optAudio=3

    #Metodo auxiliar de variables
    '''def aux(self,num):
            print(num)
            return num
            #ventanaFiltros()'''

    #Metodo para seleccionar audio        
    def Sel(self):
            print(optAudio)
            ventanaFiltros()
            
    #Metodo para pausar la musica
    def St(self):
            print('Pausa')
            pygame.mixer.music.stop()
#Clase para importar audios
class ventanaImportar:
    def __init__(self):
        #Creacion de nueva ventana para importar audios
        ventanaImportar = Toplevel()
        ventanaImportar.geometry("500x250")
        ventanaImportar.title("Importar audios")

        ventanaImportar.etiqueta = Label(ventanaImportar, text="Importación de audios", font=('Arial', 16))
        ventanaImportar.etiqueta.pack(pady=20)
        ventanaImportar.botonImportar = Button(ventanaImportar, text="Importar", command=lambda:[self.importar(),ventanaImportar.destroy()], width=20)
        ventanaImportar.botonImportar.pack(pady=30)
        
    #Metodo para el boton de importar audios
    def importar(self):
        #Pide al usuario ingresar los audios
        global m1,m2,m3,w1,w2,w3
        for i in range(3):
            if(i==0):
                print('Primer audio')
                #Linea para importar audio
                m1 = filedialog.askopenfilename(title="Selecciona el audio", filetypes=(("Archivos wav", "*.wav"), ))
                messagebox.showinfo(title='Importar Audios', message='Has importado el audio 1 correctamente')
                w1 = read_wave(m1)
                w1.normalize()
            elif(i==1):
                print('Segundo audio')
                #Linea para importar audio
                m2 = filedialog.askopenfilename(title="Selecciona el audio", filetypes=(("Archivos wav", "*.wav"), ))
                messagebox.showinfo(title='Importar Audios', message='Has importado el audio 2 correctamente')
                w2 = read_wave(m1)
                w2.normalize()
            elif(i==2):    
                print('Tercer audio')
                #Linea para importar audio
                m3 = filedialog.askopenfilename(title="Selecciona el audio", filetypes=(("Archivos wav", "*.wav"), ))
                messagebox.showinfo(title='Importar Audios', message='Has importado el audio 3 correctamente')
                w3 = read_wave(m1)
                w3.normalize()
        ventanaAudios()
#Clase para mostrar los creditos
class ventanaCreditos:
    def __init__(self):
        #Creacion de nueva ventana para creditos
        ventanaCreditos = Toplevel()
        ventanaCreditos.geometry("500x250")
        ventanaCreditos.title("Integrantes")

        ventanaCreditos.etiqueta = Label(ventanaCreditos, text="Grupo #1", font=('Arial', 16))
        ventanaCreditos.etiqueta.pack(pady=20)

        ventanaCreditos.etiqueta = Label(ventanaCreditos, text="Javier Castañeda - 1290520", font=('Arial', 12))
        ventanaCreditos.etiqueta.pack(pady=5)
        ventanaCreditos.etiqueta = Label(ventanaCreditos, text="Angel Castillo - 1172920 ", font=('Arial', 12))
        ventanaCreditos.etiqueta.pack(pady=5)
        ventanaCreditos.etiqueta = Label(ventanaCreditos, text="Andres Coronado - 1168420 ", font=('Arial', 12))
        ventanaCreditos.etiqueta.pack(pady=5)
        ventanaCreditos.etiqueta = Label(ventanaCreditos, text="Pablo Flores - 1164720", font=('Arial', 12))
        ventanaCreditos.etiqueta.pack(pady=5)
#clase de ventana principal
class VentanaInicio:
    def __init__(self, master):
        self.master = master
        master.title("Inicio - Proyecto ASS - G1")
        master.geometry("500x250")
        

        self.etiqueta = Label(master, text="Proyecto Analisis de Senales y Sistemas", font=('Arial', 16))
        self.etiqueta.pack(pady=20)

        self.botonInicio = Button(master, text="Inicio", command=self.iniciar, width=20)
        self.botonInicio.pack(pady=10)

        self.botonCreditos = Button(master, text="Creditos", command=self.creditos, width=20)
        self.botonCreditos.pack(pady=10)

        self.botonSalir = Button(master, text="Salir", command=master.quit, width=20)
        self.botonSalir.pack(pady=10)

    #Metodo para el boton de inicio
    def iniciar(self):
        print('Importar audios')
        #Llamado a la clase para la ventana de importar audios
        ventanaImportar()
        #este comando cierra VentanaInicio
        root.withdraw()

    #Metodo para el boton de creditos
    def creditos(self):
        print('Grupo 1')
        #Creacion de nueva ventana para los creditos
        ventanaCreditos()

root = Tk()
optAudio=0
miVentana = VentanaInicio(root)
root.mainloop()



