row = 3
col = 4
matriz = []
contador = 0
manual = True
if manual:
    for r in range(row):
        fila = []
        for c in range(col):
            fila.append(int(input((f'Fila actual: {r+1}\nColumna actual:{c+1}\nIngrese numero: '))))
        matriz.append(fila)
else:
    for r in range(row):
        fila = []
        for c in range(col):
            contador +=1
            fila.append(contador)
            #elemento = int(input('Ingrese numero: '))
            #fila.append(elemento)
        matriz.append(fila)
print('*'*30)
print(matriz)
print('*'*30)
for fila in range(row):
    for columna in range(col):
        print(matriz[fila][columna],end='\t')
    print('\n')
print('*'*30+'Este codigo cumple lo mismo, pero mas sencillo y directo'+'*'*30)
for fila in matriz:
    for elemento in fila:
        print(elemento,end='\t') 
    print('\n')