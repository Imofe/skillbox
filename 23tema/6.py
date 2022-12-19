name = input('Как вас зовут? ')
with open('chat.txt', 'w') as chat:
    chat.close()

while True:
    print('1 - увидеть текущий текст чата\n2 - написать сообщение')
    answer = input('Введите 1 или 2: ')
    if answer == '1':
        try:
            with open('23tema/chat.txt', 'r') as chat:
                print(''.join(chat.readlines()))
        except FileNotFoundError:
            print('Чат пуст\n')
    elif answer == '2':
        new_message = input('Введите сообщение: ')
        with open('23tema/chat.txt', 'a') as chat:
            chat.write(f'{name}: {new_message}\n')
    else:
        print('Неизвестная команда\n')