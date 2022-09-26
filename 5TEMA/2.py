firstNumber = int(input('Введите первое число: '))
secondNumber = int(input('Введите второе число: '))
thirdNumber = int(input('Введите третье число: '))

if (firstNumber > secondNumber and firstNumber > thirdNumber):
    print(firstNumber)
elif (secondNumber > firstNumber and secondNumber > thirdNumber):
    print(secondNumber)
else:
    print(thirdNumber)

    