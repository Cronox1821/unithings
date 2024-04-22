while True:
    try:
        taradito = input('Dale taradito, ingresa un numero: ')
        taradito = int(taradito)
        break
    except ValueError:
        try:
            taradito = float(taradito)
            break
        except ValueError:
            print('Sos boludito, ingresa algo bien')

taradito = taradito * 0.85

print('Resultado:', taradito)
