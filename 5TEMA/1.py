exp = int(input('Введите количество очков: '))
level = 0

if 0 <= exp < 1000:
    level = 1
    print(f'Ваш уровень: {level}')
elif 1000 <= exp < 2500:
    level = 2
    print(f'Ваш уровень: {level}')
elif 2500 <= exp < 5000:
    level = 3
    print(f'Ваш уровень: {level}')
else: 
    level = 4
    print(f'Ваш уровень: {level}')


    
