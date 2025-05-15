from Conexion import *

def registrar(nombre, url, nombre_usuario, contrasena, descripcion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = """INSERT INTO contrasena(
        nombre, url, nombre_usuario, contrasena, descripcion)
        VALUES (?, ?, ?, ?, ?)"""
        datos = (nombre, url, nombre_usuario, contrasena, descripcion)
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        conexion.close()
        return 'Contraseña registrada exitosamente'
    except Error as err:
        return "Error al registrar la contraseña:" + str(err)
    
def mostrar_contrasenas():
    datos = []
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = "SELECT * FROM contrasena"
        cursor.execute(sentencia_sql)
        datos = cursor.fetchall()
        conexion.close()
    except Error as err:
        print("Ha ocurrido un error al mostrar las contraseñas:" + str(err))
    return datos

def buscar_contrasena(id):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = "SELECT * FROM contrasena WHERE id = ?"
        cursor.execute(sentencia_sql, (id,))
        datos = cursor.fetchall()
        conexion.close()
    except Error as err:
        print("Ha ocurrido un error al buscar la contraseña:" + str(err))
    return datos

def modificar_contrasena(id, nombre, url, nombre_usuario, contrasena, descripcion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = """UPDATE contrasena
        SET nombre = ?, url = ?, nombre_usuario = ?, contrasena = ?, descripcion = ?
        WHERE id = ?"""
        datos = (nombre, url, nombre_usuario, contrasena, descripcion, id)
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        conexion.close()
        return 'Contraseña modificada exitosamente'
    except Error as err:
        return "Error al modificar la contraseña:" + str(err)

def eliminar_contrasena(id):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = "DELETE FROM contrasena WHERE id = ?"
        cursor.execute(sentencia_sql, (id,))
        conexion.commit()
        conexion.close()
        return 'Contraseña eliminada exitosamente'
    except Error as err:
        return "Error al eliminar la contraseña:" + str(err)    
