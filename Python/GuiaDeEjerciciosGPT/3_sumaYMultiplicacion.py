import os
def asignarVariable(var):
    while True: 
        var = input('Ingresa un numero: ')
        try:
            var = int(var)
#            print('Int')
            return var
        except ValueError:
            try:
                var = float(var)
#                print('Float')
                return var 
            except ValueError:
                print('Valor invalido, tiene que ser un numero')

numeroUno = 'String'
numeroDos = 'String'
numeroTres = 'String'

numeroUno = asignarVariable(numeroUno)
os.system("cls")
numeroDos = asignarVariable(numeroDos)
os.system("cls")
numeroTres = asignarVariable(numeroTres)
os.system("cls")

print(f'Suma dos primeros numeros: {numeroUno} + {numeroDos} = {numeroUno + numeroDos}')
print(f'Suma multiplicada por el tercer numero: {numeroTres} * {numeroUno + numeroDos} = {numeroTres * (numeroUno+numeroDos)}')
