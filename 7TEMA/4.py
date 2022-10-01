count = 0
for i in range(30,36):
    number = int(input(f'Введите количество людей в {i} секторе: '))

    if number > 10:
        count += 1
        print(f'Зафиксированно нарушение в {i} секторе')
    else: 
        print(f'В {i} секторе все спокойно.')

print(f'Всего нарушений - {count}')