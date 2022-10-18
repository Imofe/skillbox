vcard_num = int(input('Количество видеокарт: '))
vcard_list = []
result = []

for i in range(vcard_num):
    print(i + 1, 'Видеокарта: ', end = ' ')
    video_card = int(input())
    vcard_list.append(video_card)

max_element = max(vcard_list)
for i in range(len(vcard_list)):
    if vcard_list[i] == max_element:
        continue
    else:
        result.append(vcard_list[i])

print(f'Старый список видеокарт: {vcard_list}')

print(f'Новый спискок видеокарт: {result}')