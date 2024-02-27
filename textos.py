from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

def pruebas(nombre,apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"

texto = Label(ventana,text=pruebas(nombre="Daniel",apellidos="OSorio",pais="Colombia"))
texto.config(fg="white", bg="black", padx=20, pady=20, font=("Arial", 15), cursor="spider")
texto.pack()

ventana.mainloop()