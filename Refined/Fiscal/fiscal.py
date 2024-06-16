import csv

def obtener_lista_facturacion():
    pass

def imprimir_anhos_con_media():
    pass

def guardar_anhos_cronologicamente():
    pass

def burbuja():
    pass

def menu():
    try:
        while True:
            menu = int(input('[1] Imprimir años con media\n[2] Guardar años cronologicamente\n[3] Salir\nElige: '))
            return menu
    except ValueError:
        print('Se ha ingresado un valor no numerico, intente nuevamente')

def main():
    while (opcion := menu()) != 3:
        match opcion:
            case 1:
                imprimir_anhos_con_media()
            case 2:
                guardar_anhos_cronologicamente()
            case _:
                print('Fuera de rango')
                

if __name__ == '__main__':
    main()
