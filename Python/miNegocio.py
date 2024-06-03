# Autor: Fabian Gabriel Maulen Maulen
productos = {
    'Tomate': 500,
    'Leche': 900,
    'Huevos': 2500,
    'Harina': 1000,
    'Levadura': 500,
    'Mantequilla': 2300,
    'Queso': 4000,
    'Vienesas': 3000
}

total_afecto = 0

valor_lista = []

for key,value in productos.items():
    while True:
        try:
            cantidad = int(input(f'{key}\n{value}\nIngrese cantidad: '))
            if cantidad < 0:
                raise Exception('La cantidad no puede ser negativa, intente nuevamente\n')
        except ValueError:
            print('Se ha detectado un caracter, porfavor ingrese un numero, intente nuevamente\n')
        except Exception as e:
            print(e)
        else:
            total_afecto += cantidad * value
            valor_lista.append(total_afecto)
            print('')
            break

print(f'Detalle pago:\nTotal afecto: {total_afecto:,}\nIVA: {total_afecto * 0.19:,.1f}\nTotal a pagar: {total_afecto*1.19:,.1f}')