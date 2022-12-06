def fib(position):
    if position == 1 or position == 2:
        return 1
    else:
        return fib(position - 1) + fib(position - 2)


number = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число:', fib(number))
