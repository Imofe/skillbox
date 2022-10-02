numbers = int(input('Введите кол-во чисел: '))
count = 0

for i in range(1, numbers + 1):
    flag = True
    number = int(input('Введите число: '))
    for j in range(2, number):
        if number %  j == 0:
            flag = False  
    if flag:
        count += 1
    
print(f'Кол-во простых чисел в последовательности: {count}')