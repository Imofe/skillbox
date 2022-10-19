import random

num = input('Кол-во чисел в списке: ')
list = [random.randint(0, 2) for _ in range(int(num))]
print('Список до сжатия:', list)
compressed_list = [x for x in list if x]
print('Список после сжатия: ', compressed_list)