import hashlib  # Módulo para realizar operaciones de hash, como cifrar contraseñas
from Conexion import *  # Importa las funciones de conexión a la base de datos

# Constantes para mensajes de error
MSG_ERROR_CONEXION = "Error al conectar a la base de datos."
MSG_ERROR_REGISTRO = "Error al registrar el usuario:"
MSG_ERROR_VERIFICACION = "Error al comprobar la contraseña maestra:"

def comprobar_usuario():
    """
    Verifica si existen usuarios registrados en la base de datos.
    
    Returns:
        list: Lista de usuarios encontrados en la tabla 'usuario'.
    """
    try:
        # Establece conexión con la base de datos
        with conectar() as conexion:
            cursor = conexion.cursor()
            
            # Consulta SQL para obtener todos los usuarios
            sentencia_sql = "SELECT * FROM usuario"
            cursor.execute(sentencia_sql)
            
            # Recupera todos los registros encontrados
            usuario_encontrado = cursor.fetchall()
            
            # Devuelve la lista de usuarios encontrados
            return usuario_encontrado
    except Error as err:
        print(f"{MSG_ERROR_CONEXION} {err}")
        return []

def registrar(nombre, apellido, contrasena_maestra):
    """
    Registra un nuevo usuario en la base de datos.
    La contraseña maestra se cifra utilizando SHA-256 antes de almacenarla.
    
    Args:
        nombre (str): Nombre del usuario.
        apellido (str): Apellido del usuario.
        contrasena_maestra (str): Contraseña maestra del usuario.
    
    Returns:
        str: Mensaje indicando si el registro fue exitoso o si ocurrió un error.
    """
    if not nombre or not apellido or not contrasena_maestra:
        return "Todos los campos son obligatorios."

    try:
        # Establece conexión con la base de datos
        with conectar() as conexion:
            cursor = conexion.cursor()
            
            # Sentencia SQL para insertar un nuevo usuario
            sentencia_sql = """INSERT INTO usuario 
            (nombre, apellido, contrasena_maestra) 
            VALUES (?, ?, ?)"""
            
            # Cifra la contraseña maestra utilizando SHA-256
            cm_cifrada = hashlib.sha256(contrasena_maestra.encode('utf-8')).hexdigest()
            
            # Datos a insertar en la tabla
            datos = (nombre, apellido, cm_cifrada)
            
            # Ejecuta la sentencia SQL con los datos
            cursor.execute(sentencia_sql, datos)
            
            # Confirma los cambios en la base de datos
            conexion.commit()
            
            # Devuelve un mensaje de éxito
            return 'Usuario registrado exitosamente'
    except Error as err:
        return f"{MSG_ERROR_REGISTRO} {err}"

def comprobar_contrasena_maestra(id, contrasena_maestra):
    """
    Verifica si la contraseña maestra proporcionada coincide con la almacenada en la base de datos.
    
    Args:
        id (int): ID del usuario.
        contrasena_maestra (str): Contraseña maestra proporcionada por el usuario.
    
    Returns:
        list: Lista de registros que coinciden con el ID y la contraseña maestra.
              Si no hay coincidencias, devuelve una lista vacía.
    """
    if not id or not contrasena_maestra:
        return []

    try:
        # Establece conexión con la base de datos
        with conectar() as conexion:
            cursor = conexion.cursor()
            
            # Sentencia SQL para verificar la contraseña maestra
            sentencia_sql = """SELECT * FROM usuario
            WHERE id = ? AND contrasena_maestra = ?"""
            
            # Cifra la contraseña maestra proporcionada utilizando SHA-256
            cm_cifrada = hashlib.sha256(contrasena_maestra.encode('utf-8')).hexdigest()
            
            # Ejecuta la sentencia SQL con los parámetros proporcionados
            cursor.execute(sentencia_sql, (id, cm_cifrada))
            
            # Recupera los registros que coinciden
            datos = cursor.fetchall()
            
            # Devuelve los datos encontrados
            return datos
    except Error as err:
        print(f"{MSG_ERROR_VERIFICACION} {err}")
        return []
