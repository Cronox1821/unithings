while True:
    try:
        shows = int(input('Cuantos shows musicales ha visto en el ultimo año: '))
        break
    except ValueError:
        print('Error\n')

Flag = True if shows > 3 else False

if Flag:
    print(Flag)
    print('Ha visto mas de 3 shows')
else:
    print(Flag)
    print('No ha visto mas de 3 shows')
