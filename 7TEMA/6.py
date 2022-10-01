n = int(input('Введите кол-во учеников в классе: '))
fives = 0
fours = 0
three = 0
for i in range(1, n+1):
    rating = int(input('Введите оценку (3, 4 или 5): '))

    if rating == 5:
        fives += 1
    if rating == 4:
        fours += 1
    if rating == 3:
        three += 1

if (fives > fours and fives > three):
    print(f'Отличников сегодня больше. Их сегодня - {fives}')
if (fours > fives and fours > three):
    print(f'Хорошистов сегодня больше. Их сегодня - {fours}')
if (three > fours and three > fives):
    print(f'Троечников сегодня больше. Их сегодня - {three}')

 
