def scan():
    x = float(input('Введите координату Х: '))
    y = float(input('Введите координату Y: '))
  
    if -1 <= x <= 1 and -1 <= y <= 1:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')

scan()