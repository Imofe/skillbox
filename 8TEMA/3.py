reverse_timer = int(input('Укажите кол-во секунд подогрева: '))
for i in range(reverse_timer, 0, - 1):
  print(f'{i} секунд')
  stop = int(input('Хотите прервать режим подогрева? 1 - Да, 0 - Нет: '))
  if stop == 1:
    print(f'Ваша еда готова, можете забрать, осталось: {i} сек.')
    break
print('Ваша еда готова, осторожно горячo!')