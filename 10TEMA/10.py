number = int(input('Введите число: '))
print()

for i in range(1, number + 1):
    for j in range(i):
        print(number - j, end = '')
    print('.' * ((number - i) * 2), end = '')
    for j in range(i, 0, -1):
        print(number - j + 1, end = '')
    print()