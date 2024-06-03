from tabulate import tabulate

def add_client(clients):
   nif = input('NIF: ')
   nombre = input('Nombre: ')
   direccion = input('Direccion: ')
   telefono = input('Telefono: ')
   correo = input('Correo: ')
   preferente = input('Preferente (S/N): ').upper() == 'S' 
   client = {
      'Nombre': nombre,
      'Direccion': direccion,
      'Telefono': telefono,
      'Correo': correo,
      'Preferente': 'Si' if preferente else 'No'
   }
   clients[nif] = client
#   clients.update({nif: client}) 

#   clients.update(nif = client)

#   clients.update({
#      nif : {
#         'Nombre': nombre,                              # Se puede hacer lo mismo con estos 
#         'Direccion': direccion,
#         'Telefono': telefono,
#         'Correo': correo,
#         'Preferente': preferente
#      }
#   })

def del_client(clients):
   nif = input('NIF: ')
   if nif in clients:
      del clients[nif]
      print('Cliente eliminado')
   else:
      print('Cliente no encontrado')


def show_client(clients):
   nif = input('NIF a buscar: ')
   if nif in clients:
      print(tabulate(clients[nif].items(),headers=["Campo","Valor"],tablefmt='grid'))
   else:
      print('Client not found')
      #df = pd.DataFrame(clients) 
      #print(df.set_index('NIF'))
      #for key,value in clients[nif].items():
      #   #print(f'key : {key}\nvalue : {value}\nkey.title() : {key.title()}') # key.title capitalize words
      #   print(f'{key.title()}\t{value}\n')


def show_all(clients):
   if clients:
      print('Lista clientes')
      table = [[nif,data['Nombre']] for nif,data in clients.items()]
      print(tabulate(table,headers=['NIF','Nombre'],tablefmt='grid'))
   else:
      print('No clients')

   #for key,value in clients.items():
   #   print(f"{key}\t{value['Nombre']}")


def show_vip(clients):
   vip_clients = {nif: data for nif, data in clients.items() if data['Preferente'] == 'Si'}
   if vip_clients:
      print('Lista clientes preferentes')
      table = [[nif,data['Nombre']] for nif,data in vip_clients.items()]
      print(tabulate(table,headers=['NIF','Nombre'],tablefmt='grid'))
   else:
      print('No VIP clients')

def main():
   clientes = {}
   while True:
      try:
         option = int(input('1) Add client\n2) Del client\n3) Show client by nif\n4) Show all clients\n5) Show VIP Clients\n6) Exit\n'))
         match(option):
            case 1: # Add client
               add_client(clientes)
               print(clientes)
            case 2: # Del client
               del_client(clientes) 
            case 3: # Show client by NIF
               show_client(clientes)
            case 4: # Show all Clients
               show_all(clientes)
            case 5: # Show VIP Clients
               show_vip(clientes)
            case 6: # End
               break
            case _:          
               print('\nInvalid\n')
      except:
         print('Invalid')

if __name__ == '__main__':
   main()
