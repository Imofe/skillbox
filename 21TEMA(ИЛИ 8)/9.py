def shift_disc(n, x=1, y=3):
    if n == 1:
        print(f'Переложит диск {n} со стержня номер {x} на стержень номер {y}')
    else:
        shift_disc(n - 1, x, 6 - x - y)
        print(f'Переложит диск {n} со стержня номер {x} на стержень номер {y}')
        shift_disc(n - 1, 6 - x - y, y)


disc_number = int(input('Введите количество дисков: '))
shift_disc(disc_number)
