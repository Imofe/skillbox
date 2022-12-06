line = input('Введите строку: ')

str_len = len(line)
result = ''
i_letter = 0

while i_letter < str_len:
    counter = 0
    current_char = line[i_letter]
    while i_letter < str_len and line[i_letter] == current_char:
        i_letter += 1
        counter += 1
    result = ''.join([result, ''.join([current_char, str(counter)])])

print(f'Закодированная строка: {result}')