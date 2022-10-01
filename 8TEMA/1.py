summ_months = 0

for i in range(100 - 4, -1, -4):
  summ_months += 1
  print(f'{summ_months}-й месяц')
  print(f'Осталось {i} кг гречи')

print('Греча кончилась!')