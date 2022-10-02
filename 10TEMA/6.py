number = int(input('Введите число: '))
factorial = 1
summ = 0

for i in range(1, number + 1):
    factorial *= i
    summ += factorial
  
print('\nСумма факториалов равна:', summ)