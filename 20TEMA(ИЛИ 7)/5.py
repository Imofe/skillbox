full_name = {
    'Сидоров Никита': 35,
    'Сидорова Алина': 34,
    'Сидоров Павел': 10,
    'Лабзин Роман': 19,
    'Лабзина Дарья': 31
}
ending = {'ов': 'ова', 'ев': 'ева', 'ий': 'ая', 'ин': 'ина'}


def last_char(in_str):
    for key, value in ending.items():
        if in_str.endswith(key):
            in_str = in_str[0:-len(key)]
            break
        if in_str.endswith(value):
            in_str = in_str[0:-len(value)]
            break
    return in_str


search = input('Введите фамилию: ').lower()
search_part = last_char(search)
result = []

for surname in full_name:
    if search_part in surname.split()[0].lower():
        result.append(surname + ' ' + str(full_name[surname]))

if not result:
    print('Поиск не дал результатов')
else:
    for surname in result:
        print(surname)
