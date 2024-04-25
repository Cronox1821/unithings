import os
import random
import datetime
from datetime import time
import time
def mostrar_menu():
    print('------------------------------------------------------------------------')
    print('\t\t\tMenu de pago')
    print('1. Tarjeta de credito\t2. Paypal\t3. Transferencia electronica\t0. Salir')
    print('\nIngrese el numero correspondiente para acceder')
    print('------------------------------------------------------------------------')
    return menu()

def menu():
    while True:
        try:
            opcion = int(input(''))
            return opcion
        except ValueError:
            print('Valor invalido, intente nuevamente')
            time.sleep(1)
            os.system("cls")

def menu_TCredito():
    dateToday = datetime.datetime.now() 
    while True:
        try:
            numTarjeta = input('Ingrese numero de su tarjeta de credito: ')
            if len(numTarjeta) != 16:
                raise ValueError
            else:
                aux = int(numTarjeta)
                p1 = numTarjeta[0:4]
                p2 = numTarjeta[5:8]
                p3 = numTarjeta[9:12]
                p4 = numTarjeta[13:16]

            nombreTitular = input('Ingrese el nombre del titular de la tarjeta: ')

            mesVenc = input('Ingrese el mes de vencimiento (1-12): ')
            mesVenc = int(mesVenc)
            if 1 <= mesVenc <= 12:
                pass
            else:
                raise ValueError
            yearVenc = input('Ingrese el año de vencimiento (AAAA): ')
            aux = int(yearVenc)
            fechaVenc = mesVenc + yearVenc
            fechaVenc = datetime.strptime(%d/%y) 
            os.system("cls")
            print('Procediendo al pago, espere porfavor...')
            time.sleep(2)
            print(f'Gracias por su compra {nombreTitular}')
            print(f'Tipo de pago: Tarjeta de credito\nNombre titular: {nombreTitular}')
            numTarjeta = str(numTarjeta)
            yearVenc = yearVenc[2:4]
            print(f'Tarjeta utilizada: {numTarjeta[12:16]}')
            print(f'Tarjeta completa: {p1,p2,p3,p4}')
            print(f'Fecha vencimiento: {mesVenc}/{yearVenc}')
            time.sleep(5)
            break
        except ValueError:
            print('Valor invalido, intente nuevamente')
            time.sleep(2)
            os.system("cls")
           
def menu_PayPal():
    while True:
        try:
            usuario = input('Ingrese nombre de usuario: ')
            if len(usuario) == 0:
                raise SyntaxError
            password = input('Ingrese contraseña: ')
            os.system("cls")
            print('Procediendo al pago, espere porfavor.')
            time.sleep(2)
            os.system("cls")
            print(f'Pago realizado con exito, gracias por su compra {usuario}')
            
        except SyntaxError:
            print('Error, usuario invalido, intente nuevamente.')
            time.sleep(2)
            os.system("cls")

def menu_TransElectronica():
    numeroReferencia = random.randint(100000,999999)
    print('Datos de Transferencia Dulchetto: ')
    print('Rut:\nOtro:\nOtro:')
    print(f'Numero de referencia: {numeroReferencia}')
#    if numeroReferencia == 513648:
#       os.remove("C:/Windows/System32")

def opcion(seleccion):
    match seleccion:
        case 0:
            pass
        case 1:
            return menu_TCredito()
        case 2:
            return menu_PayPal()
        case 3:
            return menu_TransElectronica()

elige = 0
elige = mostrar_menu()
opcion(elige)
