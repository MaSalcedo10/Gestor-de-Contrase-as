from Conexion import *  # Importa las funciones de conexión a la base de datos

def registrar(nombre, url, nombre_usuario, contrasena, descripcion):
    """
    Registra una nueva contraseña en la base de datos.
    
    Args:
        nombre (str): Nombre de la contraseña (identificador).
        url (str): URL asociada a la contraseña.
        nombre_usuario (str): Nombre de usuario asociado a la contraseña.
        contrasena (str): Contraseña a almacenar.
        descripcion (str): Descripción opcional de la contraseña.
    
    Returns:
        str: Mensaje indicando si el registro fue exitoso o si ocurrió un error.
    """
    if not nombre or not url or not nombre_usuario or not contrasena:
        return "Todos los campos obligatorios deben ser completados."

    try:
        # Establece conexión con la base de datos
        with conectar() as conexion:
            cursor = conexion.cursor()
            
            # Sentencia SQL para insertar una nueva contraseña
            sentencia_sql = """INSERT INTO contrasena(
            nombre, url, nombre_usuario, contrasena, descripcion)
            VALUES (?, ?, ?, ?, ?)"""
            
            # Datos a insertar en la tabla
            datos = (nombre, url, nombre_usuario, contrasena, descripcion)
            
            # Ejecuta la sentencia SQL con los datos
            cursor.execute(sentencia_sql, datos)
            
            # Confirma los cambios en la base de datos
            conexion.commit()
            
            # Devuelve un mensaje de éxito
            return 'Contraseña registrada exitosamente'
    except Error as err:
        # Devuelve un mensaje de error en caso de fallo
        return f"Error al registrar la contraseña: {err}"

def mostrar_contrasenas():
    """
    Recupera todas las contraseñas almacenadas en la base de datos.
    
    Returns:
        list: Lista de todas las contraseñas almacenadas.
    """
    try:
        # Establece conexión con la base de datos
        with conectar() as conexion:
            cursor = conexion.cursor()
            
            # Sentencia SQL para obtener todas las contraseñas
            sentencia_sql = "SELECT * FROM contrasena"
            cursor.execute(sentencia_sql)
            
            # Recupera todos los registros encontrados
            datos = cursor.fetchall()
            
            # Devuelve los datos encontrados
            return datos
    except Error as err:
        # Imprime un mensaje de error en caso de fallo
        print(f"Ha ocurrido un error al mostrar las contraseñas: {err}")
        return []

def buscar_contrasena(id):
    """
    Busca una contraseña específica en la base de datos por su ID.
    
    Args:
        id (int): ID de la contraseña a buscar.
    
    Returns:
        list: Lista con los datos de la contraseña encontrada.
              Si no se encuentra, devuelve una lista vacía.
    """
    if not id:
        return []

    try:
        # Establece conexión con la base de datos
        with conectar() as conexion:
            cursor = conexion.cursor()
            
            # Sentencia SQL para buscar una contraseña por ID
            sentencia_sql = "SELECT * FROM contrasena WHERE id = ?"
            cursor.execute(sentencia_sql, (id,))
            
            # Recupera los registros encontrados
            datos = cursor.fetchall()
            
            # Devuelve los datos encontrados
            return datos
    except Error as err:
        # Imprime un mensaje de error en caso de fallo
        print(f"Ha ocurrido un error al buscar la contraseña: {err}")
        return []

def modificar_contrasena(id, nombre, url, nombre_usuario, contrasena, descripcion):
    """
    Modifica una contraseña existente en la base de datos.
    
    Args:
        id (int): ID de la contraseña a modificar.
        nombre (str): Nuevo nombre de la contraseña.
        url (str): Nueva URL asociada.
        nombre_usuario (str): Nuevo nombre de usuario asociado.
        contrasena (str): Nueva contraseña.
        descripcion (str): Nueva descripción opcional.
    
    Returns:
        str: Mensaje indicando si la modificación fue exitosa o si ocurrió un error.
    """
    if not id or not nombre or not url or not nombre_usuario or not contrasena:
        return "Todos los campos obligatorios deben ser completados."

    try:
        # Establece conexión con la base de datos
        with conectar() as conexion:
            cursor = conexion.cursor()
            
            # Sentencia SQL para actualizar una contraseña
            sentencia_sql = """UPDATE contrasena
            SET nombre = ?, url = ?, nombre_usuario = ?, contrasena = ?, descripcion = ?
            WHERE id = ?"""
            
            # Datos a actualizar en la tabla
            datos = (nombre, url, nombre_usuario, contrasena, descripcion, id)
            
            # Ejecuta la sentencia SQL con los datos
            cursor.execute(sentencia_sql, datos)
            
            # Confirma los cambios en la base de datos
            conexion.commit()
            
            # Devuelve un mensaje de éxito
            return 'Contraseña modificada exitosamente'
    except Error as err:
        # Devuelve un mensaje de error en caso de fallo
        return f"Error al modificar la contraseña: {err}"

def eliminar_contrasena(id):
    """
    Elimina una contraseña existente en la base de datos por su ID.
    
    Args:
        id (int): ID de la contraseña a eliminar.
    
    Returns:
        str: Mensaje indicando si la eliminación fue exitosa o si ocurrió un error.
    """
    if not id:
        return "El ID es obligatorio para eliminar una contraseña."

    try:
        # Establece conexión con la base de datos
        with conectar() as conexion:
            cursor = conexion.cursor()
            
            # Sentencia SQL para eliminar una contraseña por ID
            sentencia_sql = "DELETE FROM contrasena WHERE id = ?"
            cursor.execute(sentencia_sql, (id,))
            
            # Confirma los cambios en la base de datos
            conexion.commit()
            
            # Devuelve un mensaje de éxito
            return 'Contraseña eliminada exitosamente'
    except Error as err:
        # Devuelve un mensaje de error en caso de fallo
        return f"Error al eliminar la contraseña: {err}"
