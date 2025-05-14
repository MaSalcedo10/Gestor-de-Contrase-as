import os
from getpass import getpass
from tabulate import tabulate
from Conexion import *
import Usuario

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
            print("Añadir contraseña")
        elif opcion == '2':
            print("Mostrar contraseñas")
        elif opcion == '3':
            print("Mostrar una contraseña")
        elif opcion == '4':
            print("Modificar contraseña")
        elif opcion == '5':
            print("Eliminar contraseña")
        elif opcion == '6':
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

iniciar_sesion()  