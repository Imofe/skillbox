for i in range(1,11):
    number = int(input('Введите число: '))
    if number % 2 == 0 and number > 0:
        print(f'Число {number} подходит')
    else:
        print(f'Число {number} не подходит')