n = int(input('Введите кол-во чисел: '))
max_summ = -1
ans_number = 0

for i in range(n):
    number_summ = 0
    number = int(input('Введите число: '))
    temp = number
    while number > 0:
        number_summ += number % 10
        number //= 10

    if number_summ > max_summ:
        max_summ = number_summ
        ans_number = temp
    else:
        number_summ = 0


print(f'Наибольшее число по сумме цифр {ans_number} \nСумма цифр: {max_summ}')


