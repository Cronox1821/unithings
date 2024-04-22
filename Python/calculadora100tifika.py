import os
import time

resultado = 0
ereccion = 0
decision = 0

def menu():
    print('----------------------------------------------------------------------------------')
    print('\t\t\t\tCalculadora 100tifika')
    print('----------------------------------------------------------------------------------')
    print('1. Suma\t\t2. Resta\t3. Multiplicacion\t4. Division')

def ingreso(decision):
    decision = int(input('Ingrese opcion: '))
    return decision

def elecciones(eleccion,resultado):
    if eleccion == 1:
        sumaUsuario = input('Ingrese numeros a sumar: ')

    elif eleccion == 2:
        pass
    elif eleccion == 3:
        pass
    elif eleccion == 4:
        pass
    elif eleccion == 5:
        pass
    elif eleccion == 6:
        pass
    elif eleccion == 7:
        pass
    elif eleccion == 8:
        pass
    elif eleccion == 9:
        pass
    elif eleccion == 10:
        pass
    elif eleccion == 11:
        pass
    elif eleccion == 12:
        pass
    elif eleccion == 13:
        pass
    elif eleccion == 14:
        pass
    else:
        raise ValueError

while True:
    try:
        menu()
        ereccion = ingreso(ereccion)
        elecciones(ereccion)
        time.sleep(1)
        break
    except ValueError:
        print('Opcion invalida, intente nuevamente.')
        time.sleep(1)
        os.system("cls")
