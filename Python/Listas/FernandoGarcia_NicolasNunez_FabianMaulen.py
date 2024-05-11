# Autores: Fernando Garcia, Nicolas Nuñez, Fabian Maulen 
import time
import os
nombres = []
programa = 0
while True:
    try:
        while True:
            programa = int(input('*'*10 + ' HUB Programas ' + '*'*10 + '\n1) Almacenar 3 Nombres y mostrar el de mayor caracteres\n2) Dos listas\n3) Almacenar nombres hasta un no y eliminar el de menor caracteres\n4) Menu registrar usuarios\n5) Venta de supermercado\n0) Salir\nPrograma a ejecutar: '))
            break
    except ValueError:
        print('Caracter detectado, se esperaba un numero, intente nuevamente')
        time.sleep(2)
        os.system("cls")

    match programa:
        case 1:
            input("Programa 1, presione enter para continuar")
            os.system("cls")
            for i in range(3):
                nombres.append(input(f'Ingrese nombre {i+1}: '))

            for i in range(len(nombres)-1):
                for j in range(len(nombres)-1-i):
                    if len(nombres[j]) > len(nombres[j+1]):
                        aux = nombres[j+1]
                        nombres[j+1] = nombres[j]
                        nombres[j] = aux
            print(nombres[-1])
            input('Fin programa, presione enter para continuar')
            os.system('cls')
        case 2:
            input('Programa 2, presione enter para continuar')
            os.system('cls')
            nombres = [] 
            apellidos = []

            for i in range(3):
                nombres.append(input(f'Ingrese nombre {i+1}: '))
                apellidos.append(input('Ingrese apellido: '))


            for i in range(3):
                print(f'{nombres[i]} {apellidos[i]}')

            input('Fin programa, presione enter para continuar')
            os.system('cls')
        case 3: 
            nombres = []
            aux = 'a'

            while aux != 'no':
                nombres.append(input('Ingrese nombre: '))
                while True:
                    aux = input('Desea agregar otro nombre? Si/No: ').lower()
                    if aux == 'si' or aux == 'no':
                        break
                    else:
                        print('Valor invalido, intente nuevamente')

            for i in range(len(nombres)-1):
                for j in range(len(nombres)-1-i):
                    if len(nombres[j]) > len(nombres[j+1]):
                        aux = nombres[j+1]
                        nombres[j+1] = nombres[j]
                        nombres[j] = aux

            print(nombres)
            print(f'Nombre con menos caracteres: {nombres.pop(0)}')
            print(nombres)
            input('Fin programa, presione enter para continuar')
            os.system("cls")
        case 4:
            opcion = 0
            usuarios = []
            passwords = []
            usr_input = ''
            pwd_input = ''
            while True:
                print('*'*30)
                while True:
                    try:
                        opcion = int(input('1. Inicio sesion\n2. Registrar usuario\n3. Eliminar usuario\n4. Salir\nIngrese el numero de su opcion: \n'+'*'*30+'\n'))
                        break
                    except ValueError:
                        print('Error, caracter detectado, se esperaba numero, intente nuevamente')
                        time.sleep(2)
                        os.system("cls")
                match opcion:
                    case 1:
                        if len(usuarios) > 0:
                            usr_input = input('Ingrese nombre de usuario: ')
                            pwd_input = input('Ingrese contraseña: ')
                            if usr_input in usuarios:
                                if pwd_input == passwords[usuarios.index(usr_input)]:
                                    print('Sesion iniciada')
                                else:
                                    print('Contraseña incorrecta')
                            else:
                                print('Usuario incorrecto')
                        else:
                            print('No existen usuarios')
                    case 2:
                        usuarios.append(input('Ingrese nombre de usuario: '))
                        passwords.append(input('Ingrese contraseña: '))
                    case 3:
                        if len(usuarios) > 0:
                            for i in range(len(usuarios)):
                                print(f'ID {i} | Usuario {usuarios[i]}')
                            while True:
                                try:
                                    opcion = int(input('Ingrese el id correspondiente de cada usuario para eliminar'))
                                    del usuarios[opcion]
                                    break
                                except ValueError:
                                    print('Valor ingresado invalido, ingrese un numero')
                                    time.sleep(2)
                                    os.system("cls")
                        else:
                            print('No existen usuarios')
                    case 4:
                        break
                    case _:
                        pass
        case 5:
            canasta = []
            while True:
                opcion = 0
                productos = [{'ID': '1','Producto': 'Platano','Precio': 2300},
                             {'ID': '2','Producto': 'Manzana','Precio': 1500},
                             {'ID': '3','Producto':'Gato','Precio':5700},
                             {'ID': '4','Producto':'Pez','Precio':1200},
                             {'ID': '5','Producto':'Canela','Precio': 1000}]
                while True:
                    try:
                        opcion = int(input('*'*40+'\n1) Agregar productos\n2) Ver canasta\n3) Ver total\n4) Salir\n'+'*'*40+'\n'))
                        break
                    except ValueError:
                        print('Valor ingresado invalido, ingrese un numero')
                        time.sleep(2)
                        os.system("cls")
                match opcion:
                    case 1:
                        while True:
                            while True:
                                try:
                                    os.system("cls")
                                    for produto in productos:
                                        print(f"{produto['Producto']}: ${produto['Precio']}\t{produto['ID']}")
                                    prod_add = int(input('ID del producto a agregar | 0 Para salir\n'))
                                    break
                                except ValueError:
                                    print('Valor ingresado invalido, ingrese un numero')
                                    time.sleep(2)
                                    os.system("cls")
                            if prod_add < 6 and prod_add > 0:
                                canasta.append(productos[prod_add-1])
                                print('Producto Agregado A La Canasta')
                            elif prod_add == 0:
                                break
                            else:
                                print('Invalido')

                            input('Enter')
                    case 2:
                        for producto in canasta:
                            print(f'{producto["Producto"]}')
                    case 3:
                        total = sum(producto['Precio'] for producto in canasta) # Comprension de listas
                        print(f'Total: ${total}')
                    case 4:
                        break
                    case _:
                        pass
        case 0:
            break
        case _:
            print('Invalido')
