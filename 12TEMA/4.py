def reverseNumber():
    number = int(input('Введите число: '))
    if number != 0:
        text = ''
        while number > 0:
            last = str(number % 10)
            text += last
            number = number // 10
        reverse_num = int(text)
        print('Число наоборот:', reverse_num)
        reverseNumber()
    else:
        print('Программа завершена!')

reverseNumber()