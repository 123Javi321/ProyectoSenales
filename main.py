#Grupo 1
#Librerias a utilizar
#import numpy as np
#Libreria para analizar señales
from tkinter import *

#Clase para los filtros
class ventanaFiltros:
    def __init__(self):
        ventanaFiltros = Toplevel()
        ventanaFiltros.geometry("500x250")
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

    #Metodo para el filtro pasa altos
    def HP(self):
        print('Pasa altos')

    #Metodo para el filtro pasa banda
    def BP(self):
        print('Pasa banda')

    #Metodo para el filtro eliminación
    def E(self):
        print('Eliminacion')

#Clase para elegir los audios
class ventanaAudios:
    def __initi__(self):
        ventanaAudios = Toplevel()
        ventanaAudios.geometry("500x250")
        ventanaAudios.title("Seleccionar audio")

        ventanaAudios.etiqueta = Label(ventanaAudios, text="Seleccione el audio para filtrar: ", font=('Arial', 16))
        ventanaAudios.etiqueta.pack(pady=20)

        ventanaAudios.botonA1 = Button(ventanaAudios, text="Primer audio", command=self.A1, width=20)
        ventanaAudios.botonA1.pack(pady=20)

        ventanaAudios.botonA2 = Button(ventanaAudios, text="Segundo audio", command=self.A2, width=20)
        ventanaAudios.botonA2.pack(pady=20)

        ventanaAudios.botonA3 = Button(ventanaAudios, text="Tercer audio", command=self.A3, width=20)
        ventanaAudios.botonA3.pack(pady=20)

    #Metodo para el primer audio
    def A1(self):
            print('Primer audio')
            ventanaFiltros()

    #Metodo para el segundo audio
    def A2(self):
            print('Segundo audio')
            ventanaFiltros()

    #Metodo para el tercer audio
    def A3(self):
            print('Tercer audio')
            ventanaFiltros()

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

        ventanaImportar.botonContinuar = Button(ventanaImportar, text="Continuar", command=self.continuar, width=20)
        ventanaImportar.botonContinuar.pack(pady=20)

    #Metodo para el boton de importar audios
    def importar(self):
            print('importar')

    #Metodo para el boton de continuar
    def continuar(self):
            ventanaAudios()
            print('continuar')

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

print('xd')

