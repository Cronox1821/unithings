#Autor Fabian Maulen
from os import system
from tabulate import tabulate

def menu():
   return input('[1] Registrar trabajador\n[2] Listar todos los trabajadores\n[3] Imprimir planilla de sueldos\n[4] Salir\n') 

def crear_trabajador():
   while True:
      system('cls')
      try:
         nombre = input('Nombre del trabajador: ')
         apellido = input('Apellido del trabajador: ')
         cargo = input('Cargo del trabajador: ')
         sueldo_bruto = int(input('Sueldo bruto del trabajador: '))
         descuento = sueldo_bruto * 0.07 + sueldo_bruto * 0.12
         trabajador = {
            'Trabajador': nombre +' '+ apellido,
            'Cargo': cargo,
            'Sueldo Bruto':sueldo_bruto,
            'Desc. Salud':sueldo_bruto * 0.07,# 7%
            'Desc. AFP':sueldo_bruto * 0.12,# 12%
            'Liquido a pagar': format((sueldo_bruto - descuento),'f')
         }
         break
      except:
         print('Valor ingresado invalido, intente nuevamente')
   print('Trabajador agregado')
   wait()
   return trabajador

def listar_trabajadores(workers):
   if workers:
      print('Lista trabajadores')
      header = workers[0].keys()
      rows = [x.values() for x in workers] 
      print(tabulate(rows,header,tablefmt=('grid'),floatfmt='.0f'))
   else:
      print('No hay trabajadores registrados')
   wait()

def buscar_por_cargo(workers,role):
   print('Ingrese el cargo a buscar')
   for i,value in enumerate(role, start = 1):
      print(f'[{i}] {value}')

   cargo = int(input()) - 1
   system('cls')
   if 0 <= cargo < len(role):
      selected_role = role[cargo]
      filtered_employees = [employee for employee in workers if employee['Cargo'] == selected_role]

      if filtered_employees:
         header = filtered_employees[0].keys()
         rows = [employee.values() for employee in filtered_employees]
         print(tabulate(rows,header,format('grid'),floatfmt='.0f'))
         with open(f'table{role[cargo]}.txt', 'w') as f:
            f.write(tabulate(rows,header,tablefmt=('grid'),floatfmt='.0f'))
      else: 
         print(f'No hay trabajadores registrados con el cargo: {selected_role}')
   else:
      print('Opcion ingresada invalida')
   wait()

def imprimir_planilla_sueldos(workers,role):
   if workers:
      opcion = int(input('[1] Buscar por cargo\n[2] Mostrar todos\n'))
      system('cls')
      match opcion:
         case 1:
            buscar_por_cargo(workers,role)
         case 2:
            with open('table.txt', 'w') as f:
               header = workers[0].keys()
               rows = [x.values() for x in workers] 
               f.write(tabulate(rows,header,tablefmt=('grid'),floatfmt='.0f'))
            listar_trabajadores(workers) 
         case _:
            print('Opcion invalida')
            wait()
   else:
      print('No hay trabajadores registrados')
      wait()

def wait():
   input('Presione una tecla para continuar')
   system('cls')

def main():
   trabajadores = list()
   cargos = ['CEO','Desarrollador','Analista de datos']
   while True:
      try:
         while (opcion := int(menu())) != 4:
            match opcion:
               case 1:
                  trabajadores.append(crear_trabajador())
               case 2:
                  listar_trabajadores(trabajadores) 
               case 3:
                  imprimir_planilla_sueldos(trabajadores,cargos)
               case _:
                  print('Opcion invalida')
         break
      except Exception as e:
         print(f'Se ha encontrado un error\nCodigo de error: {e}\nContacte con un administrador para mas informacion')
         wait()

if __name__ == '__main__':
   main()
