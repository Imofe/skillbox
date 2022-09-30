deposit = int(input('Введите значение X: '))
percent = int(input('Введите значение P: '))
summ = int(input('Введите значение Y: '))
years = 0
while summ > deposit:
  deposit += percent * (deposit / 100)
  years += 1
print(f'{years} лет нужно, чтобы накопить нужную сумму')