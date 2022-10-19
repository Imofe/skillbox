text = input('Введите текст: ')
first_h = text.index('h')
last_h = text.rindex('h')
print(text[last_h-1:first_h:-1]) 