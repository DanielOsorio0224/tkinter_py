from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("500x300")

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

def sumar():
    resultado.set(float(numero1.get()) + float(numero2.get()))
    mostrarResultado()

def restar():
    resultado.set(float(numero1.get()) - float(numero2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(float(numero1.get()) * float(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(float(numero1.get()) / float(numero2.get()))
    mostrarResultado()

def mostrarResultado():
    messagebox.showinfo("Resultado: ", f"El resultado de la operacion es: {resultado.get()}")
    numero1.set("")
    numero2.set("")

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

Button(marco, text="Sumar", command=sumar).pack()
Button(marco, text="Restar",command=restar).pack()
Button(marco, text="multiplicar",command=multiplicar).pack()
Button(marco, text="Dividir",command=dividir).pack()


ventana.mainloop()