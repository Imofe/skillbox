from operator import ne


positive = 0
negative = 0

while True:
    number = int(input('Введите число: '))

    if number > 0:
        positive += 1
        continue
    if number < 0:
        negative += 1
        continue
    else:
        break

print(f'Количество положительных отзывов: {positive}')
print(f'Количество отрицательных отзывов: {negative}')
