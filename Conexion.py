import sqlite3  # Módulo para trabajar con bases de datos SQLite
from sqlite3 import Error  # Clase para manejar errores relacionados con SQLite

# Constantes para las sentencias SQL
SQL_CREAR_TABLA_USUARIO = """
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID único para cada usuario
    nombre TEXT NOT NULL,                  -- Nombre del usuario
    apellido TEXT NOT NULL,                -- Apellido del usuario
    contrasena_maestra TEXT NOT NULL       -- Contraseña maestra del usuario
)
"""

SQL_CREAR_TABLA_CONTRASENA = """
CREATE TABLE IF NOT EXISTS contrasena (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID único para cada contraseña
    nombre TEXT NOT NULL,                  -- Nombre de la contraseña
    url TEXT NOT NULL,                     -- URL asociada a la contraseña
    nombre_usuario TEXT NOT NULL,          -- Nombre de usuario asociado
    contrasena TEXT NOT NULL,              -- Contraseña almacenada
    descripcion TEXT                       -- Descripción opcional
)
"""

def conectar():
    """
    Establece una conexión con la base de datos SQLite.
    Si la base de datos no existe, se crea automáticamente.
    
    Returns:
        conexion: Objeto de conexión a la base de datos SQLite.
    """
    try:
        # Conecta a la base de datos 'database.db'
        conexion = sqlite3.connect('database.db')
        print("Conexión exitosa a la base de datos SQLite")
        return conexion
    except Error as err:
        # Maneja errores en caso de que la conexión falle
        print(f"Error al conectar a la base de datos SQLite: {err}")
        return None

def crear_tablas(conexion):
    """
    Crea las tablas necesarias en la base de datos si no existen.
    Las tablas creadas son:
    - usuario: Para almacenar información de los usuarios.
    - contrasena: Para almacenar las contraseñas gestionadas por el sistema.
    
    Args:
        conexion: Objeto de conexión a la base de datos SQLite.
    """
    if conexion is None:
        print("No se pudo crear las tablas porque la conexión es nula.")
        return

    try:
        # Crea un cursor para ejecutar comandos SQL
        cursor = conexion.cursor()
        
        # Ejecuta las sentencias SQL para crear las tablas
        cursor.execute(SQL_CREAR_TABLA_USUARIO)
        cursor.execute(SQL_CREAR_TABLA_CONTRASENA)
        print("Tablas creadas exitosamente")
        
        # Confirma los cambios en la base de datos
        conexion.commit()
    except Error as err:
        # Maneja errores en caso de que la creación de tablas falle
        print(f"Error al crear las tablas: {err}")
    finally:
        # Asegura que la conexión se cierre correctamente
        conexion.close()