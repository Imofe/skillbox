line_num = 0
count = 0

try:
    with open('23tema/people.txt', 'r', encoding='utf8') as data_file:
        for line in data_file:
            line_num += 1
            length = len(line)
            if line.endswith('\n'):
                length -= 1
            try:
                count += length
                if length < 3:
                    raise Exception(f'Ошибка: менее трёх символов в строке номер {line_num}.')
            except Exception as exception:
                print(exception)
except Exception as exception:
    print(exception)
else:
    print('Всего символов:', count)