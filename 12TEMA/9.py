def rock_paper_scissors():
    import random
    while True :
        answer = ['камень', 'ножницы', 'бумага']
        x = random.choice(answer)
        request = str(input('камень жми - 1, бумага - 2, ножницы - 3 : '))
        print('У меня ', x)
        if request == 1 and x == 'ножницы' :
            print('Ты выиграл!!')
        elif request == 2 and x == 'камень':
            print('Ты выиграл!!')
        elif request == 3 and x == 'бумага':
            print('Ты выиграл!!')
        else :
            print('Ты проиграл !')
        exit = int(input('Хочешь продолжить жми - 1, хочешь выйти жми - 2 : '))
        if exit == 2 :
            print('Игра окончена.')
            break
    
def guess_the_number():
    import random
    x = random.randrange(1, 10)
    number = int(input('Угадай число от 1 до 10 : '))
  
    while True :
        if x == number :
            print('Ты выиграл')
            break
        else :
            number = int(input('Не угадал попробуй еще раз : ')) 

def mainMenu():
    while True :
        game = int(input('Если хотите сыграть в "Камень, ножницы, бумага" жми - 1\nЕсли в "Угадай число" жми - 2 : '))
        if game == 1 :
            rock_paper_scissors()
        elif game == 2 :
            guess_the_number()
        else :
            print('Не верный выбор !')

mainMenu()