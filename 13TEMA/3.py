def reverse(n):
    rev_num = n[::-1]
    return rev_num


number_1 = input("Введите первое число: ")
number_2 = input("Введите второе число: ")
number_summ = int(reverse(number_1)) + int(reverse(number_2))
print(f'\nПервое число наоборот: {reverse(number_1)}')
print(f'Второе число наоборот: {reverse(number_2)}')
print(f'\nСумма {number_summ}')
print(f'Сумма наоборот: {reverse(str(number_summ))}')