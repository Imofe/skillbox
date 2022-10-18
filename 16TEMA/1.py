first_list = [1, 5, 3]
second_list = [1, 5, 1, 5]
third_list = [1, 3, 1, 5, 3, 3]

first_list.extend(second_list)
count_5 = first_list.count(5)
print(count_5)

for _ in range(count_5):
    first_list.remove(5)

first_list.extend(third_list)
count_3 = first_list.count(3)
print(count_3)
print(first_list)