from tkinter import *

ventana = Tk()
ventana.geometry("500x500")
ventana.title("Proyecto con tkinter")
ventana.resizable(0,0)

#Pantallas
def home():
    homeLabel.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    homeLabel.grid(row=0, column=0)

    addLabel.grid_remove()
    infoLabel.grid_remove()
    dataLabel.grid_remove()

    return True

def add():
    #encabezado
    addLabel.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    addLabel.grid(row=0, column=0, columnspan=4)

    #campos formulario
    add_name_label.grid(row=1,column=0)
    add_name_entry.grid(row=1, column=1)
    add_price_label.grid(row=2,column=0)
    add_price_entry.grid(row=2,column=1)
    add_descripcion_label.grid(row=3,column=0, sticky=NW)
    add_descripcion_entry.grid(row=3,column=1)
    add_descripcion_entry.config(width=30, height=5, font=("Consolas",12),padx=15,pady=15)
    boton.grid(row=4,column=1)

    homeLabel.grid_remove()
    infoLabel.grid_remove()
    dataLabel.grid_remove()
    return True

def info():
    infoLabel.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    infoLabel.grid(row=0, column=0)
    dataLabel.grid(row=1, column=0)

    addLabel.grid_remove()
    homeLabel.grid_remove()
    return True

#variables importante
nameData = StringVar()
priceData = StringVar()

homeLabel = Label(ventana, text="Inicio")
addLabel = Label(ventana, text="Añadir producto")

#Campos formulario
add_name_label = Label(ventana, text="Nombre: ")
add_name_entry = Entry(ventana, textvariable=nameData)

add_price_label = Label(ventana, text="Precio: ")
add_price_entry = Entry(ventana, textvariable=priceData)

add_descripcion_label = Label(ventana, text="Descripcion: ")
add_descripcion_entry = Text(ventana)

boton = Button(ventana, text="Guardar")

infoLabel = Label(ventana, text="Informacion producto")
dataLabel = Label(ventana,text="Creado por daniel")

# cargar pantalla inicio
home()

#Menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home) 
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Informacion", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

ventana.config(menu=menu_superior)

ventana.mainloop()