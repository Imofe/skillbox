temp = 0
count = 0
for i in range(1,11):
    salary = int(input('Введите зарплату: '))

    if salary > temp: 
        temp = salary
        count += 1
    else:
        print('Числа не упорядочены')
        break
        
if count == 10:
    print('Числа упорядочены')