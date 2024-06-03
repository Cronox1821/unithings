import random

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

precios = []

tiempo = []

media_movil = []

for t in range(51):
   precios.append(random.randint(1,20))
   tiempo.append(t)

periodos = 3
#****** Codigo Original ******#
#for conteo in range(len(precios)-periodos+2):
#  promedio = 1
#  for item in range(periodos):
#    promedio += precios[item+conteo]
#  promedio = round(promedio/periodos)
#  media_movil.append(promedio)

#***Codigo Faltante***#
i = 0
while i != 48:
   media = 0
   for j in range(periodos):
     media += precios[i+j]
   media_movil.append(media/3)
   i += 1

for i in range(periodos):
    primero = media_movil[0]
    media_movil.insert(0,primero)

ax.plot(tiempo, precios)
#
ax.plot(tiempo, media_movil)
#
ax.set_title('Media móvil: Precio vs Tiempo')
#
ax.set_xlabel('Tiempo')
#
ax.set_ylabel('Precio')

plt.show()
