def rate_problem(first_op, second_op, operand):
    if second_op == 0:
        raise ZeroDivisionError('Деление на ноль!')
    if operand == '+':
        return first_op + second_op
    if operand == '-':
        return first_op - second_op
    if operand == '*':
        return first_op * second_op
    if operand == '/':
        return first_op / second_op


def rate_every(line):
    global all_summ
    line = line.replace('\n', '')
    data = line.split()
    operand = data[1]
    try:
        if len(operand) != 1:
            raise TypeError
        op_1 = int(data[0])
        op_2 = int(data[2])
        all_summ += rate_problem(op_1, op_2, operand)
    except (TypeError, SyntaxError, ValueError, ZeroDivisionError):
        print(f'Обнаружена ошибка в строке: {line}')
        answer = input('Хотите исправить? ')
        if answer.lower() == 'да':
            rate_every(input('Введите исправленную строку: '))


all_summ = 0

with open('23tema/calc.txt', 'r', encoding='utf-8') as f_calc:
    for line in f_calc:
        rate_every(line)

print(all_summ)