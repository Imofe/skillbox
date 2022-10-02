text = input('Введите текст: ')
count = 0
max_count = 0

for char in text:
  if char != ' ':
    count += 1
  else:
    count = 0
  if max_count < count:
    max_count = count
    
print(f'Самое длинное слово, букв: {max_count}')