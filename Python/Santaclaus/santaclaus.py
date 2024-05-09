floor = 0
first = 0
counter = 0
with open('code.txt') as code:
    for char in code.read():
        counter += 1
        if char == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1 and first == 0:
            first = counter 
        print(floor)
    print(first)
