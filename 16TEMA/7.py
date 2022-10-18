rollers_size = []
foot_size = []
count = 0

r_num = int(input('Количество коньков: '))
for i in range(1, r_num + 1):
    rollers_size.append(int(input(f'Размер {i} пары: ')))

p_num = int(input('\nКоличество людей: '))
for i in range(1, p_num + 1):
    foot_size.append(int(input(f'Размер ноги {i} человека: ')))

rollers_size.sort()
foot_size.sort()

for i in foot_size:
    for j in range(len(rollers_size)):
        if rollers_size[j] >= i:
            rollers_size.remove(rollers_size[j])
            count += 1
            break

print(f'\nНаибольшее кол-во людей, которые могут взять ролики: {count}')





