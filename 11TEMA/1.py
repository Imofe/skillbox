import math

euro = int(input('Введите стоимость в евро: '))

dol = euro * 1.25
rub = dol * 60.87

print('Покупка в рублях будет стоить:', round(rub, 2))