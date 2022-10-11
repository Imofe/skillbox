danger_level = float(input('Введите максимально допустимый уровень опасности: '))

depth_up = 0
depth_down = 4

depth = depth_up + (depth_down - depth_up) / 2
danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10

if danger_level < 0:
    print('Ошибка: максимально допустимый уровень опасности - абсолютная величина и должна быть больше нуля.')
else:
    while abs(danger) > danger_level:
        if danger > 0:
            depth_up = depth
        else:
            depth_down = depth
        depth = depth_up + (depth_down - depth_up) / 2
        danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10

print(f'Приблизительная глубина безопасной кладки: {depth} м.')