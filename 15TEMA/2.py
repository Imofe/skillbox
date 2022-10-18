names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']

even = []
for name in range(0, len(names), 2):
    even.append(names[name])

print(f'Первый день: {even}')
