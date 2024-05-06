import os
import time

class customError(Exception):
    pass

def cleanWait(x):
    time.sleep(x)
    os.system("cls")

def menu():
    print('1) Pikachu Roll $4500\n2) Otaku Roll $5000 \n3) Pulpo Venenoso Roll $5200\n4) Anguila Electrica Roll $4800\n 0) Finalizar compra\n')

flag = True
final = False
pikachu = 0
otaku = 0
pulpo = 0
anguila = 0
total = 0
opcion = 0
descuento = False
total_productos = 0

while True:
    if flag:
        pikachu = 0
        total_productos = 0
        descuento = False
        otaku = 0
        pulpo = 0
        anguila = 0
        total = 0
        opcion = 0
        final = False
        flag = False
    while True:
        try:
            menu()
            opcion = int(input('Ingrese numero de Roll para añadir a la cesta: '))
            match opcion:
                case 1:
                    pikachu += 1
                    pass
                case 2:
                    otaku += 1
                    pass
                case 3:
                    pulpo += 1
                    pass
                case 4:
                    anguila += 1
                    pass
                case 0:
                    if pikachu or otaku or pulpo or anguila:
                        break
                    else:
                        raise customError('Porfavor ingrese al menos un Roll para finalizar su pedido. ')
                case _:
                    raise customError('Valor invalido, intente nuevamente')
            pass
        except customError as e:
            print(e)
            cleanWait(2)
        except ValueError:
            print('Opcion invalida, ingrese un numero indicado en las opciones, intente nuevamente')
            cleanWait(2)
        finally:
            cleanWait(0)
    # Bucle para codigo
    flag = True
    final = True
    while True:
        try:
            os.system("cls")
            opcion = int(input('Posee codigo de descuento?\n1) Si\n2) No\n'))
            match opcion:
                case 1:
                    while True:
                        opcion = input('Ingrese codigo de descuento: ')
                        descuento = True if opcion == 'soyotaku' else False
                        if descuento:
                            final = True
                            break
                        else:
                            try:
                                opcion = input('Ingrese X para volver al menu, ingrese 1 para reingresar un codigo')
                                if opcion == 'x':
                                    final = False
                                    break
                                elif opcion == '1':
                                    pass
                                    
                            except ValueError:
                                if opcion.lower() == 'x':
                                    final = False
                                    opcion = 2
                    break
                case 2:
                    break
                case _:
                    raise customError('Valor invalido, intente nuevamente') 
        except customError as e:
            print(e)
            cleanWait(2)
        except ValueError:
            print('Ingrese una opcion mostrada, intente nuevamente')
            cleanWait(2)

    # Menu y bucle final
    os.system("cls")
    total_productos = pikachu + otaku + pulpo + anguila
    total = (pikachu * 4500) + (otaku * 5000) + (pulpo * 5200) + (anguila * 4800)
    if final:
        print('*'*30)
        print(f'\nTotal productos: {total_productos}')
        print('*'*30)
        print(f'Pikachu Roll: {pikachu}')
        print(f'Otaku Roll: {otaku}')
        print(f'Pulpo Roll: {pulpo}')
        print(f'Anguila Roll: {anguila}')
        print('*'*30)
        print(f'\nSubtotal por pagar: ${total}')
        print(f'Descuento por codigo: ${total * 0.1 if descuento else "N/A"}')
        print(f'Total = ${total * 0.9 if descuento else total}')

    while True:
        try:
            opcion = int(input('Ingrese 1 para realizar otro pedido, ingrese 0 para salir.\n'))
            match opcion:
                case 1:
                    break
                case 0:
                    break
                case _:
                    raise customError('Ingrese una opcion valida')
        except customError as e:
            print(e)
        except ValueError:
            print('Ingrese 1 o 0')
        finally:
            cleanWait(2)
    if opcion == 0:
        break
