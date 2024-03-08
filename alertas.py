from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.geometry("500x300")

def sacarAlerta():
    MessageBox.showinfo("Alerta", "Hola soy una alerta")

Button(ventana, text="Mostrar alerta", command=sacarAlerta).pack()

def salir():
    resultado = MessageBox.askquestion("Salir", "quieres salirte?")

    if resultado == "yes":
        ventana.destroy()

Button(ventana, text="Salir", command=salir).pack()


ventana.mainloop()