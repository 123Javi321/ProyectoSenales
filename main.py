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
import pygame

optAudio =0

pygame.mixer.init()

#Clase para los graficos
class ventanaGraficos:
    def __init__(self):
        ventanaFiltros = Toplevel()
        ventanaFiltros.geometry("700x250")
        ventanaFiltros.title("Graficas")

        ventanaFiltros.etiqueta = Label(ventanaFiltros, text="Seleccione la grafica que desea ver: ", font=('Arial', 16))
        ventanaFiltros.etiqueta.pack(pady=20)

        ventanaFiltros.botonG1 = Button(ventanaFiltros, text="Gráfico en dominio del tiempo sin filtrar", command=self.G1, width=40)
        ventanaFiltros.botonG1.place(x=60, y=60)

        ventanaFiltros.botonG2 = Button(ventanaFiltros, text="Gráfico en dominio de la frecuencia sin filtrar", command=self.G2, width=40)
        ventanaFiltros.botonG2.place(x=60, y=160)

        ventanaFiltros.botonG3 = Button(ventanaFiltros, text="Gráfico en dominio del tiempo filtrado", command=self.G3, width=40)
        ventanaFiltros.botonG3.place(x=360, y=60)

        ventanaFiltros.botonG4 = Button(ventanaFiltros, text="Gráfico en dominio de la frecuencia filtrado", command=self.G4, width=40)
        ventanaFiltros.botonG4.place(x=360, y=160)

    def G1(self):
        print("Grafico 1")

    def G2(self):
        print("Grafico 2")

    def G3(self):
        print("Grafico 3")
    
    def G4(self):
        print("Grafico 4")

#Clase para los filtros
class ventanaFiltros:
    def __init__(self):
        ventanaFiltros = Toplevel()
        ventanaFiltros.geometry("500x450")
        ventanaFiltros.title("Seleccionar filtro")

        ventanaFiltros.etiqueta = Label(ventanaFiltros, text="Seleccione el filtro para aplicar: ", font=('Arial', 16))
        ventanaFiltros.etiqueta.pack(pady=20)

        ventanaFiltros.botonLP = Button(ventanaFiltros, text="Pasa bajos", command=self.LP, width=20)
        ventanaFiltros.botonLP.pack(pady=20)

        ventanaFiltros.botonHP = Button(ventanaFiltros, text="Pasa altos", command=self.HP, width=20)
        ventanaFiltros.botonHP.pack(pady=20)

        ventanaFiltros.botonBP = Button(ventanaFiltros, text="Pasa banda", command=self.BP, width=20)
        ventanaFiltros.botonBP.pack(pady=20)

        ventanaFiltros.botonE = Button(ventanaFiltros, text="Eliminación", command=self.E, width=20)
        ventanaFiltros.botonE.pack(pady=20)

    #Metodo para el filtro pasa bajos
    def LP(self):
        print('Pasa bajos')
        ventanaGraficos()

    #Metodo para el filtro pasa altos
    def HP(self):
        print('Pasa altos')
        ventanaGraficos()

    #Metodo para el filtro pasa banda
    def BP(self):
        print('Pasa banda')
        ventanaGraficos()

    #Metodo para el filtro eliminación
    def E(self):
        print('Eliminacion')
        ventanaGraficos()

#Clase para elegir los audios
class ventanaAudios:
    def __init__(self):
        m1=None
        m2=None
        m3=None
        #Pide al usuario ingresar los audios
        for i in range(3):
            if(i==0):
                print('Primer audio')
                #Linea para importar audio
                m1 = filedialog.askopenfilename(title="Selecciona el audio", filetypes=(("Archivos wav", "*.wav"), ))
                messagebox.showinfo(title='Importar Audios', message='Has importado el audio 1 correctamente')
            elif(i==1):
                print('Segundo audio')
                #Linea para importar audio
                m2 = filedialog.askopenfilename(title="Selecciona el audio", filetypes=(("Archivos wav", "*.wav"), ))
                messagebox.showinfo(title='Importar Audios', message='Has importado el audio 2 correctamente')
            elif(i==2):    
                print('Tercer audio')
                #Linea para importar audio
                m3 = filedialog.askopenfilename(title="Selecciona el audio", filetypes=(("Archivos wav", "*.wav"), ))
                messagebox.showinfo(title='Importar Audios', message='Has importado el audio 3 correctamente')

        ventanaAudios = Toplevel()
        ventanaAudios.geometry("610x200")
        ventanaAudios.title("Seleccionar audio")

        ventanaAudios.etiqueta = Label(ventanaAudios, text="Seleccione el audio para filtrar: ", font=('Arial', 16))
        ventanaAudios.etiqueta.pack()
        #Load y play del primer audio
        ventanaAudios.botonA1 = Button(ventanaAudios, text="Primer audio", command=lambda:[pygame.mixer.music.load(m1),pygame.mixer.music.play(loops=0)], width=20)
        ventanaAudios.botonA1.place(x=30, y=60)
        #Load y play del segundo audio
        ventanaAudios.botonA2 = Button(ventanaAudios, text="Segundo audio", command=lambda:[pygame.mixer.music.load(m2),pygame.mixer.music.play(loops=0)], width=20)
        ventanaAudios.botonA2.place(x=230, y=60)
        #Load y play del tercer audio
        ventanaAudios.botonA3 = Button(ventanaAudios, text="Tercer audio", command=lambda:[pygame.mixer.music.load(m3),pygame.mixer.music.play(loops=0)], width=20)
        ventanaAudios.botonA3.place(x=430, y=60)
        #Ventana para aplicar filtros
        ventanaAudios.botonSel = Button(ventanaAudios, text="Seleccionar", command=self.Sel, width=20)
        ventanaAudios.botonSel.place(x=230, y=160)
        #Pausar el audio que está cargado
        ventanaAudios.botonStop = Button(ventanaAudios, text="Pausa", command=self.St, width=20)
        ventanaAudios.botonStop.place(x=230, y=120)

    #Metodo para el primer audio
    def A1(self):
            #Lineas para reproducir el audio
            #pygame.mixer.music.load(m1)
            #pygame.mixer.music.play(loops=0)
            optAudio =1

    #Metodo para el segundo audio
    def A2(self):
            #Lineas para reproducir el audio
            #pygame.mixer.music.load(m2)
            #pygame.mixer.music.play(loops=0)
            optAudio=2

    #Metodo para el tercer audio
    def A3(self):
            #Lineas para reproducir el audio
            #pygame.mixer.music.load(m3)
            #pygame.mixer.music.play(loops=0)
            optAudio=3

    #Metodo para seleccionar audio        
    def Sel(self):
            print('Seleccionar')
            pygame.mixer.music.unpause()
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
miVentana = VentanaInicio(root)
root.mainloop()


