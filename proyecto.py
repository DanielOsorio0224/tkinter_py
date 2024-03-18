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
    addLabel.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    addLabel.grid(row=0, column=0)

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

homeLabel = Label(ventana, text="Inicio")
addLabel = Label(ventana, text="Añadir producto")
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