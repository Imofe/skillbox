from operator import length_hint


length = int(input('Введите длину квадрата: '))
print('')

for i in range(length):
    for j in range(length):
        if j == i:
            print('^', end = '')
        elif j == -i + length - 1:
            print('^', end = '')
        else:
            print(' ', end = '')
    
    print('')