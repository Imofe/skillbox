people = int(input('Количество человек: '))
count = int(input('Како число в считалке? '))
print(f'Значит, выбывает каждый {count}-й человек\n')

array = [i for i in range(1, people + 1)]
start = 0
while len(array) > 1:
    print(f'Текущий круг людей: {array}')
    print(f'Начало счета с номера {array[start]}')
    delete = (start + count - 1) % len(array)
    if array[delete] == array[-1]:
        start = 0
    else:
        start = delete
    print(f'Выбывает человек под номером {array.pop(delete)}\n')

print(f'Остался человек под номером {array[0]}')