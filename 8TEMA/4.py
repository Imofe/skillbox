number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))

summ = 0
count = 0
for i in range(number1, number2):
    if i % number3 == 0:
        count += 1
        summ += i

print(f'Среднее арифметическое: {summ/count}')
