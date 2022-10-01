debtors = int(input('Введите кол-во должников: '))
summ_duty = 0
for i in range(0, debtors+1, 5):
    print(f'Должник с номером {i}')
    duty = int(input('Сколько должны? '))
    summ_duty += duty

print(f'Общая сумма долга: {summ_duty}')
