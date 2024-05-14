# Autor: Fabian Gabriel Maulen Maulen
def calcularRut(rut):
    for char in rut:
        pass

def verificarRepeticion(num):
    for char in num:
        contador = 0
        for i in len.num()-1:
            if char == num[i+1]:
                contador += 1
        if contador >= 4:
            return False


import re
nombres = []
direcciones = []
telefonos = []
ruts = []
dir_pattern = "[A-Za-z]+ +[0-9]"
add = ''
while add != 'n':
    try:
        nombres.append(input('Ingrese nombre y apellido del alumno: ')) 
        while True:
                direcciones.append(input('Ingrese la direccion del alumno: '))
                if re.search(dir_pattern,direcciones[-1]):
                    break
                else:
                    print('Direccion invalida, asegurese de haber ingresado la direccion en formato [Direccion][Numero]')
        while True:
            try: 
                num = input('Ingrese numero de telefono del alumno: ')
                telefonos.append(num)
                print(telefonos[-1])
                print(len(telefonos[-1]))
                if len(num) != 8 and not num.isdigit():
                    print(f'Longitud del numero "{telefonos.pop(-1)}" invalida, asegurese de que el numero sea de 8 digitos')
                else:
                    print('Numero agregado')
                    break
            except ValueError:
                del telefonos[-1]
                print('Numero ingresado invalido, se ha detectado un caracter, intente nuevamente ingresando solo numeros')
        #while True:
        #    ruts.append(input('Ingrese rut sin puntos y sin guion: '))
        #    if 8 >= len(ruts[-1]) >= 9:
        #        
        #        break
        #    else:
        #        print('Rut invalido, intente nuevamente')

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
    print(f'Nombre: {nombres[pos]}\nDireccion: {direcciones[pos]}\nTelefono: {telefonos[pos]}\n')