x = 8
y = 10

while True:
  print('[Программа]: Марсоход находится на позиции', x, ',', y, '\nвведите команду: ')
  command_user = input('[Оператор]: ')
  if command_user == 'W' and y != 20:
    y += 1
  elif command_user == 'S' and y != 0:
    y -= 1
  elif command_user == 'A' and x != 0:
    x-= 1
  elif command_user == 'D' and x != 15:
    x += 1
  else:
    print('Неверная команда\n')