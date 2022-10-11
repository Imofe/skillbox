threshold = 270
russian_language = int(input('Введите количество баллов по русскому языку: '))
mathematics = int(input('Введите количество баллов по математике: '))
informatics = int(input('Введите количество баллов по информатике: '))

if (russian_language + mathematics + informatics > 270):
    print('Поздравляю, ты поступил на бюджет!')
else: 
    print('К сожалению, ты не прошёл на бюджет.')