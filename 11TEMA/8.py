angle = float(input("Укажите угол часовой стрелки: ")) 
angle_minute = (angle % 30 * 12)
print(f'Угол поворота минутной стрелки = {angle_minute} градусов.')
