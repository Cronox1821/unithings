# Autor: Fabian Gabriel Maulen Maulen

from datetime import datetime
from datetime import date
import os
import math
import time

class fechaDiferida(Exception): # Definicion de excepcion personalizada para casos especificos
    pass

def cleanWait(): # Funcion para limpiar y esperar
    time.sleep(4)
    os.system("cls")

def div(): # Funcion para generar lineas para separar el menu instructivo
    print('\n')
    for _ in range (100):
        print('-', end = '')
    print('\n')

def constraints(): # Funcion que muestra un menu instructivo:
    div()
    print('Considere lo siguiente:\n1. Evite el uso de dias y meses ficticios\n2. Los años deben de estar en el rango: 1 < año < 3000\n3. No se aceptan cadenas de caracteres, exceptuando los utilizados para el ingreso de fecha\n4. Ingresar incorrectamente el formato indicado de la fecha reiniciara el proceso.\n5. A la hora de ocurrir un error se mostrara un mensaje por pantalla indicando el problema, seguidamente volvera al menu para reintentar el ingreso.\n\nFormatos disponibles: \na) AAAA-MM-DD\nb) AAAA MM DD\nC) AAAAMMDD')
    div()

while True: # Bucle [1] que pide la fecha actual
    try:
        os.system("cls")
        constraints()
        dateNowUser = datetime.fromisoformat(input('Ingrese la fecha de hoy: ').replace(' ','-')) # Convierte el ingreso directamente al formato de fecha, reemplaando de ser necesario los espacios por guiones. Las excepciones ya son controladas
        # dateNowUser = datetime.fromisoformat(dateNowUser) # Tambien funcionaria
        if dateNowUser.date() != datetime.today().date(): # Verifica que la fecha ingresada sea la fecha actual
            raise fechaDiferida(f'La fecha ingresada difiere con la fecha actual, intente nuevamente\nFecha ingresada: {dateNowUser.date()}\nFecha esperada: {datetime.today().date()}')
        os.system("cls")
        while True: # Bucle [2] que pide una fecha bajo las condiciones dadas
                try:
                    os.system("cls")
                    constraints()
                    dateCustomUser = datetime.fromisoformat(input('Ingrese una fecha para calcular la diferencia: ').replace(' ','-'))
                    if (1 <= dateCustomUser.date().year <= 3000): # Verificacion de los limites de años
                        delta = abs(dateCustomUser.date().year - dateNowUser.date().year) # Obtener diferencia de años
                        months = delta * 12 # La diferencia de años la multiplicamos por 12 para obtener los meses 
                        print(f'La diferencia entre la fecha otorgada por el usuario: {dateCustomUser.date()} y hoy {dateNowUser.date()} es de\nDias: {abs((dateCustomUser.date()-dateNowUser.date()).days)}\no\nMeses: {months}\no\nAños: {delta}') # Calculo diferencia en dias, meses y años
                        break
                    else:
                        raise fechaDiferida('Año fuera de rango, intente nuevamente') 
                except fechaDiferida as e:
                    print(e)
                    cleanWait()
                except Exception as e:
                    print(f'Error: {e}\nIntente nuevamente')
                    cleanWait()
        break
        # Fin Bucle [2]
    except fechaDiferida as e:
        print(e)
        cleanWait()
    except Exception as e:
        print(f'Error: {e}\nIntente nuevamente')
        cleanWait()
# Fin Bucle [1]
