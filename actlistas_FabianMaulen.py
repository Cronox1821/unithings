# Autor: Fabian Gabriel Maulen Maulen
import os
nombres = []
programa = 0
while True:
    programa = int(input('*'*10 + ' HUB Programas ' + '*'*10 + '\n1) Almacenar 3 Nombres y mostrar el de mayor caracteres\n2) Dos listas\n3) Almacenar nombres hasta un no y eliminar el de menor caracteres\n4) Menu registrar usuarios\n5) Venta de supermercado\n0) Salir\nPrograma a ejecutar: '))
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
                opcion = int(input('1. Inicio sesion\n2. Registrar usuario\n3. Eliminar usuario\n4. Salir\nIngrese el numero de su opcion: \n'+'*'*30))
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
                            opcion = int(input('Ingrese el id correspondiente de cada usuario para eliminar'))
                            del usuarios[opcion]
                        else:
                            print('No existen usuarios')
                    case 4:
                        break
                    case _:
                        pass
        case 5:
            pass
        case 0:
            break
        case _:
            print('Invalido')
