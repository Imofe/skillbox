number = int(input('введите число: '))

for i in range(1, number + 1):
    for j in range(1, number + 1):
        if i == j:
            print(i, end = ' ')
        elif i > j:
            print(i, end = ' ')
    print()