number = int(input('Введите число: '))

symbol = 0
if number == 0:
    symbol += 1
while number > 0:
    symbol += 1
    number //= 10
print(symbol)