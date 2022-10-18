count = int(input('Количество контейнеров: '))
containers = []

for i in range(count):
    container = int(input('Введите вес контейнера: '))
    if container > 200:
        print('Ошибка! Вес контейнера превышает 200')
        continue
    if len(containers) > 0 and container > containers[-1]:
        print('Ошибка! Последовательность должна быть невозрастающей.')
        continue
    containers.append(container)

new_container = int(input('Введите вес нового контейнера: '))
i = 0
while i < len(containers) and containers[i] >= new_container:
    i += 1

print(f'Номер, который получит новый контейнер: {i+1}')
