n = int(input('Введите число: '))
answer = 1

for i in range(1, n+1):
    answer *= i

print(f'Факториал числа {n} равен {answer}')
