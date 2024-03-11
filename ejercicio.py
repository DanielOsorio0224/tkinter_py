from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("500x300")

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=250, height=250)
marco.config(
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer numero").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo numero").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Button(marco, text="Sumar").pack()
Button(marco, text="Restar").pack()
Button(marco, text="multiplicar").pack()
Button(marco, text="Dividir").pack()


ventana.mainloop()