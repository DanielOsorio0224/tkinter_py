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
encabezado.grid(row=0, column=0, columnspan=4, sticky=W)

#LAbel para el campo(nombre)
label = Label(ventana, text="Nombre")  
label.grid(row=1, column=0, padx=5, pady=5)

#CAmpo de texto(nombre)
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="normal")

#LAbel para el campo(apellidos)
label = Label(ventana, text="Apellidos")  
label.grid(row=2, column=0, padx=5, pady=5)

#CAmpo de texto(apellidos)
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

#LAbel para el campo(descripcion)
label = Label(ventana, text="Descripcion")  
label.grid(row=3, column=0, sticky=N, padx=5, pady=5)

#Campo de texto GRANDE
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(width=30,height=5)

#Boton
Label(ventana).grid(row=4,column=1)

boton = Button(ventana,text="Enviar")
boton.grid(row=5, column=1)
boton.config(bg="blue", fg="white", cursor="pirate")

encabezado.mainloop()