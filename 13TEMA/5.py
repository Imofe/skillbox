def num_count(f_num, s_num):
    f_num_count = len(str(f_num))
    s_num_count = len(str(s_num))
    if (f_num_count != 3) or (s_num_count != 4):
        print('\nОшибка! В первом числе должно быть не меньше трёх цифр,\nво втором числе — не меньше четырёх.')
        return 'Ошибка!', ' Ошибка!'
    else:
        f_num = coup(first_n, f_num_count)
        s_num = coup(second_n, s_num_count)
    return f_num, s_num


def coup(temp, len):
    last_digit = temp % 10
    first_digit = temp // 10 ** (len - 1)
    between_digits = temp % 10 ** (len - 1) // 10
    number = last_digit * 10 ** (len - 1) + between_digits * 10 + first_digit
    return number


first_n = int(input("Введите первое число: "))
second_n = int(input("Введите второе число: "))

first_n, second_n = num_count(first_n, second_n)

print(f'Изменённое первое число: {first_n}')
print(f'Изменённое второе число: {second_n}')
print(f'Сумма чисел: {first_n + second_n}')