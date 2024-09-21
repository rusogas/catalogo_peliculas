import sqlite3
from .conexion_db import ConexiondDB  # Usa import relativo si está en el mismo paquete
from tkinter import messagebox

def crear_tabla():
    conexion = ConexiondDB()
    
    sql = '''
        CREATE TABLE IF NOT EXISTS peliculas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            duracion INTEGER NOT NULL,
            genero TEXT NOT NULL
        )
    '''
    
    try:
        conexion.cursor.execute(sql)
        conexion.conexion.commit()
        titulo = 'crear registro'
        mensaje = 'se creo la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except sqlite3.OperationalError as e:
        print(f"Error al crear la tabla: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
        titulo = 'crear registro'
        mensaje = 'la tabla ya esta creada'
        messagebox.showwarning(titulo, mensaje)
    finally:
        conexion.cerrar()

def borrar_tabla():
    conexion = ConexiondDB()
    
    sql = 'DROP TABLE IF EXISTS peliculas'
    
    try:
        conexion.cursor.execute(sql)
        conexion.conexion.commit()
        titulo = 'borrar registro'
        mensaje = 'la tabla se borro con exito'
        messagebox.showinfo(titulo, mensaje)
    except sqlite3.OperationalError as e:
        print(f"Error al borrar la tabla: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
        titulo = 'borrar registro'
        mensaje = 'no hay tabla para borrar'
        messagebox.showerror(titulo, mensaje)
    finally:
        conexion.cerrar()

class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
    
    def __str__(self):
        return f'pelicula[{self.nombre}, {self.duracion}, {self.genero}]' 
    
def guardar(pelicula):
    conexion = ConexiondDB()
    
    sql = f"""INSERT INTO peliculas (nombre, duracion, genero)
              VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.conexion.commit()  
        conexion.cerrar()
    except sqlite3.OperationalError as e:
        print(f"Error al guardar los datos: {e}")
        titulo = 'Conexion al registro'
        mensaje = 'Error al guardar la película en la base de datos'
        messagebox.showerror(titulo, mensaje)
    except Exception as e:
        print(f"Error inesperado: {e}")
        titulo = 'Error inesperado'
        mensaje = 'Ha ocurrido un error inesperado'
        messagebox.showerror(titulo, mensaje)
    finally:
        conexion.cerrar()
        
def listar():
    conexion = ConexiondDB()
    
    lista_peliculas = []
    sql= 'SELECT * FROM peliculas'
    
    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'conexion al registro'
        mensaje = 'crear la tabla en la base de datos'
        messagebox.showwarning(titulo, mensaje)
                 
    return lista_peliculas    
          
def editar(pelicula, id_pelicula):
    conexion = ConexiondDB()
    
    sql = """UPDATE peliculas
             SET nombre = ?, duracion = ?, genero = ?
             WHERE id = ?"""
    
    try:
        conexion.cursor.execute(sql, (pelicula.nombre, pelicula.duracion, pelicula.genero, id_pelicula))
        conexion.conexion.commit()
        messagebox.showinfo('Editar película', 'Película actualizada con éxito')
    except sqlite3.OperationalError as e:
        print(f"Error al actualizar la película: {e}")
        messagebox.showerror('Editar película', 'No se pudo actualizar la película')
    except Exception as e:
        print(f"Error inesperado: {e}")
        messagebox.showerror('Error inesperado', 'Ha ocurrido un error inesperado')
    finally:
        conexion.cerrar()

def eliminar(id_pelicula):
    conexion = ConexiondDB()  
    sql = 'DELETE FROM peliculas WHERE id = ?'  
    
    try:
        conexion.cursor.execute(sql, (id_pelicula,))  
        conexion.conexion.commit()  
        messagebox.showinfo('Eliminar datos', 'Registro eliminado con éxito')
    except sqlite3.OperationalError as e:
        print(f"Error al eliminar el registro: {e}")
        messagebox.showerror('Eliminar datos', 'No se pudo eliminar el registro')
    except Exception as e:
        print(f"Error inesperado: {e}")
        messagebox.showerror('Error inesperado', 'Ha ocurrido un error inesperado')
    finally:
        conexion.cerrar()    