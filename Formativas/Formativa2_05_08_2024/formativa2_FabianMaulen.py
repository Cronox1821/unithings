# Autor: Fabian Gabriel Maulen Maulen
# Seccion: FPY1101
import os
import time

def constraints():
    print('Puede ingresar hasta 3 artefactos por dia\tDe no hacer uso de algun artefacto, ingresar la opcion 6\tEsta secuencia se repetira 3 veces por dia')

def tabla():
    print('1) Hervidor\t2) Microondas 800 watts\t3) Aspiradora 1400 watts\n4) Secador de pelo 1800 watts\t5) Lavadora/Secadora\t 6) No hay uso')

opcion = 0
consumo_total = 53.2
consumo_og = 0.0
flag = False

while True:
    try:
        integrantes = int(input('Numero de integrantes de su grupo familiar: '))
        if 0 < integrantes <= 5:
            consumo_total *= integrantes
            while True:
                try:
                    constraints()
                    input('Presione enter para continuar')
                    for miembro in range(integrantes):
                        for dia in range(7):
                            for artefacto in range(3):
                                while True:
                                    try:
                                        os.system("cls")
                                        print(f'Miembro {miembro+1}')
                                        print(f'Dia {dia+1}')
                                        tabla()
                                        opcion_usuario = int(input(f'({artefacto}/3) Artefacto utilizado: '))
                                        match opcion_usuario:
                                            case 1:
                                                consumo_total += 5.9
                                                break
                                            case 2:
                                                consumo_total += 0.8
                                                break
                                            case 3:
                                                consumo_total += 7.0
                                                break
                                            case 4:
                                                consumo_total += 4.5
                                                break
                                            case 5:
                                                consumo_total += 2.1
                                                break
                                            case 6:
                                                break
                                            case _:
                                                print('Opcion invalida, intente nuevamente')
                                                time.sleep(1)
                                    except ValueError:
                                        print('Valor invalido, intente nuevamente')
                                        time.sleep(1)
                    break
                except:
                    pass
            break
        else:
            print('Valor ingresado fuera de rango, no puede ser menor a 0 y mayor a 5')
            time.sleep(1)
            os.system("cls")
    except ValueError:
        print('Valor ingresado invalido, intente nuevamente')
        pass
os.system("cls")
print(f'Consumo semanal total: {consumo_total:.1f}kWh')
