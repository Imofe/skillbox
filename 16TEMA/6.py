first_list = []
second_list = []

for i in range(1, 4):
    print('Введите', i, 'число для первого списка:', end=' ')
    number = int(input())
    first_list.append(number)

for i in range(1, 8):
    print('Введите', i, 'число для второго списка:', end=' ')
    number = int(input())
    second_list.append(number)

print(f'Первый список: {first_list}')
print(f'Второй список: {first_list}') 

first_list.extend(second_list)
for i in range(len(first_list)):
    for j in first_list:
        if first_list.count(j) > 1:
            first_list.remove(j)

print(f'Новый первый список с уникальными элементами: {first_list}')