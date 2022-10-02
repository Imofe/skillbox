count = 0
day_of_week = input('Введите день недели: ').lower()
week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

for day in week:
    count += 1
    if day == day_of_week:
        print(f'Номер дня недели: {count}')