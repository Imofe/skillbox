right_word = 'карамба'
count = 0
for i in range(10):
    word = input('Введите слово: ').lower()
    if word == right_word:
        count += 1
    
print(count)
