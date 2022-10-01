n = int(input('Введите число карточек: '))
total_summ = 0
for i in range(1, n+1):
    total_summ += i
summ = 0
for i in range(1, n):
    currentCards = int(input('Введите номер текущей карточки: '))
    summ += currentCards

print(f'Потерялась карточка: {total_summ - summ}')
