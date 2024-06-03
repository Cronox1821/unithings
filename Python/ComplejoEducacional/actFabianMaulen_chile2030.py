# Autor: Fabian Gabriel Maulen Maulen
import pandas as pd
from math import trunc
from os import system
import re
from collections import Counter

def calcularRut(rut):
    aritmetica = 0
    temp = 0
    serie = 2
    rut_temp = rut[:-1]
    for char in rut_temp[::-1]:
        aritmetica += (int(char) * serie) 
        if serie == 7:
            serie = 2
        else:
            serie +=1
    temp = aritmetica
    aritmetica = (trunc(aritmetica/11)) * 11
    temp = abs(temp-aritmetica)
    temp = 11 - temp
    if temp == 10:
        digito_verificador = 'K'
    elif temp == 11:
        digito_verificador = '0'
    else:
        digito_verificador = str(temp)
    if digito_verificador == rut[-1].upper():
        return True
    else:
        return False

def verificarRepeticion(num):
    digits = re.findall(r'\d',num)

    contador = Counter(digits)

    for count in contador.values():
        if count >= 4:
            return True
    return False

lista_numeros = []

for i in range(10):
    cadena = ''.join(str(( i+j ) % 10 ) for j in range (8))
    lista_numeros.append(cadena)    

nombres = []
apellidos = []
direcciones = []
telefonos = []
ruts = []
dir_pattern = "[A-Za-z]+ +[0-9]"
add = 's'
while add != 'n':
    try:
        while True:
            system("cls")
            nom = input('Ingrese nombre(s) del alumno: ')
            if len(nom) == 0:
                print('El nombre no puede estar vacio, intente nuevamente')
            else:
                nombres.append(nom)
                break
        while True:
            system("cls")
            app = input('Ingrese apellido(s) del alumno: ')
            if len(app) == 0:
                print('La entrada de apellidos no puede ser vacia, intente nuevamente')
            else:
                apellidos.append(app)
                break

        while True:
                system("cls")
                direcc = input('Ingrese la direccion del alumno: ')
                if re.search(dir_pattern,direcc):
                    direcciones.append(direcc)
                    break
                else:
                    print('Direccion invalida, asegurese de haber ingresado la direccion en formato [Direccion][Numero]')

        while True:
            system("cls")
            num = input('Ingrese numero de telefono del alumno: ')
            if not verificarRepeticion(num):
                if len(num) != 8:
                    print(f'Longitud del numero "{num}" invalida, asegurese de que el numero sea de 8 digitos')
                elif not num.isdigit():
                    print(f'Se ha ingresado un caracter, intente nuevamente')
                elif num in lista_numeros:
                    print('Numero invalido, intente nuevamente')
                else:
                    telefonos.append(num)
                    break
            else:
                print('El numero no existe, intente nuevamente')
            
            
        while True:
            try:
                system("cls")
                rut = input('Ingrese rut sin puntos y sin guion: ')
                if 8 <= len(rut) <= 9 and not '-' in rut:
                    if calcularRut(rut):
                        ruts.append(rut)
                        break
                    else:
                        print('El rut ingresado no existe, intente nuevamente')
                else:
                    print('Rut invalido, intente nuevamente')
            except ValueError:
                print('Entrada invalida, caracter detectado en el rut, intente nuevamente.')

        while True:
            system("cls")
            add = input('Desea agregar otro alumno (s/n): ')
            if add.lower() == "s" or add.lower() == "n":
                break
            else:
                add = 's'
                print('Opcion invalida, intente nuevamente')
    except:
        pass

<<<<<<< HEAD
system("cls")
data_dict = {
    'Nombre': nombres,
    'Apellido': apellidos,
    'Direccion': direcciones,
    'Telefono': telefonos,
    'Rut': ruts
}
df = pd.DataFrame(data_dict)
print(df.set_index('Rut'))
=======
nombres = [*range(1,7)]
direcciones = [*range(7,13)]
apellidos = [*range(13,19)]
telefonos = [*range(19,26)]
ruts = [*range(26,33)]

print(nombres)
print(direcciones)
print(apellidos)
print(telefonos)
print(ruts)
print(len(nombres))
print(len(direcciones))

print('{:<0}'.format('Rut'),end='----')
print('{:<5}'.format('Nombre(s)'),end='----')
print('{:<5}'.format('Apellidos'),end='----')
print('{:<5}'.format('Telefono'),end='----')
print('{:<5}'.format('Direccion'))
for pos in range(len(nombres)):
    print('{:<0}'.format(ruts[pos]),end='----')
    print('{:<5}'.format(nombres[pos]),end='----')
    print('{:<5}'.format(apellidos[pos]),end='----')
    print('{:<5}'.format(telefonos[pos]),end='----')
    print('{:<5}'.format(direcciones[pos]))
    #print(f'Nombre: {nombres[pos]}\nDireccion: {direcciones[pos]}\nTelefono: {telefonos[pos]}\nRut: {ruts[pos]}\n')
>>>>>>> eb9dceda55bc6fcb2804cbe987ce2a9a64aaa081
