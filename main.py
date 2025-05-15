import os
from getpass import getpass  # Para ocultar la entrada de contraseñas
from tabulate import tabulate  # Para mostrar datos en formato tabular
from Conexion import *  # Importa funciones relacionadas con la conexión a la base de datos
import Usuario  # Módulo para gestionar usuarios
import Contrasena  # Módulo para gestionar contraseñas

# Constantes para mensajes
MSG_BIENVENIDA = "Bienvenido a la aplicación de gestión de contraseñas."
MSG_ERROR_CONTRASENA = "Contraseña maestra incorrecta."
MSG_SALIR = "Saliendo de la aplicación..."
MSG_OPCION_INVALIDA = "Opción no válida, por favor intente de nuevo."

# Establece la conexión con la base de datos y crea las tablas necesarias
conexion = conectar()
crear_tablas(conexion)

def iniciar_sesion():
    """
    Función principal para iniciar sesión o registrar un nuevo usuario.
    Si no hay usuarios registrados, solicita el registro.
    Si ya hay usuarios, solicita la contraseña maestra para iniciar sesión.
    """
    try:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
        comprobar = Usuario.comprobar_usuario()  # Verifica si hay usuarios registrados
        if len(comprobar) == 0:
            print("No hay usuarios registrados. Por favor, registre un usuario.")
            registrar_usuario()
        else:
            contrasena_maestra = getpass("Ingrese su contraseña maestra: ")
            respuesta = Usuario.comprobar_contrasena_maestra(1, contrasena_maestra)
            if len(respuesta) == 0:
                print(MSG_ERROR_CONTRASENA)
            else:
                print("Inicio de sesión exitoso.")
                menu()  # Muestra el menú principal
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

def registrar_usuario():
    """
    Registra un nuevo usuario en el sistema.
    """
    try:
        nombre = input("Ingrese su nombre: ").strip()
        apellido = input("Ingrese su apellido: ").strip()
        contrasena_maestra = getpass("Ingrese su contraseña maestra: ").strip()
        if not nombre or not apellido or not contrasena_maestra:
            print("Todos los campos son obligatorios.")
            return
        respuesta = Usuario.registrar(nombre, apellido, contrasena_maestra)
        print(respuesta)
        if respuesta == 'Usuario registrado exitosamente':
            menu()
    except Exception as e:
        print(f"Error al registrar el usuario: {e}")

def menu():
    """
    Muestra el menú principal de la aplicación y permite al usuario seleccionar opciones.
    """
    while True:
        print(f"\n{MSG_BIENVENIDA}\nSeleccione una de las siguientes opciones:")
        print("\t1- Añadir contraseña")
        print("\t2- Mostrar contraseñas")
        print("\t3- Mostrar una contraseña")
        print("\t4- Modificar contraseña")
        print("\t5- Eliminar contraseña")
        print("\t6- Salir")
        opcion = input("Ingrese una opción: ").strip()
        if opcion == '1':
            nueva_contrasena()
        elif opcion == '2':
            mostrar_contrasenas()
        elif opcion == '3':
            buscar_contrasena()
        elif opcion == '4':
            modificar_contrasena()
        elif opcion == '5':
            eliminar_contrasena()
        elif opcion == '6':
            print(MSG_SALIR)
            break
        else:
            print(MSG_OPCION_INVALIDA)

def nueva_contrasena():
    """
    Permite al usuario añadir una nueva contraseña al sistema.
    """
    try:
        nombre = input("Ingrese el nombre de la contraseña: ").strip()
        url = input("Ingrese la URL: ").strip()
        nombre_usuario = input("Ingrese el nombre de usuario: ").strip()
        contrasena = input("Ingrese la contraseña: ").strip()
        descripcion = input("Ingrese una descripción: ").strip()
        if not nombre or not url or not nombre_usuario or not contrasena:
            print("Todos los campos son obligatorios.")
            return
        respuesta = Contrasena.registrar(nombre, url, nombre_usuario, contrasena, descripcion)
        print(respuesta)
    except Exception as e:
        print(f"Error al añadir la contraseña: {e}")

def mostrar_contrasenas():
    """
    Muestra todas las contraseñas almacenadas en el sistema en formato tabular.
    Oculta las contraseñas reales por seguridad.
    """
    try:
        datos = Contrasena.mostrar_contrasenas()
        if not datos:
            print("No hay contraseñas registradas.")
            return
        nuevos_datos = []
        for dato in datos:
            convertido = list(dato)
            convertido[4] = "********"  # Oculta la contraseña
            nuevos_datos.append(convertido)
        headers = ["ID", "Nombre", "URL", "Nombre de usuario", "Contraseña", "Descripción"]
        tabla = tabulate(nuevos_datos, headers, tablefmt="fancy_grid")
        print('\n\t\t\t\tTodas las contraseñas')
        print(tabla)
    except Exception as e:
        print(f"Error al mostrar las contraseñas: {e}")

def buscar_contrasena():
    """
    Permite al usuario buscar una contraseña específica por su ID.
    """
    try:
        contrasena_maestra = getpass("Ingrese su contraseña maestra: ").strip()
        respuesta = Usuario.comprobar_contrasena_maestra(1, contrasena_maestra)
        if len(respuesta) == 0:
            print(MSG_ERROR_CONTRASENA)
        else:
            id = input("Ingrese el ID de la contraseña que desea buscar: ").strip()
            datos = Contrasena.buscar_contrasena(id)
            if not datos:
                print("No se encontró la contraseña.")
            else:
                headers = ["ID", "Nombre", "URL", "Nombre de usuario", "Contraseña", "Descripción"]
                tabla = tabulate(datos, headers, tablefmt="fancy_grid")
                print('\n\t\t\t\tContraseña encontrada')
                print(tabla)
    except Exception as e:
        print(f"Error al buscar la contraseña: {e}")

def modificar_contrasena():
    """
    Permite al usuario modificar una contraseña existente.
    """
    try:
        contrasena_maestra = getpass("Ingrese su contraseña maestra: ").strip()
        respuesta = Usuario.comprobar_contrasena_maestra(1, contrasena_maestra)
        if len(respuesta) == 0:
            print(MSG_ERROR_CONTRASENA)
        else:
            id = input("Ingrese el ID de la contraseña que desea modificar: ").strip()
            datos = Contrasena.buscar_contrasena(id)
            if not datos:
                print("No se encontró la contraseña.")
            else:
                nombre = input("Ingrese el nuevo nombre de la contraseña: ").strip()
                url = input("Ingrese la nueva URL: ").strip()
                nombre_usuario = input("Ingrese el nuevo nombre de usuario: ").strip()
                contrasena = input("Ingrese la nueva contraseña: ").strip()
                descripcion = input("Ingrese una nueva descripción: ").strip()
                respuesta = Contrasena.modificar_contrasena(id, nombre, url, nombre_usuario, contrasena, descripcion)
                print(respuesta)
    except Exception as e:
        print(f"Error al modificar la contraseña: {e}")

def eliminar_contrasena():
    """
    Permite al usuario eliminar una contraseña existente por su ID.
    """
    try:
        contrasena_maestra = getpass("Ingrese su contraseña maestra: ").strip()
        respuesta = Usuario.comprobar_contrasena_maestra(1, contrasena_maestra)
        if len(respuesta) == 0:
            print(MSG_ERROR_CONTRASENA)
        else:
            id = input("Ingrese el ID de la contraseña que desea eliminar: ").strip()
            respuesta = Contrasena.eliminar_contrasena(id)
            print(respuesta)
    except Exception as e:
        print(f"Error al eliminar la contraseña: {e}")

# Inicia la aplicación
if __name__ == "__main__":
    iniciar_sesion()