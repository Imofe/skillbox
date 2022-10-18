step = int(input('Сдвиг: '))
arr = [1, 4, -3, 0, 10]

for i in range(step):
    new_arr = arr[-step:] + arr[:-step]

print(f'Изначальный список: {arr}')
print(f'Сдвинутый список: {new_arr}')


