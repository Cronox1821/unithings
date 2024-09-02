""""
 Autor: Fabian Gabriel Maulen Maulen
 19-07-2024
 Seccion 001

"""
import random
import csv
import math

try:
    from tabulate import tabulate
except ModuleNotFoundError:
    input('No tiene instalado el modulo tabulate, Para continuar, debera instalarlo utilizando pip install tabulate\n')
    exit()

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

def asignar_sueldos_aleatorios():
   sueldos = [random.randint(300000, 2500000) for _ in trabajadores]
   return sueldos

def clasificar_sueldos(sueldos):
   clasificacion = {'menores_800k': [], 'entre_800k_2m': [], 'mayores_2m': []}
   for nombre, sueldo in zip(trabajadores, sueldos):
      match sueldo:
         case s if s < 800000:
            clasificacion['menores_800k'].append((nombre, sueldo))
         case s if 800000 <= s <= 2000000:
            clasificacion['entre_800k_2m'].append((nombre, sueldo))
         case s if s > 2000000:
            clasificacion['mayores_2m'].append((nombre, sueldo))
   return clasificacion

def ver_estadisticas(sueldos):
   max_sueldo = max(sueldos)
   min_sueldo = min(sueldos)
   promedio = sum(sueldos) / len(sueldos)
   media_geom = round((math.prod(sueldos))**(1/len(sueldos)))
   return max_sueldo, min_sueldo, promedio, media_geom

def reporte_sueldos(sueldos):
  reporte = []
  for nombre, sueldo in zip(trabajadores, sueldos):
      descuento_salud = sueldo * 0.07
      descuento_afp = sueldo * 0.12
      sueldo_liquido = sueldo - descuento_salud - descuento_afp
      reporte.append([nombre, sueldo, descuento_salud, descuento_afp, sueldo_liquido])
  return reporte

def exportar_a_csv(reporte):
   with open('reporte_sueldos.csv', mode='w', newline='', encoding='utf-8') as file:
      writer = csv.writer(file)
      writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
      writer.writerows(reporte)

def menu():
   while True:
      try:
         print("\nMenú de opciones:")
         print("[1] Asignar sueldos aleatorios")
         print("[2] Clasificar sueldos")
         print("[3] Ver estadísticas")
         print("[4] Reporte de sueldos")
         print("[5] Salir del programa")
         opc = int(input())
         return opc
      except ValueError:
         print('Valor esperado: Entero\nValor ingresado: Caracter\nIntente nuevamente\n')


def main():
   sueldos = []
   while (opcion := int(menu())) != 5 :
         match opcion:
            case 1:
               sueldos = asignar_sueldos_aleatorios()
               print("Sueldos asignados exitosamente.")

            case 2:
               if sueldos:
                  clasificacion = clasificar_sueldos(sueldos)
                  print("\nSueldos menores a $800.000")
                  print(tabulate(clasificacion['menores_800k'], headers=["Nombre", "Sueldo"], tablefmt="grid",floatfmt="0.f"))
                        
                  print("\nSueldos entre $800.000 y $2.000.000")
                  print(tabulate(clasificacion['entre_800k_2m'], headers=["Nombre", "Sueldo"], tablefmt="grid",floatfmt="0.f"))
                        
                  print("\nSueldos superiores a $2.000.000")
                  print(tabulate(clasificacion['mayores_2m'], headers=["Nombre", "Sueldo"], tablefmt="grid",floatfmt="0.f"))
               else:
                  print("No hay sueldos")
            case 3:
               if sueldos:
                  max_sueldo, min_sueldo, promedio, media_geom = ver_estadisticas(sueldos)
                  print(f"Sueldo más alto: ${max_sueldo}")
                  print(f"Sueldo más bajo: ${min_sueldo}")
                  print(f"Promedio de sueldos: ${promedio}")
                  print(f"Media geométrica de sueldos: ${media_geom}")
               else:
                  print("Primero debe asignar los sueldos (opción 1).")

            case 4:
               if sueldos:
                  reporte = reporte_sueldos(sueldos)
                  print("\nReporte de sueldos:")
                  print(tabulate(reporte, headers=["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"], tablefmt="grid"))
                  exportar_a_csv(reporte)
                  print("Reporte exportado a reporte_sueldos.csv")
               else:
                  print("Primero debe asignar los sueldos (opción 1).")

            case _:
               print("Opcion invalida. Intente nuevamente")

   print("Finalizando programa...")
   print("Desarrollado por Fabian Maulen")
   print("RUT 21.342.798-9")

if __name__ == "__main__":
   main()
