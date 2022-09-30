ticket = int(input('Введите номер билета: '))
firstNumber = 0
secondNumber = 0
count = 0
while ticket > 0:
    last = ticket % 10
    count += 1
    ticket = ticket // 10
    if count <= 3:
      firstNumber += last
    else:
      secondNumber += last
if firstNumber == secondNumber:
  print('Вам выпал счастливый билет!')
else:
  print('Увы, билет обычный.')