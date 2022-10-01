n = int(input('Введите число: '))
summ = 0
for number in range(n + 1):
    summ += ((-1) ** number) * (1 / (2 ** number))
print(f'При n = {n} сумма ряда равна: {summ}')