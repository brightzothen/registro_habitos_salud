import sqlite3

# Creamos la clase Habitos diarios, tendrá los siguientes atributos:
# id_registro: INTEGER PRIMARY KEY AUTOINCREMENT,
# Fecha: un INTEGER de la forma año-mes-dia 
# ID_USUARIO: INTEGER con el ID del usuario que hace el registro.
# Agua: REAL con los litros de agua que ha bebido ese día.
# Pasos: INTEGER pasos realizados ese día.
# Sueño: INTEGER minutos de sueño descansados ese día.

class HabitosDiarios:

    def __init__ ( self, db_name='registro_habitos.db'):
        self.db_name = db_name
        self.conexion = sqlite3.connect(db_name)
        self.cursor = self.conexion.cursor()

    def crear_tabla ( self ):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS registro_habitos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            fecha INTEGER NOT NULL,                           
            id_usuario INTEGER NOT NULL,   
            agua REAL NOT NULL,
            pasos INTEGER NOT NULL,
            sueño INTEGER NOT NULL                                                 
        )
        """)
        self.conexion.commit()
