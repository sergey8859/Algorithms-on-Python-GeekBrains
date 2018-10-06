# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

num_list = [random.randint(1, 100) for _ in range(10)]
min_el = num_list[1]
pre_min = num_list[0]

for num in num_list:
    if num <= min_el:
        pre_min = min_el
        min_el = num
    elif num <= pre_min:  # условие обеспечивает работу программы, если минимальный элемент находится вначале
        pre_min = num

print(f'В массиве: \n{num_list} \nминимальные элементы: {min_el} и {pre_min}')
