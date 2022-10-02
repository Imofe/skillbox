total_sum = int(input('Введите общую длину колонтитула: '))
sum = int(input('Введите количество восклицательных знаков: '))
print(('~' * (total_sum // 2)) + ('!' * sum) + ('~' * (total_sum // 2)))