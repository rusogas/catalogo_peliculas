import sqlite3
import os

class ConexiondDB:
    def __init__(self):
        # Ruta relativa a la base de datos
        self.base_datos = os.path.join('catalogo-peliculas','client', 'database', 'peliculas.db')

        # Verificar si la carpeta que contiene la base de datos existe
        if not os.path.exists(os.path.dirname(self.base_datos)):
            raise FileNotFoundError(f"La carpeta '{os.path.dirname(self.base_datos)}' no existe. Por favor, cree la carpeta 'client/database'.")

        # Crear la base de datos si no existe
        if not os.path.isfile(self.base_datos):
            open(self.base_datos, 'w').close()

        # Conectar a la base de datos
        try:
            self.conexion = sqlite3.connect(self.base_datos)
            self.cursor = self.conexion.cursor()
        except sqlite3.Error as e:
            raise RuntimeError(f"No se pudo conectar a la base de datos: {e}")

    def cerrar(self):
        """Cierra la conexión a la base de datos"""
        self.conexion.close()




