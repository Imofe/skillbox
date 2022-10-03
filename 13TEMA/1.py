def num_float(n):
    count = 0
    if n > 10:
        while n > 10:
            n /= 10
            count += 1
        return n, count
    elif n < 10:
        while n < 1:
            n *= 10
            count += 1
        return n, count


number = float(input('Введите число: '))
while number <= 0:
    print('Введённое число должно быть больше нуля.\n')
    number = float(input('Введите число: '))
else:
    n, count = num_float(number)

print(f'Формат с плавающей точкой: {number} = {round(n, 15)} * 10 ** {count}')
