import random

original_list = [random.randint(0, 9) for _ in range(10)]

print('Оригинальный список:', original_list)

new_list = [*map(tuple, zip(original_list[::2], original_list[1::2]))]
print('Новый список:', new_list)
