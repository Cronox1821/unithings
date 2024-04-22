edad = 15

if edad > 17:
    print("Es mayor")
else:
    print("Es menor")

# Lo podemos convertir progresivamente a lo siguiente

edad = 15

if edad > 17:
    mensaje = "Es mayor"
else:
    mensaje = "Es menor"

print(mensaje)

# Y eventualmente con el operador ternario nos permite hacer lo siguiente:

mensaje = "Es mayor" if edad > 17 else "Es menor"

print(mensaje)
