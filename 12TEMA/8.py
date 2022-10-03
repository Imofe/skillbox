import math

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))

def nod(number1, number2):
    print(f'Наибольший общий делитель двух чисел = {math.gcd(number_1, number_2)}')
  
nod(number_1, number_2)