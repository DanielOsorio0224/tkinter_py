from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("500x300")

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

Label(ventana, text="Primer numero").pack()
Entry(ventana, textvariable=numero1).pack()

Label(ventana, text="Segundo numero").pack()
Entry(ventana, textvariable=numero2).pack()

Button(ventana, text="Sumar").pack()
Button(ventana, text="Restar").pack()
Button(ventana, text="multiplicar").pack()
Button(ventana, text="Dividir").pack()


ventana.mainloop()