word = str(input('Введите слово: '))
length = len(word)
i = 0
length = length - 1
flag = False
while length - i >= i:
    if word[length - i] == word[i]:
        i += 1
    else:
        flag = True
        break

if flag:
    print('Слово не является палиндромом')
else:
    print('Слово является палиндромом')