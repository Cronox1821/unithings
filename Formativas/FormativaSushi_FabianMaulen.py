# Autor: Fabian Gabriel Maulen Maulen
import os
import time

#print(len('******************************')) # 30

class customError(Exception):
    pass

def div():
    for _ in range(30):
        print('*', end='')

def cleanWait(x):
    time.sleep(x)
    os.system("cls")

def menu():
    print('1. Pikachu Roll $4500\n2. Otaku Roll $5000\n3. Pulpo Venoso Roll $5200\n4. Anguila Electrica Roll $4800\n5. Para finalizar su pedido.\n')

opcion_usuario = None
pedido = [0,0,0,0]
cantidad = [0,0,0,0]
total = 0
pago_sin_descuento = 0
pago_final = 0
texto_descuento = 'a'
descuento = 0

while True:
    pedido.clear()
    cantidad.clear()
    cantidad = [0,0,0,0]
    descuento = 0
    primera = 0
    try:
        while True:
            try:
                menu()
                opcion_usuario = int(input('Porfavor ingrese su pedido ingresando el numero correspondiente: '))
                match opcion_usuario:
                    case 1:
                        pedido.append(4500)
                        cantidad[0] += 1
                        total += 1
                        primera = 1
                    case 2:
                        pedido.append(5000)
                        cantidad[1] += 1
                        total += 1
                        primera = 1
                    case 3:
                        pedido.append(5200)
                        cantidad[2] += 1
                        total += 1
                        primera = 1
                    case 4:
                        pedido.append(4800)
                        cantidad[3] += 1
                        total += 1
                        primera = 1
                    case 5:
                        if not primera:
                            cleanWait(0)
                            print('No puedes finalizar sin agregar un sushi, intenta nuevamente.')
                            cleanWait(2)
                        else:
                            break
                    case _:
                        os.system("cls")
                        print('Valor invalido, intente nuevamente')
                        cleanWait(1)
            except ValueError:
                print('Error, valor ingresado invalido, intente nuevamente')
                cleanWait(2)
            finally:
                cleanWait(0)
        pedido_sin_descuento = sum(pedido)
        while True: 
            try:
                opcion_usuario = int(input('Posee codigo de descuento?\n1) Tengo codigo de descuento\n2) No tengo codigo de descuento\n'))
                match opcion_usuario:
                    case 1:
                        opcion_usuario = input('Ingrese su codigo de descuento: ')
                        if opcion_usuario == 'soyotaku':
                            print('Codigo de descuento aplicado')
                            descuento = 1920
                            cleanWait(2)
                            break
                        else:
                            raise ValueError('Codigo de descuento no valido.')
                    case 2:
                        break
            except ValueError as e:
                print(f'Error: {e}. Intente nuevamente.')
            finally:
                cleanWait(0)
        # Detalle compra
        div()
        print(f'\nTotal productos: {total}')
        div() 
        print(f'\nPikachu Roll: {cantidad[0]}')
        print(f'Otaku Roll: {cantidad[1]}')
        print(f'Pulpo Venenoso Roll: {cantidad[2]}')
        print(f'Anguila Electrica Roll: {cantidad[3]}\n')
        div()
        print(f'\nSubtotal por paga: ${pedido_sin_descuento}')
        print(f'Descuento por codigo: ${descuento}')
        print(f'TOTAL: ${pedido_sin_descuento-descuento}')
         
        while True:
            try:
                opcion_usuario = int(input('1) Hacer otro pedido\n2) Finalizar\n'))
                match opcion_usuario:
                    case 1:
                        break
                    case 2:
                        break
            except ValueError as e:
                print(e)
        match opcion_usuario:
            case 1:
                pass
            case 2:
                pass
        if opcion_usuario == 2:
            print('Chao!11!111!!!')
            break

    except ValueError:
        print('Error, valor ingresado invalido, intente nuevamente')
        cleanWait(2)
   
    finally:
        cleanWait(2)
