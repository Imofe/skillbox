letter_size = int(input('Введите размер письма: '))
count = 0
while letter_size > 12:
    letter_size /= 2
    count += 1
print(f'Письмо нужно сложить {count} раз')