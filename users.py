# Creamos la clase Usuario:
# Tendrá los siguientes atributos
# id_user INTEGER
# Nombre TEXT
# passwrd BLOB (TEXT originalmente)

# Necesitaremos importar para la mejora el bcrypt y el hash
import sqlite3
import tkinter as tk
from tkinter import messagebox

class Usuario:

    def __init__(self, id_user, nombre, contrasenya):
        self.id_user = id_user
        self.nombre = nombre
        self.password = contrasenya

# La clase Usuarios será con conjunto de usuarios y gestionará el almacenamiento persistente de los distintos usuarios del sistema.
class Usuarios:

    def __init__ ( self, db_name='usuarios.db'):

        self.db_name = db_name
        self.conexion = sqlite3.connect(db_name)
        self.cursor = self.conexion.cursor()

        self.crear_tabla()
        user_window = tk.Tk()
        user_window.title('Agregar Usuario:')
        user_window.geometry('400x300+200+200')

        # self.leer_usuarios()

        tk.Label(user_window, text='Nombre').pack(pady=5)
        entry_nombre = tk.Entry()
        entry_nombre.pack(pady=10)

        tk.Label(user_window, text='Password').pack(pady=5)
        entry_passw = tk.Entry()
        entry_passw.pack(pady=10)

        tk.Button(user_window, text='Agregar usuario', command=self.agregar_usuario).pack(pady=10)

    def agregar_usuario ( self ):

            nombre = self.entry_nombre.get().strip()
            passw = self.entry_passw.get().strip()

            if not nombre or not passw:
                messagebox.showwarning('Atención','El nombre y el password son obligatorios.')
                return
    
            self.cursor.execute("INSERT INTO usuarios ( nombre, passwrd ) VALUES ( ?, ? )", (nombre, passw))
            self.conexion.commit()

            messagebox.showinfo('Éxito', f'Usuario: {nombre} agregado correctamente.')
            self.entry_nombre.delete(0, tk.END)
            self.entry_passw.delete(0, tk.END)

    def crear_tabla ( self ):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id_user INTEGER PRIMARY KEY AUTOINCREMENT,  
            Nombre TEXT NOT NULL,                           
            passwrd TEXT NOT NULL                                      
        )
        """)
        self.conexion.commit()

    def leer_usuarios( self ):

        self.cursor.execute("SELECT * FROM usuarios")
        self.contacts = self.cursor.fetchall()  # lista de tuplas (id, nombre, passwrd)