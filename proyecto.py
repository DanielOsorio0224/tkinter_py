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
    add_frame.grid_remove()

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
    add_frame.grid(row=1)
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
    add_frame.grid_remove()
    return True

def addProduct():
    products.append([
        nameData.get(),
        priceData.get(),
        add_descripcion_entry.get("1.0", "end-1c")
    ])

    nameData.set("")
    priceData.set("")
    add_descripcion_entry.delete("1.0", END)

    home()    
#variables importante
products = []
nameData = StringVar()
priceData = StringVar()

homeLabel = Label(ventana, text="Inicio")
addLabel = Label(ventana, text="Añadir producto")

#Campos formulario
add_frame = Frame(ventana)
add_name_label = Label(add_frame, text="Nombre: ")
add_name_entry = Entry(add_frame, textvariable=nameData)

add_price_label = Label(add_frame, text="Precio: ")
add_price_entry = Entry(add_frame, textvariable=priceData)

add_descripcion_label = Label(add_frame, text="Descripcion: ")
add_descripcion_entry = Text(add_frame)

boton = Button(add_frame, text="Guardar", command=addProduct)

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