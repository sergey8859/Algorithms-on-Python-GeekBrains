# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
import random

num_list = [random.randint(-10, 10) for _ in range(10)]
min_el = -float('inf')

for i, item in enumerate(num_list):
    if min_el < item < 0:
        min_el = item
        min_idx = i

print(f'В массиве: \n{num_list} \nминимальный отрицательный элемент = {min_el} \nего индекс = {min_idx}')
