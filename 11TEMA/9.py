import math


a = float(input('Введите коэффициент а (а != 0): '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))

if a != 0:
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print(f'Уравнение имеет два корня: \nx1 = {x1}\nx2 = {x2}')
    elif discr == 0:
        x = -b / (2 * a)
        print(f'Уравнение имеет один корень: x = {x}')
    else:
        print("Корней нет")