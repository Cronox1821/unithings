import os
def calcularConsumo():
    while True:
        try:
            km_recorridos = float(input('Ingrese kilometros recorridos: '))
            os.system("cls")
            litros_consumidos = float(input('Ingrese litros consumidos: ')) 
            consumo = litros_consumidos / km_recorridos
            os.system("cls")
            return consumo
        except ValueError:
            print('Valor invalido, intente nuevamente.')

consumo = 1.0

consumo = calcularConsumo()

print(f'Consumo: {consumo:.2f} l/km')
