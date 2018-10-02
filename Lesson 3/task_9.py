# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

for i, line in enumerate(matrix):

    if i == 0:                              # Первую строку копируем для сравнения сразу переходим ко второй строке
        min_line = line.copy()
        for item in line:
            print(f'{item:>5}', end='')
        print()
        continue

    for idx, item in enumerate(line):
        if item < min_line[idx]:            # В строках сравниваем каждый элемент с элементом в копии первой строки
            min_line[idx] = item            # меняем по индексу для сохранения порядка
        print(f'{item:>5}', end='')
    print()

print('-' * len(min_line) * 5)

max_min = min_line[0]
for item in min_line:
    print(f'{item:>5}', end='')
    if item > max_min:
        max_min = item

print()
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы = {max_min}')
