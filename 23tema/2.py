import random

def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y

def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x

line_num = 0
my_list = []

with open('23tema/coordinates.txt', 'r', encoding='utf-8') as coordinate_file:
    for row in coordinate_file:
        line_num += 1
        num_list = row.split()
        if len(num_list) != 2:
            raise Exception(f'Ошибка: В строке {line_num} не две координаты.')
        try:
            res1 = f(int(num_list[0]), int(num_list[1]))
            print(str(line_num), 'res1 =', res1)
            try:
                res2 = f2(int(num_list[0]), int(num_list[1]))
                print(str(line_num), 'res2 =', res2)
                number = random.randint(0, 100)
                my_list.append(sorted([number, res1, res2]))
            except ZeroDivisionError:
                print(f'В строке {line_num} попытка деления на 0.')
            except Exception:
                print(f'Строка {line_num} содержит неверные данные')
        except ZeroDivisionError:
            print(f'В строке {line_num} попытка деления на 0.')
        except Exception:
            print(f'Строка {line_num} содержит не  данные')
    sorted_data = sorted(my_list)
    with open('23tema/result.txt', 'w', encoding='utf8') as f_save:
        for row in sorted_data:
            f_save.write('\t'.join([str(item) for item in row]) + '\n')