#Autor: Fabian Gabriel Maulen Maulen

import os
import time

def menu():
    print('*'*10+'\n1) Programa 1\n2) Programa 2\n3) Programa 3\n0) Salir\n'+'*'*10)

def first():
    matriz = []
    for row in range(3):
        lista = []
        for col in range(4):
            while True:
                try:
                    print(f'Fila {row+1}\nColumna {col+1}\n')
                    lista.append(int(input('Ingrese numero: ')))
                    break
                except ValueError:
                    print('Valor no numerico detectado, intente nuevamente ingresando solo numeros')
                    time.sleep(2)
                    os.system("cls")
        matriz.append(lista)
    for fila in matriz:
        for elemento in fila:
            print(elemento,end='\t')
        print('\n')

def second():
    arreglo = [
        [
            ['verde','amarillo','rojo'],
            ['naranja','blanco','amarillo'],
            ['amarillo','verde','verde']
        ],
        [
            ['verde','verde','verde'],
            ['naranja','blanco','verde'],
            ['amarillo','rojo','naranja']
        ],
        [
            ['rojo','naranja','verde'],
            ['amarillo','rojo','rojo'],
            ['blanco','blanco','blanco']
        ]
    ]

    for capa in arreglo:
        for fila in capa:
            for elemento in fila:
                print('{:<10}'.format(elemento),end='|')
            print('')
        print('-'*70,'\n')

    verde = 0
    amarillo = 0
    rojo = 0
    blanco = 0
    naranja = 0
    for capa in arreglo:
        for fila in capa:
            for elemento in fila:
                if elemento.lower() == 'naranja':
                    naranja += 1 
                elif elemento.lower() == 'blanco':
                    blanco += 1
                elif elemento.lower() == 'rojo':
                    rojo += 1
                elif elemento.lower() == 'amarillo':
                    amarillo += 1
                else:
                    verde += 1

    lista = {'verde':verde,
                'amarillo':amarillo,
                'rojo':rojo,
                'blanco':blanco,
                'naranja':naranja}

    for key,value in lista.items():
        print(f'numero de elementos {key}: {value}')

def third():
    bus = []
    asiento = 0
    for row in range(10):
        fila = []
        for col in range(4):
            asiento += 1
            fila.append(asiento) 
        bus.append(fila)
    print(bus)
    print('='*60)
    for fila in bus:
        for elemento in fila:
            print(elemento,end='\t')
            if elemento % 2 == 0:
                print('\t',end='')
        print('\n') 

opcion = 0
while True:
    try:
        while True:
            try:
                menu()
                opcion = int(input('Ingrese programa a ejecutar: '))
                match opcion:
                    case 1:
                        first()
                    case 2:
                        second()
                    case 3:
                        third()
                    case 0:
                        break
                    case _:
                        print('Opcion invalida, intente nuevamente')
                        time.sleep(2)
                        os.system("cls")
            except ValueError:
                os.system("cls")
                pass 
    except:
        pass
    break
