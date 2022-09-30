tasks = 0
wifeСalls = 0
hour = 1
print('Начался 8-часовой рабочий день')

while hour <= 8:
  print(f'{hour}-й час')
  task = int(input('Сколько задач решит Максим? '))
  call = int(input('Звонит жена. Взять трубку? (1 - да, 0 - нет): '))
  hour += 1
  tasks += task
  wifeСalls += call

print(f'Рабочий день закончился. Всего выполнено задач: {tasks}')

if wifeСalls > 0:
  print('Нужно зайти в магазин')