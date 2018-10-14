# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
# первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
#
import sys
import random

"""
Хотел реализовать декоратор, который будет возвращать список переменных для функции, но он работает не совсем так,
как я ожидал. Он возвращает только значения объектов. В принципе, и с этим можно анализировать программы, но выходит
сложнее для понимания. Второй вариант, в функции добавлять возврат locals(). Для анализа проще, но приходится
прописывать вручную в каждой функции. Для примера на первой функции выполню оба варианта, а для остальных только второй.
"""


def my_decor(func, args):
    def objects(args):
        func(args)
        return locals()

    return objects(args)


def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                show_size(y, level + 1)

        elif not isinstance(x, str):
            for y in x:
                show_size(y, level + 1)


# Задание 5 урок 3
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.


def my_func(num_list):
    min_el = float('-inf')
    for i, item in enumerate(num_list):
        if min_el < item < 0:
            min_el = item
            min_idx = i
        return locals()


"""
Вариант с декоратором
"""

# type = <class 'dict'>, size = 240, object = {'args': [-14, -13, -17, -8, -14, -1, -3, -8, -11, -10, -6, -11, -15,
#                                                        -20, -3, -14, -1, -6, -15, -1],
#                                              'func': <function my_func at 0x00000235189C8AE8>}
# 	 type = <class 'tuple'>, size = 64, object = ('args', [-14, -13, -17, -8, -14, -1, -3, -8, -11, -10, -6, -11, -15, -20, -3, -14, -1, -6, -15, -1])
# 		 type = <class 'str'>, size = 53, object = args
# 		 type = <class 'list'>, size = 264, object = [-14, -13, -17, -8, -14, -1, -3, -8, -11, -10, -6, -11, -15, -20, -3, -14, -1, -6, -15, -1]
# 			 type = <class 'int'>, size = 28, object = -14
# 			 type = <class 'int'>, size = 28, object = -13
# 			 type = <class 'int'>, size = 28, object = -17
# 			 type = <class 'int'>, size = 28, object = -8
# 			 type = <class 'int'>, size = 28, object = -14
# 			 type = <class 'int'>, size = 28, object = -1
# 			 type = <class 'int'>, size = 28, object = -3
# 			 type = <class 'int'>, size = 28, object = -8
# 			 type = <class 'int'>, size = 28, object = -11
# 			 type = <class 'int'>, size = 28, object = -10
# 			 type = <class 'int'>, size = 28, object = -6
# 			 type = <class 'int'>, size = 28, object = -11
# 			 type = <class 'int'>, size = 28, object = -15
# 			 type = <class 'int'>, size = 28, object = -20
# 			 type = <class 'int'>, size = 28, object = -3
# 			 type = <class 'int'>, size = 28, object = -14
# 			 type = <class 'int'>, size = 28, object = -1
# 			 type = <class 'int'>, size = 28, object = -6
# 			 type = <class 'int'>, size = 28, object = -15
# 			 type = <class 'int'>, size = 28, object = -1
# 	 type = <class 'tuple'>, size = 64, object = ('func', <function my_func at 0x00000235189C8AE8>)
# 		 type = <class 'str'>, size = 53, object = func
# 		 type = <class 'function'>, size = 136, object = <function my_func at 0x00000235189C8AE8>
#
"""
Вариант 2
"""


#  type = <class 'dict'>, size = 240, object = {'num_list': [-1, -19, 0, -10, -5, -12, -12, -3, -6, -1, -7, -17, -13, -6, -12, -14, -5, -11, -20, -12], 'min_el': -1, 'i': 0, 'item': -1, 'min_idx': 0}
# 	 type = <class 'tuple'>, size = 64, object = ('num_list', [-1, -19, 0, -10, -5, -12, -12, -3, -6, -1, -7, -17, -13, -6, -12, -14, -5, -11, -20, -12])
# 		 type = <class 'str'>, size = 57, object = num_list
# 		 type = <class 'list'>, size = 264, object = [-1, -19, 0, -10, -5, -12, -12, -3, -6, -1, -7, -17, -13, -6, -12, -14, -5, -11, -20, -12]
# 			 type = <class 'int'>, size = 28, object = -1
# 			 type = <class 'int'>, size = 28, object = -19
# 			 type = <class 'int'>, size = 24, object = 0
# 			 type = <class 'int'>, size = 28, object = -10
# 			 type = <class 'int'>, size = 28, object = -5
# 			 type = <class 'int'>, size = 28, object = -12
# 			 type = <class 'int'>, size = 28, object = -12
# 			 type = <class 'int'>, size = 28, object = -3
# 			 type = <class 'int'>, size = 28, object = -6
# 			 type = <class 'int'>, size = 28, object = -1
# 			 type = <class 'int'>, size = 28, object = -7
# 			 type = <class 'int'>, size = 28, object = -17
# 			 type = <class 'int'>, size = 28, object = -13
# 			 type = <class 'int'>, size = 28, object = -6
# 			 type = <class 'int'>, size = 28, object = -12
# 			 type = <class 'int'>, size = 28, object = -14
# 			 type = <class 'int'>, size = 28, object = -5
# 			 type = <class 'int'>, size = 28, object = -11
# 			 type = <class 'int'>, size = 28, object = -20
# 			 type = <class 'int'>, size = 28, object = -12
# 	 type = <class 'tuple'>, size = 64, object = ('min_el', -1)
# 		 type = <class 'str'>, size = 55, object = min_el
# 		 type = <class 'int'>, size = 28, object = -1
# 	 type = <class 'tuple'>, size = 64, object = ('i', 0)
# 		 type = <class 'str'>, size = 50, object = i
# 		 type = <class 'int'>, size = 24, object = 0
# 	 type = <class 'tuple'>, size = 64, object = ('item', -1)
# 		 type = <class 'str'>, size = 53, object = item
# 		 type = <class 'int'>, size = 28, object = -1
# 	 type = <class 'tuple'>, size = 64, object = ('min_idx', 0)
# 		 type = <class 'str'>, size = 56, object = min_idx
# 		 type = <class 'int'>, size = 24, object = 0


# Задание 9 урок 2
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
def max_d_sum(num):
    max_sum = 0
    for i in num:
        digit_sum = 0
        n = i
        while i % 10 != 0 or i // 10 != 0:
            digit_sum += i % 10
            i //= 10
        if digit_sum > max_sum:
            max_sum = digit_sum
            max_num = n
    print(f'У числа {max_num} наибольшая сумма цифр = {max_sum}')
    return locals()


# type = <class 'dict'>, size = 368, object = {'num': [2708, 6801, 6546, 5467, 6762, 3162, 8831, 7466, 3648, 3355, 7340,
#                                                      5771, 8024, 1832, 4685, 4226, 1731, 7247, 3441, 8191],
#                                              'max_sum': 23, 'i': 0, 'digit_sum': 19, 'n': 8191, 'max_num': 7466}
# 	 type = <class 'tuple'>, size = 64, object = ('num', [2708, 6801, 6546, 5467, 6762, 3162, 8831, 7466, 3648, 3355,
#                                                        7340, 5771, 8024, 1832, 4685, 4226, 1731, 7247, 3441, 8191])
# 		 type = <class 'str'>, size = 52, object = num
# 		 type = <class 'list'>, size = 264, object = [2708, 6801, 6546, 5467, 6762, 3162, 8831, 7466, 3648, 3355, 7340,
#                                                     5771, 8024, 1832, 4685, 4226, 1731, 7247, 3441, 8191]
# 			 type = <class 'int'>, size = 28, object = 2708
# 			 type = <class 'int'>, size = 28, object = 6801
# 			 type = <class 'int'>, size = 28, object = 6546
# 			 type = <class 'int'>, size = 28, object = 5467
# 			 type = <class 'int'>, size = 28, object = 6762
# 			 type = <class 'int'>, size = 28, object = 3162
# 			 type = <class 'int'>, size = 28, object = 8831
# 			 type = <class 'int'>, size = 28, object = 7466
# 			 type = <class 'int'>, size = 28, object = 3648
# 			 type = <class 'int'>, size = 28, object = 3355
# 			 type = <class 'int'>, size = 28, object = 7340
# 			 type = <class 'int'>, size = 28, object = 5771
# 			 type = <class 'int'>, size = 28, object = 8024
# 			 type = <class 'int'>, size = 28, object = 1832
# 			 type = <class 'int'>, size = 28, object = 4685
# 			 type = <class 'int'>, size = 28, object = 4226
# 			 type = <class 'int'>, size = 28, object = 1731
# 			 type = <class 'int'>, size = 28, object = 7247
# 			 type = <class 'int'>, size = 28, object = 3441
# 			 type = <class 'int'>, size = 28, object = 8191
# 	 type = <class 'tuple'>, size = 64, object = ('max_sum', 23)
# 		 type = <class 'str'>, size = 56, object = max_sum
# 		 type = <class 'int'>, size = 28, object = 23
# 	 type = <class 'tuple'>, size = 64, object = ('i', 0)
# 		 type = <class 'str'>, size = 50, object = i
# 		 type = <class 'int'>, size = 24, object = 0
# 	 type = <class 'tuple'>, size = 64, object = ('digit_sum', 19)
# 		 type = <class 'str'>, size = 58, object = digit_sum
# 		 type = <class 'int'>, size = 28, object = 19
# 	 type = <class 'tuple'>, size = 64, object = ('n', 8191)
# 		 type = <class 'str'>, size = 50, object = n
# 		 type = <class 'int'>, size = 28, object = 8191
# 	 type = <class 'tuple'>, size = 64, object = ('max_num', 7466)
# 		 type = <class 'str'>, size = 56, object = max_num
# 		 type = <class 'int'>, size = 28, object = 7466


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
    return locals()


# type = <class 'dict'>, size = 368, object = {'matrix': [[1, 2, 7], [4, 1, 5], [5, 6, 3]],
#                                               'i': 2, 'line': [5, 6, 3], 'min_line': [1, 1, 3],
#                                                'idx': 2, 'item': 3, 'max_min': 3}
#  type = <class 'tuple'>, size = 64, object = ('matrix', [[1, 2, 7], [4, 1, 5], [5, 6, 3]])
# 	 type = <class 'str'>, size = 55, object = matrix
# 	 type = <class 'list'>, size = 88, object = [[1, 2, 7], [4, 1, 5], [5, 6, 3]]
# 		 type = <class 'list'>, size = 88, object = [1, 2, 7]
# 			 type = <class 'int'>, size = 28, object = 1
# 			 type = <class 'int'>, size = 28, object = 2
# 			 type = <class 'int'>, size = 28, object = 7
# 		 type = <class 'list'>, size = 88, object = [4, 1, 5]
# 			 type = <class 'int'>, size = 28, object = 4
# 			 type = <class 'int'>, size = 28, object = 1
# 			 type = <class 'int'>, size = 28, object = 5
# 		 type = <class 'list'>, size = 88, object = [5, 6, 3]
# 			 type = <class 'int'>, size = 28, object = 5
# 			 type = <class 'int'>, size = 28, object = 6
# 			 type = <class 'int'>, size = 28, object = 3
#  type = <class 'tuple'>, size = 64, object = ('i', 2)
# 	 type = <class 'str'>, size = 50, object = i
# 	 type = <class 'int'>, size = 28, object = 2
#  type = <class 'tuple'>, size = 64, object = ('line', [5, 6, 3])
# 	 type = <class 'str'>, size = 53, object = line
# 	 type = <class 'list'>, size = 88, object = [5, 6, 3]
# 		 type = <class 'int'>, size = 28, object = 5
# 		 type = <class 'int'>, size = 28, object = 6
# 		 type = <class 'int'>, size = 28, object = 3
#  type = <class 'tuple'>, size = 64, object = ('min_line', [1, 1, 3])
# 	 type = <class 'str'>, size = 57, object = min_line
# 	 type = <class 'list'>, size = 88, object = [1, 1, 3]
# 		 type = <class 'int'>, size = 28, object = 1
# 		 type = <class 'int'>, size = 28, object = 1
# 		 type = <class 'int'>, size = 28, object = 3
#  type = <class 'tuple'>, size = 64, object = ('idx', 2)
# 	 type = <class 'str'>, size = 52, object = idx
# 	 type = <class 'int'>, size = 28, object = 2
#  type = <class 'tuple'>, size = 64, object = ('item', 3)
# 	 type = <class 'str'>, size = 53, object = item
# 	 type = <class 'int'>, size = 28, object = 3
#  type = <class 'tuple'>, size = 64, object = ('max_min', 3)
# 	 type = <class 'str'>, size = 56, object = max_min
# 	 type = <class 'int'>, size = 28, object = 3


lst = [random.randint(-20, 0) for _ in range(20)]
# show_size(my_decor(my_func, lst))
# show_size(my_func(lst))
lst2 = [random.randint(1000, 9999) for _ in range(20)]
# show_size(max_d_sum(lst2))
matrix = [[1, 2, 7], [4, 1, 5], [5, 6, 3]]
# show_size(matrix_func(matrix))

"""
Понятно, что количество потребляемой памяти в первую очередь зависит от объема входных данных, но кроме этого на память
влияют и количество и тип используемых переменных. Сами же переменные судя по всему представляют собой кортеж(???)*
из имени переменной и её значения.

* Не нашел конкретную информацию по этому вопросу. Если это так, то не совсем понятно, как происходит переприсваивание
значений для переменных. Расскажите, пожалуйста, на уроке, как именно хранится имя и значение внутри python.
"""
