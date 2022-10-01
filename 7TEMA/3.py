summ = 0
for i in range(1,13):
    salary = int(input(f'Введите зарплату за {i}-й месяц: '))
    summ += salary

print(f'Средняя зарплата за год: {summ / 12}')
