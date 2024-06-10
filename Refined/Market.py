products = {
            'Tomate': 500, 
            'Leche': 900,
            'Huevos': 2500,
            'Harina': 1000,
            'Levadura': 500,
            'Mantequilla': 2300,
            'Queso': 4000,
            'Vienesas': 3000
}

total_afecto = int()

for key,value in products.items():
    total_afecto += int(input(f'{key}\n{value}\nIngrese cantidad: ')) * value
    print()

print(f'Detalle pago: \nTotal afecto: {total_afecto:,}\nIva: {total_afecto * 0.19:,}\nTotal a pagar: {total_afecto * 1.19:,}')