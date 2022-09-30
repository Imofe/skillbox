months = 0

while True:
    days = int(input('Введите колличество дней: '))
    if days == 0:
        break
    
    if days % 2 == 0:
        months += 1 
print(f'Количество месяцев с четными днями: {months}')