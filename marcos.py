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
Label(marco, text="Segundo marco").pack()    

marco.pack(side=LEFT, anchor=NW)
ventana.mainloop()