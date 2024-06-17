import csv
import math
try:
    import tabulate
except ModuleNotFoundError:
    input('No tiene instalado el modulo tabulate, Para continuar, debera instalarlo utilizando pip install tabulate\n')
    exit()
from datetime import datetime

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
    aritmetica = (math.trunc(aritmetica/11)) * 11
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

"""

Register Done

"""


def registrar_reclamo():
    while True:
        try:
            rut = input('Ingrese rut sin puntos y sin guion: ')
            if 8 <= len(rut) <= 9 and not '-' in rut:
                if calcularRut(rut):
                   break
                else:
                    print('El rut ingresado no existe, intente nuevamente')
            else:
                print('Rut invalido, intente nuevamente')
        except ValueError:
            print('Entrada invalida, caracter detectado en el rut, intente nuevamente.')
    while True:
        try:
            monto = int(input('Ingrese monto: '))
            break
        except ValueError:
            print('Ingrese solo digitos, intente nuevamente\n')
    reclamo = input('Ingrese reclamo (No mas de veinte caracteres): ')
    fecha = datetime.now().strftime("%d-%m-%Y")
    while len(reclamo) > 20:
       print('La extension del reclamo no puede ser mayor a veinte caracteres, intente nuevamente')
       reclamo = input('Reclamo: ')
    return {'Rut': rut,'Fecha': fecha, 'Monto': monto, 'Reclamo': reclamo}

"""

Print Done

"""

def listar_reclamos(data):
    if not data:
        print("No hay reclamos registrados.")
    else:
        print(tabulate.tabulate(data, headers="keys", tablefmt="grid"))


"""

Backup Done

"""

def respaldar_reclamos(data):
    with open('reclamos.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["Rut", "Fecha", "Monto", "Reclamo"])
        writer.writeheader()
        for reclamo in data:
            writer.writerow(reclamo)
    print("Reclamos respaldados con exito")

"""

Menu Done

"""

def menu():
    while True:
        try:
            opc = int(input('[1] Registrar reclamo\n[2] Listar reclamos\n[3] Respaldar reclamos\n[4] Salir\n'))
            return opc
        except ValueError:
            print('Valor esperado: Entero\nValor ingresado: Caracter\nIntente nuevamente\n')

"""

Main Done

"""

def main():
    reclamos = list()
    while (opcion := menu()) != 4:
        match opcion:
            case 1:
                reclamos.append(registrar_reclamo())
            case 2:
                listar_reclamos(reclamos)
            case 3:
                respaldar_reclamos(reclamos)
            case _:
                print('Opcion invalida, intente nuevamente')

if __name__ == '__main__':
    main()
