line = input('Введите строку: ')

print('Результат: ', ' '.join(word.capitalize() for word in line.split()))