def summ():
    number = int(input('Введите число: '))
    summ_number = 0
    while number > 0:
        summ_number += number % 10
        number = number // 10
    print(f'Сумма цифр числа равна {summ_number}')

def max_num():
    number = int(input('Введите число: '))
    max_number = number % 10
    while number > 0:
        number = number // 10
        if max_number < number % 10:
            max_number = number % 10
    print(f'Максимальная цифра в числе равна {max_number}')

def min_num():
    number = int(input('Введите число: '))
    min_number = number % 10
    while number > 0:
        number = number // 10
        if number == 0:
            break
        if min_number > number % 10:
            min_number = number % 10
    print(f'Минимальная цифра в числе равна {min_number}')

def calculate():
    act = int(input('Выберите действие (0 - вывести сумму цифр числа, 1 - вывести максимальную цифру числа, 2 - вывести минимальную цифру числа): '))
    if act == 0:
        summ()
        print('\n')
        calculate()
    elif act == 1:
        max_num()
        print('\n')
        calculate()
    else:
        min_num()
        print('\n')
        calculate()

calculate()