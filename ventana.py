#Modulo para interfaces graficas de usuario

from tkinter import *

class Programa:

    def __init__(self):
        self.title = "Tkinter"
        self.icon = "./imagenes/img.ico"
        self.size = "770X400"
        self.resizable = False

    def cargar(self):
        #Crear la ventana rai<
        ventana = Tk()
        self.ventana = ventana

        #Titulo de la ventana
        ventana.title(self.title)

        #Icono de la ventana
        ventana.iconbitmap(self.icon)

        #cambio de tamaño
        ventana.geometry(self.size)

        #fiajr tamaño
        if self.resizable:
            ventana.resizable(1,0) 

        #Arrancar y mostrar la ventana
        # ventana.mainloop()

    def addTexto(self):
        texto = Label(self.entana, text="Hola desde un metodo")    
        texto.pack()

    def mostrar(self):
        self.ventana.mainloop()    

programa = Programa()        
programa.cargar()
programa.addTexto()
programa.mostrar()