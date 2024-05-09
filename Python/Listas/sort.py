import os
#import random
nombres = [6,3,8,9,5,4,2,7,1]
iteraciones = 0
iteracionesi = 0
#random.shuffle(nombres)
print('Long: ',len(nombres))
print('Lista inicial: ',nombres)
for i in range(len(nombres)-1):
    for j in range(len(nombres)-1-i):
        print('-'*39)
        print('Limite j: ',len(nombres)-i-1)
        print(f'Posicion Actual: {j} comparando con {j+1}')
        print(f'Comparando {nombres[j]} > {nombres[j+1]}')
        if nombres[j] > nombres[j+1]:
            print('\n'+'*'*10+'Actualizacion lista'+'*'*10)
            print(nombres)
            aux = nombres[j+1]
            nombres[j+1] = nombres[j]
            nombres[j] = aux
            print(nombres,'\n')
        iteraciones += 1
    iteracionesi += 1

print('Iteraciones bucle i: ',iteracionesi)
print('Iteraciones bucle j: ',iteraciones)
input('Waiting input')
os.system("cls")
iteraciones = 0
iteracionesi = 0
nombres = [6,3,8,9,5,4,2,7,1]
for _ in range(len(nombres)):
    for i in range(len(nombres)-1):
        if nombres[i] > nombres[i+1]:
            aux = nombres[i+1]
            nombres[i+1] = nombres[i]
            nombres[i] = aux
        iteraciones += 1
    iteracionesi += 1

print('Iteraciones bucle i: ',iteracionesi)
print('Iteraciones bucle j: ',iteraciones)
