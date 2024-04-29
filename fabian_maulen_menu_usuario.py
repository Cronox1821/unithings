# Autor: Fabian Gabriel Maulen Maulen
import re
import time
import os

class CustomError(Exception):
    pass

def menu():
    print('1) Iniciar sesion\n2) Registrar usuario\n3) Salir\nIngrese su opcion ingresando el numero correspondiente: ', end='')

def menu_sesion_iniciada():
    print('1) Realizar llamada\n2) Enviar correo electronico\n3) Cerrar sesion\nIngrese su opcion ingresando el numero correspondiente: ', end='')

def registrar_usuario(users,password):
    if len(users) != 3:
        print('Registro de usuarios\n')
        usuario_temp = input('Ingrese nombre de usuario a registrar: ')
        if users.count(usuario_temp) == 0:
            users.append(usuario_temp)
        else:
            raise CustomError('Usuario ya registrado, intente nuevamente')
        password.append(input('Ingrese contraseña a registrar: '))
        print(f'Nombre de usuario ingresado: "{users[len(users)-1]}"\nCantidad de usuarios registrados: {len(users)}')
    else:
        raise CustomError('Limite de usuarios alcanzado')

def clean_wait(x):
    time.sleep(x)
    os.system("cls")



usuarios = []
contrasenas = []
correo = []
mensajeCorreo = []
OPCION = None
SESION_INICIADA = False
EMAIL_PATTERN = "[a-zA-Z0-9]+@[a-zA-Z]+.(com|cl|es|net)"

while True:
    try:
        if not SESION_INICIADA:
            menu() # Despliegue menu
            OPCION = int(input(''))
            match(OPCION):
                case 1: # Iniciar Sesion
                    #if usuario1 == None and usuario2 == None and usuario3 == None:
                    if len(usuarios) == 0: # De no existir usuarios, notifica y se reinicia el bucle
                        raise CustomError('No es posible iniciar sesion, no existen usuarios. Agregue al menos un usuario para Iniciar Sesion') 
                    userSearch = input('Ingrese nombre de usuario: ')
                    if usuarios.count(userSearch) != 0:
                        passSearch = input('Ingrese contraseña: ')
                        if contrasenas[usuarios.index(userSearch)] == passSearch:
                            os.system("cls")
                            time.sleep(2)
                            print(f'Bienvenido {usuarios[usuarios.index(userSearch)]}')
                            SESION_INICIADA = True
                        else:
                            raise CustomError('Contraseña incorrecta, volviendo al menu.')
                    else:
                        raise CustomError('Error, usuario no encontrado, intente nuevamente.')
                case 2:
                    registrar_usuario(usuarios,contrasenas)
                case 3:
                    break
                case _:
                    raise ValueError

        while SESION_INICIADA:
            menu_sesion_iniciada()
            OPCION = int(input(''))
            match(OPCION):
                case 1:
                    NUM_CELULAR = int(input('Ingrese numero para realizar llamada: '))
                    NUM_CELULAR = str(NUM_CELULAR)
                    if len(NUM_CELULAR)!= 9:
                        raise CustomError('Numero fuera de rango, asegurese de haber ingresado 9 digitos y haber incluido el prefijo "9"')
                    clean_wait(2)
                    print('Llamada agendada, espere respuesta en su dispositivo')
                case 2:
                    correoTemp = input('Ingrese correo electronico: ')
                    if re.search(EMAIL_PATTERN,correoTemp):
                        os.system("cls")
                        print('Agregando correo...')
                        clean_wait(2)
                        correo.append(correoTemp)
                        print('Correo agregado correctamente')
                        clean_wait(2)
                    else:
                        raise CustomError('Correo invalido, intente nuevamente')
                case 3:
                    SESION_INICIADA = False
                    break
                case _:
                    raise ValueError

    except CustomError as e:
        print(e)
        clean_wait(2)
    except ValueError:
        print('Valor invalido, porfavor verifique el ingreso de datos e intente nuevamente.')
        clean_wait(2)
    except Exception as e:
        print(f'Error, verifique el codigo de error e intente nuevamente {e}')
        clean_wait(2)
