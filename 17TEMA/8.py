line = list('|' * int(input('Количество палок: ')))

for num in range(1, int(input('Количество бросков: ')) + 1):
    for j in range(int(input(f'Бросок {num}. Сбиты палки с номера ')) - 1, int(input('по номер '))):
        line[j] = '.'

print('Результат:', ''.join(line))
