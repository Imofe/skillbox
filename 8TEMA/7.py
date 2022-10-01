educational_grant = int(input('Введите размер стипендии: '))
expenses = int(input('Введите расходы на проживание: '))

sum_expenses = expenses
budget = educational_grant

for month in range(9):
    expenses += 3 * (expenses // 100)
    sum_expenses += expenses
    budget += educational_grant
print(f'Нужно попросить у родителей минимум {sum_expenses - budget} рублей')