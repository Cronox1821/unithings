# Autor: Fabian Gabriel Maulen Maulen

import os
import time

i = 0
totalIngresos = 0

while True:
    try:
        Pasajes = int(input("Pasajes a vender: "))
        if Pasajes <= 0:
            raise ValueError
    except ValueError:
        print("Error, fuera de rango, no es un numero entero")
    else:
        break
   
for i in range(Pasajes):
    while True:
        try:
            ingreso = int(input(f"Ingrese precio pasaje {i+1}: "))
            if ingreso < 0:
                raise ValueError
        except ValueError:
            print("Error, fuera de rango, ingrese un numero entero.")
            time.sleep(1)
            os.system("cls") 
        else:
            totalIngresos += ingreso
            print(f"Ingresos actuales (previo al redondeo): {totalIngresos}")
            i += 1
            if i == Pasajes:
                break
    if i == Pasajes:
        break

print (f"Ingresos totales: {round(totalIngresos,-1)}")
