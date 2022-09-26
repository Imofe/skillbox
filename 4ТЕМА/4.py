firstPrice = int(input('Введите цену первого товара: '))
secondPrice = int(input('Введите цену второго товара: '))
thirdPrice = int(input('Введите цену третьего товара: '))
summ = firstPrice + secondPrice + thirdPrice

if (summ > 10000):
    summ -= summ * 0.1

print(summ)