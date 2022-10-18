num_friends = int(input('Кол-во друзей: '))
count = int(input('Кол-во долговых расписок: '))
print()
friends_list = []

for i in range(num_friends):
    friends_list.append(0)

for number in range(count):
    print(f'{number+1}-я расписка: ')
    to_who = int(input('Кому: '))
    from_who = int(input('От кого: '))
    how_much = int(input('Сколько: '))
    friends_list[from_who - 1] += how_much
    friends_list[to_who - 1] -= how_much

print('Баланс друзей: ')
for index in range(len(friends_list)):
    print(f'{index + 1}: {friends_list[index]}')