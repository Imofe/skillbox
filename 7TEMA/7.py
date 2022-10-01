number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
count = 0
summ = 0
for i in range(number1, number2+1):
    if i % 3 == 0:
        count += 1
        summ += i

print(f'Среднее арифметическое: {summ/count}')
