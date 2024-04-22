import os
def calculoFahrenheit(farenjeit):
    celsio = (5/9) * (farenjeit-32)
    return celsio

farengei = 0.0

while True:
    try:
        farengei = float(input('Ingresa la temperatura en farenhei boludito: '))
        os.system("cls")
        break
    except ValueError:
        print('Taradito te equivocaste')

celsio = calculoFahrenheit(farengei)

print(f'La temperatura en celsio es : {celsio:.1f}')
