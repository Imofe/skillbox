threshold = 270
russianLanguage = int(input('Введите количество баллов по русскому языку: '))
mathematics = int(input('Введите количество баллов по математике: '))
informatics = int(input('Введите количество баллов по информатике: '))

if (russianLanguage + mathematics + informatics > 270):
    print('Поздравляю, ты поступил на бюджет!')
else: 
    print('К сожалению, ты не прошёл на бюджет.')