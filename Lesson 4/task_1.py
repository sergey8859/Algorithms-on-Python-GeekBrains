# Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.
#
# Задание 5 урок 3
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.



def my_func(num_list):
    min_el = float('-inf')
    for i, item in enumerate(num_list):
        if min_el < item < 0:
            min_el = item
            min_idx = i


# python -m timeit -n 100 -s "import random" "x = [random.randint(-100, 0) for _ in range(10)]" "import task_1" "task_1.my_func(x)"

# 100 loops, best of 5: 72.4 usec per loop      random.randint(-10, 0) for _ in range(10)
# 100 loops, best of 5: 682 usec per loop       100
# 100 loops, best of 5: 76.4 usec per loop      random.randint(-100, 0) for _ in range(10)
# 100 loops, best of 5: 764 usec per loop       100
# 100 loops, best of 5: 7.86 msec per loop      1000
# 100 loops, best of 5: 67.8 msec per loop      10000
# 100 loops, best of 5: 673 msec per loop       100000



def func_2(num_list):
    new_list = [i for i in num_list if i < 0]
    maximum = max(new_list)
    idx = new_list.index(maximum)

# 100 loops, best of 5: 66.9 usec per loop      random.randint(-10, 10) for _ in range(10)
# 100 loops, best of 5: 612 usec per loop       100
# 100 loops, best of 5: 76.9 usec per loop      random.randint(-100, 100) for _ in range(10)
# 100 loops, best of 5: 632 usec per loop       100
# 100 loops, best of 5: 6.16 msec per loop      1000
# 100 loops, best of 5: 64.4 msec per loop      10000
# 100 loops, best of 5: 411 msec per loop       100000


"""
Я все надеялся, что с ростом количества переменных первый вариант окажется лучше, но, на удивление, нет 
"""

# Задание 9 урок 3
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

def matrix_func(matrix):
    for i, line in enumerate(matrix):

        if i == 0:
            min_line = line.copy()
            continue

        for idx, item in enumerate(line):
            if item < min_line[idx]:
                min_line[idx] = item

    max_min = min_line[0]
    for item in min_line:
        if item > max_min:
            max_min = item

# python -m timeit -n 100 -s "import random" "x = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]" "import task_1" "task_1.matrix_func(x)"

# 100 loops, best of 5: 73.6 usec per loop          3 X 3
# 100 loops, best of 5: 177 usec per loop           5 X 5
# 100 loops, best of 5: 375 usec per loop           5 X 10
# 100 loops, best of 5: 338 usec per loop           10 X 5
# 100 loops, best of 5: 657 usec per loop           10 X 10


def matrix_func2(matrix):

    max_ = float('-inf')

    for j in range(len(matrix[0])):
        min_ = matrix[0][j]

        for i in range(len(matrix)):
            if matrix[i][j] < min_:
                min_ = matrix[i][j]

        if min_ > max_:
            max_ = min_

# 100 loops, best of 5: 79.2 usec per loop          3 X 3
# 100 loops, best of 5: 196 usec per loop           5 X 5
# 100 loops, best of 5: 378 usec per loop           5 X 10
# 100 loops, best of 5: 373 usec per loop           10 X 5
# 100 loops, best of 5: 687 usec per loop           10 X 10
