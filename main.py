#Grupo 1
#Librerias a utilizar
#import numpy as np
#Libreria para analizar señales
import thinkdsp
from tkinter import *

#Clase para importar audios
class ventanaImportar:
    def __init__(self):
        #Creacion de nueva ventana para importar audios
        ventanaImportar = Toplevel()
        ventanaImportar.geometry("500x250")
        ventanaImportar.title("Importar audios")

        ventanaImportar.etiqueta = Label(ventanaImportar, text="Importación de audios", font=('Arial', 16))
        ventanaImportar.etiqueta.pack(pady=20)

        ventanaImportar.botonImportar = Button(ventanaImportar, text="Importar", command=self.importar, width=20)
        ventanaImportar.botonImportar.pack(pady=30)

    def importar(self):
            print('importar')

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
        ventanaCreditos.etiqueta = Label(ventanaCreditos, text="Leonardo Castillo - ", font=('Arial', 12))
        ventanaCreditos.etiqueta.pack(pady=5)
        ventanaCreditos.etiqueta = Label(ventanaCreditos, text="Andres Coronado - ", font=('Arial', 12))
        ventanaCreditos.etiqueta.pack(pady=5)
        ventanaCreditos.etiqueta = Label(ventanaCreditos, text="Pablo Flores - ", font=('Arial', 12))
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


