mileage = int(input('Введите пробег (трехзначное число): '))
date = int(input('Введите сегодняшнее число: '))

summ = 0;

mileage_temp = mileage
while (mileage_temp > 0):
    summ += mileage_temp % 10
    mileage_temp /= 10

if summ > date:
    mileage = 0
    print('Сброс.')
    print(f'Пробег: {mileage}')
else:
    print('Сегодня не сломался.')
    print(mileage)
