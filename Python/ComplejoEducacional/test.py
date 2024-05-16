from math import trunc
rut = '213427989'
flag = bool
aritmetica = 0
temp = 0
serie = 2
rut_temp = rut[:-1]
print(rut_temp[::-1])
for char in rut_temp[::-1]:
    aritmetica = aritmetica + (int(char) * serie) 
    print(f'{char} x {serie} = {int(char)*serie}\n')
    if serie == 7:
        serie = 2
    else:
        serie +=1

print(aritmetica)
temp = aritmetica
aritmetica = (trunc(aritmetica/11)) * 11
print(aritmetica)
temp = abs(temp-aritmetica)
print(temp)
temp = 11 - temp
print(temp)
if temp == 10:
    digito_verificador = 'K'
elif temp == 11:
    digito_verificador = '0'
else:
    digito_verificador = str(temp)

print(f'Last {rut[-1]} / {digito_verificador} Calc')
if digito_verificador == rut[-1]:
    flag = True
else:
    flag = False

print('Valido') if flag else print('Invalido')