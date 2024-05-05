import os
import time

def rollAgregado():
    print('Roll agregado correctamente')

def menu():
    print('1. Pikachu Roll $4500\n2. Otaku Roll $5000\n3. Pulpo Venenoso Roll $5200\n4. Anguila Electrica Roll $4800\n0. Finalizar Pedido')

while True:
    pikachu = 0 # 4500
    otaku = 0 # 5000
    pulpo = 0 # 5200
    anguila = 0 # 4800
    productos_totales = 0
    descuento = 0
    descuento_aplicado = 0
    total = 0
    total_final = 0
    seleccion = 0
    descuento = 'string'

    while True:
        try:
            os.system("cls")
            menu()
            seleccion = int(input('Ingrese numero de roll a agregar: '))
            match seleccion:
                case 1:
                    pikachu += 1
                    productos_totales += 1
                    total += 4500
                    rollAgregado()
                case 2:
                    otaku += 1
                    productos_totales += 1
                    total += 5000
                    rollAgregado()
                case 3:
                    pulpo += 1
                    productos_totales += 1
                    total += 5200
                    rollAgregado()
                case 4:
                    anguila += 1
                    productos_totales += 1
                    total += 4800
                    rollAgregado()
                case 0:
                    if productos_totales == 0:
                        print('Agregue al menos un roll para finalizar su pedido')
                        time.sleep(2)
                    else:
                        break
                case _:
                    print('Valor invalido, intenta nuevamente')
        except ValueError:
            pass
    total_final = total
    while True:
        try:
            print('1. Tengo codigo de descuento\n2. No tengo codigo de descuento')
            seleccion = int(input('Ingrese el numero correspondiente si tiene o no codigo de descuento: '))
            match seleccion:
                case 1:
                    while True:
                        os.system("cls")
                        try:
                            descuento = input('Ingrese codigo de descuento\n')
                            os.system("cls")
                            if descuento == 'soyotaku':
                                print('Descuento aplicado')
                                total_final = total * 0.9
                                descuento_aplicado = total * 0.1
                                time.sleep(2)
                                break
                            else:
                                while True:
                                    descuento = input('Codigo no valido\nIngrese X para volver al menu, ingrese 1 para reingresar el codigo\n')
                                    if descuento == '1':
                                        break
                                    elif descuento.lower() == 'x':
                                        break
                                    else:
                                        print('Opcion fuera de rango, intente nuevamente')
                                        time.sleep(2)
                                if descuento == '1':
                                    pass
                                else:
                                    break
                        except:
                            pass
                case 2:
                    break
                case _:
                    print('Valor invalido, intente nuevamente)')
            if descuento_aplicado != 0:
                break
        except:
            pass
    os.system("cls")
    print('*'*30)
    print(f'Total productos: {productos_totales}')
    print('*'*30)
    print(f'Pikachu Roll: {pikachu}\nOtaku Roll: {otaku}\nPulpo Venenoso Roll: {pulpo}\nAnguila Electrica Roll: {anguila}')
    print('*'*30)
    print(f'Subtotal por pagar: ${total}\nDescuento por codigo: ${descuento_aplicado}\nTOTAL: ${total_final}')
    print('\n')
    while True:
        try:
            seleccion = int(input('1. Realizar otro pedido\n2. Salir del programa\n'))
            match seleccion:
                case 1:
                    break
                case 2:
                    break
                case _:
                    print('Valor invalido, intente nuevamente.')
        except:
            pass
    if seleccion == 2:
        break
