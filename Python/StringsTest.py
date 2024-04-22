texto = 'Esto es un texto'

print(texto.lower()) # Convertir a minusculas
print(texto.upper()) # Convertir a mayusculas
print(texto.capitalize()) # Convertir el primer caracter a mayusculas y el resto en minusculas
print(texto.title()) # Convertir la primera letra de cada palabra a mayusculas
texto = ' Texto con espacios  '
print(texto.strip().capitalize()) # Strip quita los espacios en blancos
print(texto.capitalize())
print(texto.lstrip()) # lstrip quita los espacios en blancos de la izquierda y rstrip los de la derecha
print(texto.rstrip())
print(texto.find('e')) # Permite buscar en que posicion de la cadena se encuentra el caracter o la cadena solicitada, si no existe retorna -1
print(texto.find('h'))
print(texto.replace('Texto','Hola')) # Remplaza la cadena buscada por el valor ingresado
print('Texto' in texto) # Retorna un bool si lo encuentra, la diferencia con find, es que te retorna el indice, y la funcion in retorna bool, TLDR; in para saber si un caracter o una cadena se encuentra dentro de un string y find para sacar el indice
print('Texto' not in texto)
