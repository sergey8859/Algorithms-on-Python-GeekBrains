# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

num_list = [random.randint(0, 100) for _ in range(10)]
print(*num_list)
min_el = num_list[0]
max_el = num_list[1]

for i, item in enumerate(num_list):
    if item <= min_el:
        min_el = item
        min_idx = i
    if item >= max_el:
        max_el = item
        max_idx = i

num_list[min_idx] = max_el         # Присваивание нового значения для элемента
num_list[max_idx] = min_el         # списка быстро происходит или как с insert?

print('Переставим максимальный и минимальный элементы:\n', *num_list)
