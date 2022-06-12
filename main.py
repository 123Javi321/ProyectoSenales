#Grupo 1
#Librerias a utilizar
#import numpy as np
from tkinter import *

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
        #este comando cierra VentanaInicio
        importarAudio = ventanaImportar()
        root.withdraw()


    #Metodo para el boton de creditos
    def creditos(self):
        print('Grupo 1')
        #Creacion de nueva ventana para los creditos
        ventanaCreditos = Toplevel()
        ventanaCreditos.geometry("500x250")
        ventanaCreditos.title("Integrantes")
        #este comando cierra VentanaInicio
        root.withdraw()

root = Tk()
miVentana = VentanaInicio(root)
root.mainloop()


