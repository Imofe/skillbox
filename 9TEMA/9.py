stall = input('Введите строку, где: a - свободное стойло, b - занятое: ')
milk = 0
count = 0

for i in stall:
    count += 1
    if i == 'b':
        milk += count * 2

print(f'Кол-во молока за день: {milk}')