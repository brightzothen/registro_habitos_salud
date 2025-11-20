# Creamos la clase Usuario:
# Tendrá los siguientes atributos
# id_user INTEGER
# Nombre TEXT
# passwrd BLOB (TEXT originalmente)

# Necesitaremos importar para la mejora el bcrypt y el hash
import sqlite3

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

    def crear_tabla ( self ):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS registro_habitos (
            id_user INTEGER PRIMARY KEY AUTOINCREMENT,  
            Nombre TEXT NOT NULL,                           
            passwrd TEXT NOT NULL                                      
        )
        """)
        self.conexion.commit()