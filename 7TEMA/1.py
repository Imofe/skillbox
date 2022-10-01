arr = [114, 12, 14, 10605, 4907, 450]

for i in arr:
    if i % 2 == 0 and i % 3 != 0:
        print(f'Число {i} подходит.')
    else:
        print(f'Число {i} не подходит.')