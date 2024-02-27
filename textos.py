from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

texto = Label(ventana,text="Bienvenido a mi programa")
texto.config(fg="white", bg="black", padx=20, pady=20, font=("Arial", 15), cursor="spider")
texto.pack()

ventana.mainloop()