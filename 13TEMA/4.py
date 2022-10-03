def find_mantissa(string):
    print(f'Мантисса равна {(string[:string.find("e"):])}, порядок числа {(string[string.find("e") + 1:])}')

line = input('Введите строку в экспоненциальной форме числа: ')
find_mantissa(line)