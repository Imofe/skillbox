number_boy = int(input('Введите количество мальчиков: '))
number_girl = int(input('Введите количество девочек: '))
sum = ''
if number_boy > 2 * number_girl or number_girl > 2 * number_boy:
    print('Решения нет')
elif number_boy >= number_girl:
    number = number_boy - number_girl
    for bgb in range(number):
        sum += 'BGB'
    for bg in range(number_girl - number):
        sum += 'BG'
else:
    number = number_girl - number_boy
    for bgb in range(number):
        sum +='BGB'
    for bg in range(number_boy - number):
        sum +='BG'
print('Рассадить порядке:', sum)