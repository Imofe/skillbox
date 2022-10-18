cells_num = int(input('Введите кол-во клеток: '))
cells_list = []
result = []

for i in range(cells_num):
    print('Эффективность', i+1, 'клетки', end = ' ')
    effic_cells = int(input())
    cells_list.append(effic_cells)

for i in range(cells_num):
    if cells_list[i] < i:
        result.append(cells_list[i])

print()
print('Неподходящие значения', ' '.join(map(str, result)))
