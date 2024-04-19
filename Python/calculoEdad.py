import os
import datetime
from datetime import date

os.system("cls")

print(datetime.datetime.today())
print(datetime.datetime.now())

today = datetime.datetime.now()
Bday = datetime.datetime.fromisoformat(input('Bday(YYYY-MM-DD): '))

print(Bday)

print(type(Bday))
print(type(today))

age = (Bday - datetime.datetime.now())/365

age = abs(age)

print(type(age))

#print((Bday - datetime.datetime.now())/365)
#print(datetime.datetime.fromisoformat(date))

print(age)

print(age.days)
