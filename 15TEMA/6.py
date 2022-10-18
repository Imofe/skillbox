word = input('Введите слово: ').lower()
print('Кол-во уникальных букв:', len([i for i in set(word) if word.count(i) == 1]))