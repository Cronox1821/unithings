import time
import os
palabra = input('Ingresa una palabra: ')
os.system("cls")
print(palabra[0])
time.sleep(2)
while True:
    try:
        indice = int(input(f'Ingresa un numero menor a {len(palabra)} y mayor a 0: '))
        if  0 < indice < len(palabra):
            break
        else:
            raise ValueError 
    except ValueError:
        print('Intenta nuevamente')
        time.sleep(1)
        os.system("cls")

print(f'Caracter encontrado en la posicion {indice}: {palabra[indice]}')
