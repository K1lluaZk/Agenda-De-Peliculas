#En Esta Parte Del Codigo Se Realiza La Conexion Con La Base De Datos

import sqlite3

class ConexionDB:
    def __init__(self):
        self.base_datos = "Agenda De Peliculas/database/peliculas.db"
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()
