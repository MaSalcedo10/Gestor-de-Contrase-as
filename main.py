import os
from getpass import getpass
from tabulate import tabulate
from Conexion import *
import Usuario
import Contrasena

conexion = conectar()
crear_tablas(conexion)

def iniciar_sesion():
    os.system('cls')
    comprobar = Usuario.comprobar_usuario()
    if len(comprobar) == 0:
        print("Bienvenido, por favor registre su usuario")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        contrasena_maestra = getpass("Ingrese su contraseña maestra: ")
        respuesta = Usuario.registrar(nombre, apellido, contrasena_maestra)
        if respuesta == 'Usuario registrado exitosamente':
            print(f"Bienvenido, su usuario ha sido registrado exitosamente{nombre}")
            menu()
        else:
            print(respuesta)
    else:
        contrasena_maestra = getpass("Ingrese su contraseña maestra: ")
        respuesta = Usuario.comprobar_contrasena_maestra(1, contrasena_maestra)  
        if len(respuesta) == 0:
            print("Contraseña maestra incorrecta")
        else:
            print('Bienvenido')
            menu()          

def menu():
    while True:
        print('''Bienvenido a la aplicación de gestión de contraseñas, \n
              selecciones una de las siguientes opciones''')
        print("\t1- Añadir contraseña")
        print("\t2- Mostrar contraseñas")
        print("\t3- Mostrar una contraseña")
        print("\t4- Modificar contraseña")
        print("\t5- Eliminar contraseña")
        print("\t6- Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == '1':
            nueva_contrasena()
        elif opcion == '2':
            mostrar_contrasenas()
        elif opcion == '3':
            buscar_contrasena()
        elif opcion == '4':
            print("Modificar contraseña")
        elif opcion == '5':
            print("Eliminar contraseña")
        elif opcion == '6':
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

def nueva_contrasena():
    nombre = input("Ingrese el nombre de la contraseña: ")
    url = input("Ingrese la URL: ")
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    descripcion = input("Ingrese una descripción: ")    
    respuesta = Contrasena.registrar(nombre, url, nombre_usuario, contrasena, descripcion)
    print(respuesta)

def mostrar_contrasenas():
    datos = Contrasena.mostrar_contrasenas()
    nuevos_datos = []
    for dato in datos:
        convertido = list(dato)
        convertido[4] = "********"
        nuevos_datos.append(convertido)
        
    headers = ["ID", "Nombre", "URL", "Nombre de usuario", "Contraseña", "Descripción"]
    tabla = tabulate(nuevos_datos, headers, tablefmt="fancy_grid")
    print('\t\t\t\tTodas las contraseñas')
    print(tabla)

def buscar_contrasena():
    contrasena_maestra = getpass("Ingrese su contraseña maestra: ")
    respuesta = Usuario.comprobar_contrasena_maestra(1, contrasena_maestra)
    if len(respuesta) == 0:
        print("Contraseña maestra incorrecta")
    else:
        id = input("Ingrese el ID de la contraseña que desea buscar: ")
        datos = Contrasena.buscar_contrasena(id)
        if len(datos) == 0:
            print("No se encontró la contraseña")
        else:
            headers = ["ID", "Nombre", "URL", "Nombre de usuario", "Contraseña", "Descripción"]
            tabla = tabulate(datos, headers, tablefmt="fancy_grid")
            print('\t\t\t\tContraseña encontrada')
            print(tabla)

iniciar_sesion()  