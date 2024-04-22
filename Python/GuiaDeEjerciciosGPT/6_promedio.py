numeros = []
for i in range(3):
    numero_valido = False
    while not numero_valido:
        try:
           numeros.append(float(input(f'Ingresa numero {i+1}: ')))
           numero_valido = True
        except ValueError:
            print('Invalido, intenta nuevamente')

promedio = sum(numeros)/len(numeros)

print(f'Promedio: {promedio:.1f}')
