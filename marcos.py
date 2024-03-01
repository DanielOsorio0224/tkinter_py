from tkinter import *

ventana = Tk()
ventana.geometry("700x400")

marco = Frame(ventana, width=250, height=250)
marco.config(bg="red",
             bd=12,
             relief=SOLID)

marco.pack(side=RIGHT, anchor=SE)

marco = Frame(ventana, width=250, height=250)
marco.config(bg="blue",
             bd=12,
             relief=SOLID)
marco.pack_propagate(False)
texto = Label(marco, text="Segundo marco").pack()    
texto.config(
    bg="red",
    fg="white",
    font=("Arial", 20),
    height = 4,
    width = 4,
    db=3,
    relief=SOLID,
    anchor=CENTER
)

marco.pack(side=LEFT, anchor=NW)
ventana.mainloop()