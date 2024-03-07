from tkinter import *

ventana = Tk()
ventana.geometry("700x450")

def getDato() :
    resultado.set(dato.get())

dato = StringVar()
resultado = StringVar()

Label(ventana, text="Mete un texto").pack()
Entry(ventana, textvariable=dato).pack()

Label(ventana,text="Dato recogido: ").pack()
Label(ventana,textvariable=resultado).pack()

Button(ventana, text="Mostrar dato", command=getDato).pack()


ventana.mainloop()