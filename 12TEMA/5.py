def count_letters (text = input('Введите текст: ')):
    text = text.lower()
    number = int(input('Какую цифру ищем? '))
    letter = input('Какую букву ищем? ')

    num_count = 0
    let_count = 0
    for char in text:
        if str(number) == char:
            num_count += 1
        if letter == char:
            let_count += 1
        
    print(f'Количество цифр {number}: {num_count}')
    print(f'Количество букв {letter}: {let_count}')

count_letters()
    


