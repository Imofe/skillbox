number = int(input('Введите число: '))

if (number >= 10 and number < 100) or (number <= -10 and number > -100):
    print('Число двухзначное')
else:
    print('Вы не прошли проверку на дурака. Число НЕ двухзначное')