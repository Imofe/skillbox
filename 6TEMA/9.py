number = int(input('Загадайте число: '))

count = 0

while True:
    currentNumber = int(input('Введите число: '))
    count += 1
    if currentNumber == number:
        print(f'Вы угадали. Число попыток: {count}')
        break
    if currentNumber < number:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
        continue
    if currentNumber > number:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
        continue