# Main de la aplicación
import tkinter as tk
from users import Usuarios

def app_salud ():
    
    root = tk.Tk()              # crear ventana principal
    app = Usuarios()        # instanciar aplicación
    root.mainloop()             # ejecutar bucle principal


if __name__ == '__main__':

    app_salud()