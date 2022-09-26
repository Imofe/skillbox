firstNumber = int(input('Введите первое число: ')) 
secondNumber = int(input('Введите второе число: ')) 

if (firstNumber >= secondNumber):
    print(f'Разность: {firstNumber - secondNumber}')
    print('Костя платит')
else: 
    print(f'Сумма: {firstNumber + secondNumber}')
    print('Владелец платит')

print('Игра окончена')