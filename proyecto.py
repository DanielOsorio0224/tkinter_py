from tkinter import *

ventana = Tk()
ventana.geometry("500x500")
ventana.title("Proyecto con tkinter")
ventana.resizable(0,0)

menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio") 
menu_superior.add_command(label="Añadir")
menu_superior.add_command(label="Informacion")
menu_superior.add_command(label="Salir", command=ventana.quit)

ventana.config(menu=menu_superior)

ventana.mainloop()