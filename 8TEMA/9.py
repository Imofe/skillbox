x = int(input('Введите число X: '))
number1 = 1
number2 = 1
for i in range(1, 7):
  number1 *= (x - (2 ** i - 1))
  number2 *= (x - 2 ** i) 

if number2 == 0:
  print('Ошибка. На ноль делить нельзя.')
else:
  print('Результат:', number1 / number2)