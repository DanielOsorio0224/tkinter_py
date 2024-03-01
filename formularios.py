from tkinter import *

ventana = Tk()
ventana.geometry("700x500")
ventana.title("Formularios")

encabezado = Label(ventana, text="Formularios con Tkinter")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Arial", 20),
    padx=10,
    pady=10
)
encabezado.pack()

encabezado.mainloop()