import math
import os
import time                 # Librerias para truncar, limpiar consola, asignar fechas, time.sleep.
import datetime
from datetime import date

today = datetime.datetime.now() # Asignamos la fecha de hoy para luego restarla con el cumpleaños

while True: # Ciclo While para ejecutar el try y que el programa no se caiga al ingresar la fecha en un formato incorrecto
    try:
        bDay = datetime.datetime.fromisoformat(input('Ingrese su cumpleaños en formato YYYY-MM-DD: '))
        break # Break para salir del ciclo While si no hay algun error
    except:
        os.system("cls")
        print(f'Se ha encontrado un error.\nDetalles: {ValueError}') # Se indica que hubo un error y se indica de que tipo.
        time.sleep(1)

diferencia = today - bDay   # Al salir del ciclo While se hace la diferencia de fechas para asi obtener la diferencia en dias

print(f'Tienes {math.trunc(diferencia.days/365)} años') # Dividimos en 365 y truncamos, asi los dias lo pasamos a años
