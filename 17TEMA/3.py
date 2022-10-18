import random

first_team = [round(random.uniform(5, 10), 2) for i in range(20)]
second_team = [round(random.uniform(5, 10), 2) for i in range(20)]
answer = list(map(max, first_team, second_team))

print(f'Первая команда:  {first_team}')
print(f'Вторая команда:  {second_team}')
print(f'Победители тура: {answer}')