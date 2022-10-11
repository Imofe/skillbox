def get_elements_sum(number):
    summ = 0
    while number > 0:
        summ += number % 10
        number //= 10
    return summ


def get_number_length(number):
    length = 0
    while number > 0:
        length += 1
        number //= 10
    return length


number = int(input('Введите число: '))
elements_summ = get_elements_sum(number)
number_length = get_number_length(number)
print(f'Сумма чисел: {elements_summ}')
print(f'Количество цифр в числе: {number_length}')
print(f'Разность суммы и количества цифр: {elements_summ - number_length}')