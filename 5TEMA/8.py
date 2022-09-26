price = int(input('Введите стоимость квартиры: '))
area = int(input('Введите площадь квартиры: '))

if (price <= 10000000 and area >= 100) or (price <= 7000000 and area >= 80):
    print('Квартира подходит.')

else:
    print('Квартира не подходит.')