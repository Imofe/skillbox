import string


name = input('Введите имя должника: ')
duty = int(input('Введите сумму долга: '))

while duty > 0:
    summ = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
    duty -= summ
    if duty > 0:
        print(f'Маловато, {name}. Давайте ещё раз.')
        continue
    if duty <= 0:
        print(f'Отлично, {name}! Вы погасили долг. Спасибо!')
        break

