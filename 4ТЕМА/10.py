firstNumber = int(input('Введите первое число: '))
secondNumber = int(input('Введите второе число: '))
thirdNumber = int(input('Введите третье число: '))
temp = firstNumber 

if secondNumber > temp:
    temp = secondNumber
if thirdNumber > temp:
    temp = thirdNumber
print(temp)