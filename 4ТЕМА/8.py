hours = int(input('Введите количество отработанных часов: '))
balance = int(input('Введите остаток по кредиту: '))
foodMoney = int(input('Введите количество денег на еду: '))

salary = ((200 * hours) / 2**3) + hours

if (salary >= balance + foodMoney):
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся работать!')

