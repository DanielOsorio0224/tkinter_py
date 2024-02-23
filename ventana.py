#Modulo para interfaces graficas de usuario

from tkinter import *
#Crear la ventana rai<
ventana = Tk()

#Titulo de la ventana
ventana.title("Interfaz grafica en TKINTER")

#Icono de la ventana
ventana.iconbitmap("./imagenes/img.ico")

#cambio de tamaño
ventana.geometry("750x450")

#fiajr tamaño
ventana.resizable(1,0) 

#Arrancar y mostrar la ventana
ventana.mainloop()