from threading import current_thread


current_detail = input('Введите название детали: ')
amount = int(input('Введите количество деталей: '))
shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
summ = 0
count = 0

for detail in shop:
    if count >= amount:
        break
    if detail[0] == current_detail:
        summ += detail[1]
        count += 1

print(f'Общая стоимость - {summ}')
