import math

random_pl = float(input('Введите радиус случайной планеты: '))
volume_earth = 10.8321 * 10**11
v = (4/3) * math.pi * random_pl**3

if volume_earth > v:
    print('Объём планеты Земля больше в', round(volume_earth / v, 3), 'раз')
else:
    print('Объём планеты Земля меньше в (1/' + str(round(volume_earth/v, 3)) + ') =', round(v/volume_earth, 3), 'раз')