rut = []
nombre = []
direccion = []
telefono = []
correo = []
cliente = {
   "clave" : rut,
   "nombre" : nombre,
   "direccion" : direccion,
   "telefono" : telefono,
   "correo": correo,
   "preferente" : True
} 

def menu():
   print("(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\t(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar")

select = 0

match (select):
  case 1:
      pass
   case _:
      pass
