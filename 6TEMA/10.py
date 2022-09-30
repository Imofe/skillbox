min = 1
max = 100

while True:
    number = (min + max) // 2
    print(f'Твое число равно, меньше или больше, чем число {number}?')
    answer = int(input('Введите вариант ответа: 1 — равно, 2 — больше, 3 — меньше: '))
    if answer == 1:
        print('Я yгадал!')
        break
    elif answer == 2:
        min = number + 1
    else:
        answer = 3
        max = number - 1