# Autor: Fabian Gabriel Maulen Maulen
# Dulchetto
import os
import random
import time
from datetime import datetime

def cleanWait(x):
    time.sleep(x)
    os.system("cls")

def mostrar_menu():
    while True:
        print('-----------------------------------------------------------------------------------')
        print('\t\t\t\t  Menu de pago')
        print('1. Tarjeta de credito\t2. Paypal\t3. Transferencia electronica\t0. Salir')
        print('\nIngrese el numero correspondiente para acceder')
        print('-----------------------------------------------------------------------------------')
        try:
            opcion = int(input('Seleccion: '))
            return opcion
        except ValueError:
            print('Valor invalido, intente nuevamente')
            cleanWait(2)

def CCNUM():
    numCard = input('Ingrese los numeros de su tarjeta: ')
    if len(numCard) != 16:
        raise ValueError('Longitud fuera de rango, intente nuevamente')
    else:
        blockCard = [
            int(numCard[0:4]),
            int(numCard[4:8]),
            int(numCard[8:12]),
            int(numCard[12:16])
        ]
    return blockCard

def CCTIT():
    nombreTitular = input('Ingrese nombre y apellido del titular de la tarjeta: ')
    if not " " in nombreTitular:
        raise ValueError('Nombre invalido, asegurese de que este separado por un espacio, incluya nombre y apellido')
    return nombreTitular

def CCFECAD():
    fechaCad = input("Ingrese fecha de caducidad incluyendo el caracter especial '-' (AAAA-MM): ")
    if '-' in fechaCad:
        _, month = map(int, fechaCad.split('-'))
        if not 1 < month <= 12 or  len(fechaCad) != 7:
            raise ValueError('Fecha invalida')
        fechaIso = datetime.strptime(fechaCad, "%Y-%m").date()
        fechaActualIso = datetime.today().date().replace(day=1)
        if fechaIso < fechaActualIso:
            raise ValueError('La fecha de caducidad es invalida, intente nuevamente')
    os.system("cls")
    return fechaIso

def menuCredito():
    nombre = 'String'
    numerosTarjeta = []
    fechaCaducidad = datetime.today 
    while True:
        try:    
            numerosTarjeta = CCNUM()
            nombre = CCTIT()
            fechaCaducidad = CCFECAD()
            print(f'Datos de compra:\nComprador: {nombre}\nNumero de tajeta: {' '.join(str(x) for x in numerosTarjeta)}\nFecha de caducidad: {fechaCaducidad}') # List Comprehension
            break
        except ValueError as error:
            os.system("cls")
            print(f'Error, {error}')
            cleanWait(3)
        except Exception:
            os.system("cls")
            print('Error critico, intente nuevamente')
            cleanWait(4)

def menuPaypal():
    while True:
        try:
            usuario = input('Ingrese nombre de usuario: ')
            while True:
                password = input('Ingrese una contraseña fuerte (Incluya mayusculas, minusculas, numeros. Longitud minima 6 caracteres): ')
                upperFlag = False
                lowerFlag = False 
                numberFlag = False
                for char in password:
                    if char.islower():
                        lowerFlag = True
                    if char.isupper():
                        upperFlag = True
                    if char.isdigit(): 
                        numberFlag = True
                if lowerFlag and upperFlag and numberFlag and len(password) >= 6:
                    break
                else:
                    print('Contraseña debil, intenta nuevamente')
                    cleanWait(2)

            print(f'Datos de compra:\nUsuario: {usuario}\nCodigo de compra: {random.randint(100000,999999)}')
            break
        except ValueError:
            pass

def transElec():
    print(f'Banco: Banco de shile\nNombre: Juan\nNumero de cuenta: 1234 5678 9123\nCodigo de referencia {random.randint(100000,999999)}')

while True:
    opcion = mostrar_menu()
    match opcion:
        case 0:
            break
        case 1:
            os.system("cls")
            menuCredito()
        case 2:
            os.system("cls")
            menuPaypal()
        case 3:
            os.system("cls")
            transElec()
