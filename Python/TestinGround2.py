import os
import time

hour = 9
minute = 58
second = 57

while hour <= 23:
    while minute <= 59:
        while second <= 59:
            os.system("cls")
            hprint = f'0{hour}:' if hour < 10 else f'{hour}:'
            mprint = f'0{minute}:' if minute < 10 else f'{minute}:'
            sprint = f'0{second}' if second < 10 else f'{second}'
            print(hprint+mprint+sprint)
            time.sleep(1)
            second += 1
        minute += 1
        second = 0
    minute = 0
    hour += 1
    hour = 0 if hour == 24 else hour
