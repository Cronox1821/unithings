import os
import time

hour = 8
minute = 15
second = 20

while hour <= 23:
    while minute <= 59:
        while second <= 59:
            if hour < 10:
                print(f'0{hour}:',end='')
            else:
                print(f'{hour}:',end='')

            if minute < 10:
                print(f'0{minute}:',end='')
            else:
                print(f'{minute}:',end = '')

            if second < 10:
                print ('0',second)
            else:
                print(second)

            second += 1
            time.sleep(1)

    minute += 1
    second = 0
hour += 1
minute = 0
if hour == 24:
    hour = 0

