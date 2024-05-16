from collections import Counter
import re

def verificarRepeticion(num):
    digits = re.findall(r'\d',num)

    contador = Counter(digits)

    for count in contador.values():
        if count >= 4:
            return True
    return False
num = '90043359'
print(verificarRepeticion(num))