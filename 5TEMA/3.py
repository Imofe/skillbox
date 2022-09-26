from re import X


x = int(input('Введите икс: '))

if x > 0: 
    print(f'Игрек равен: {x - 12}')
elif x == 0:
    print(f'Игрек равен: {5}')
elif x < 0:
    print(f'Игрек равен: {x*x}')


