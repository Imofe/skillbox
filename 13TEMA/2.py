def max_number(x, y):
    max_n = ((x + y) + abs(x - y)) / 2
    return max_n


number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))

print(f'Наибольшее число: {max_number(max_number(number_1, number_2), number_3)}')