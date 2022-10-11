import math

print('Введите координаты монетки')
x = float(input('X: '))
y = float(input('Y: '))
rad = float(input('Введите радиус: '))

if math.sqrt(x * x + y * y) > rad:
    print('Монетки в области нет')
else:
    print('Монетка где-то рядом')