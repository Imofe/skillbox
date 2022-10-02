string = input('Введите строку: ')
count = 0
count_max = 0

for i in string:
  if i == 's':
    count += 1
  else:
    count = 0
  if count_max < count:
    count_max = count
print(f'Самая длинная последовательность: {count_max}')