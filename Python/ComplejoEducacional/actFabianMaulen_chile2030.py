# Autor: Fabian Gabriel Maulen Maulen
from math import trunc
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
    if digito_verificador == rut[-1]:
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
direcciones = []
telefonos = []
ruts = []
dir_pattern = "[A-Za-z]+ +[0-9]"
add = ''
while add != 'n':
    try:
        while True:
            nombres.append(input('Ingrese nombre y apellido del alumno: ')) 
            if len(nombres[-1]) == 0:
                print('El nombre no puede estar vacio, intente nuevamente')
                del nombres[-1]
            else:
                break

        while True:
                direcciones.append(input('Ingrese la direccion del alumno: '))
                if re.search(dir_pattern,direcciones[-1]):
                    break
                else:
                    print('Direccion invalida, asegurese de haber ingresado la direccion en formato [Direccion][Numero]')

        while True:
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
                    print('Numero agregado')
                    break
            else:
                print('El numero no existe, intente nuevamente')
            
            
        while True:
            try:
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
            add = input('Desea agregar otro alumno (s/n): ')
            if add.lower() == "s" or add.lower() == "n":
                break
            else:
                add = 's'
                print('Opcion invalida, intente nuevamente')
    except:
        pass

for pos in range(len(nombres)):
    print(f'Nombre: {nombres[pos]}\nDireccion: {direcciones[pos]}\nTelefono: {telefonos[pos]}\nRut: {ruts[pos]}\n')