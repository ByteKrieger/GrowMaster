pi = 3.1415
while True:
    try:
        wahl = int(input('Willst du Zylinder:1 oder Kreis:2 ? : '))
        break
    except ValueError:
        print('wiederhole deine Eingabe')
        continue
while True:   
    try:  
        if wahl == 1:
            r = float(input('Gib den Radius ein : '))
            h = float(input('Gib die Höhe ein   : '))

            rechnung = r * r * pi * h

            v = round(rechnung, 2)
            l = round(rechnung / 1000)
            print(f' Das Volumen beträgt {v}cm^3 deine benötigte Erdemenge beträgt somit ca {l} Liter.')
            if l < 25.0:
                print('du brauchst weniger als 25l Erde!')
            else:
                print(f'Du brauchst ca {l}l Erde.')

            break
        if wahl == 2:
            a = float(input('Gib Seite A an  : '))
            b = float(input('Gib Seite B an  : '))
            c = float(input('Gib die Höhe an : '))

            rechnung = a * b * c
            v = round(rechnung, 2)
            l = round(rechnung / 1000)
            print(f' Das Volumen beträgt {v}cm^3 deine benötigte Erdemenge beträgt somit ca {l} Liter.')

            break

    except ValueError:
        print('Fehlerhafte Eingabe !')


