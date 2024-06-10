def mostrar_matriz(matriz):
    for row in matriz:
        for col in row:
            print(f'{col:5}',end='')
        print()

def input_matriz(dimension):
    if dimension:
        m = list()
        for row in range(dimension):
            temp_row = list()
            for col in range(dimension):
                temp_row.append(int(input(f'Valor en pos[{row}][{col}]: ')))
            m.append(temp_row)
        return m

def menu():
    print('[A] Sumar dos matrices\n[B] Multiplicar una matriz por un escalar\n[C] Obtener la matriz transpuesta\n[X] Salir')

def dimension_matriz():
    dimension = int(input('Dimensiones de la matriz: '))
    if 1 < dimension < 2**48-1:
        return dimension
    else:
        print('Dimension fuera de rango')
        return 0

def suma_matrices():
    dimension = dimension_matriz()
    print('Matriz 1')
    m1 = input_matriz(dimension)
    print('Matriz 2')
    m2 = input_matriz(dimension)
    m3 = list()
    for row in range(dimension):
        temp_row = list()
        for col in range(dimension):
            temp_row.append(m1[row][col] + m2[row][col])
        m3.append(temp_row) 
    print('Suma de la matriz: ')
    mostrar_matriz(m3)
         
def multiplicar_matriz_escalar():
    dimension = dimension_matriz()
    escalar = int(input('Escalar: '))
    print('Datos de la Matriz')
    m = input_matriz(dimension)
    m2 = list()
    for row in m:
        temp_row = list()
        for col in row:
            temp_row.append(col * escalar)
        m2.append(temp_row)
    print('Matriz final: ')
    mostrar_matriz(m2)

def matriz_transpuesta():
    dimension = dimension_matriz()
    print('Datos de la Matriz')
    m = input_matriz(dimension)
    m2 = list()
    m2_lc = [[m[j][i] for j in range(dimension)] for i in range(dimension)]

    for i in range(dimension):
        temp_row = list()
        for j in range(dimension):
            temp_row.append(m[j][i])
        m2.append(temp_row)

    print('Matriz transpuesta')
    mostrar_matriz(m2)
    mostrar_matriz(m2_lc)

def main():
    menu()
    while (step := input().upper()) != 'X':
        if step == 'A':
            suma_matrices()
        elif step == 'B':
            multiplicar_matriz_escalar()
        elif step == 'C':
            matriz_transpuesta()
        else:
            print('Opcion Invalida')
        menu()

if __name__ == '__main__':
    main()