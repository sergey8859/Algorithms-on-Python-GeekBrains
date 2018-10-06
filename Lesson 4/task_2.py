# Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.
import cProfile


# n = int(input('Какое по счету простое число вы хотите найти: '))
# lst = [i for i in range(n * n)]


# Вариант 1. Решето Эратосфена.


def sieve(num_list, idx):
    num_list[1] = 0
    i = 2
    s_num_list = []
    while len(s_num_list) < idx:
        if num_list[i] != 0:
            s_num_list.append(num_list[i])
            j = i * 2
            while j < len(num_list):
                num_list[j] = 0
                j += i
        i += 1
    return s_num_list[-1]


#                                                   номер простого числа
# 100 loops, best of 5: 19 usec per loop                    3
# 100 loops, best of 5: 1.04 msec per loop                  10
# 100 loops, best of 5: 33.4 msec per loop                  30
# 100 loops, best of 5: 1.51 sec per loop                   100

# y = 10
# x = [i for i in range(y * y)]
# cProfile.run('sieve(x, y)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_2.py:12(sieve)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       177    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вариант 2. Перебор.

def simple_num(num_list, idx):
    num_list[1] = 0
    s_nums = []
    for i in range(2, len(num_list)):
        for num in s_nums:
            if num_list[i] % num == 0:
                break
        else:
            s_nums.append(num_list[i])
        if len(s_nums) == idx:
            return s_nums[-1]


# 100 loops, best of 5: 8.15 usec per loop                  3
# 100 loops, best of 5: 43.6 usec per loop                  10
# 100 loops, best of 5: 251 usec per loop                   30
# 100 loops, best of 5: 2.12 msec per loop                  100
# 100 loops, best of 5: 8.07 msec per loop                  200

# y = 10
# x = [i for i in range(y * y)]
# cProfile.run('simple_num(x, y)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_2.py:48(simple_num)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        29    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Сложность 1го алгоритма (Эратосфен) = O(n**2)    y = 0,2058x**2 - 5,7299x + 24,481
# Достоверность апроксимации R**2 = 0,998
# Сложность 2го алгоритма (Перебор)  = O(n**2)     y = 0,1912x**2 + 2,0725x + 5,5545
# Достоверность апроксимации R**2 = 1
# Сложность алгоритмов объясняется вложенностью циклов.
# Несмотря на то, что сложность у обоих алгоритмов = O(n**2), очень заметна разница в скорости.
# Я даже не рискнул запускать 200 на решете.
# Видимо такая существенная разница объясняется коэффициентами при n.
# В cProfile видно значительную разницу в количестве вызовов метода len. Возможно из-за этого такая разница
# Проверим в фукнции sieve2


def sieve2(num_list, idx):
    num_list[1] = 0
    i = 2
    s_num_list = []
    length = 0
    length_num_list = len(num_list)
    while length < idx:
        if num_list[i] != 0:
            s_num_list.append(num_list[i])
            length += 1
            j = i * 2
            while j < length_num_list:
                num_list[j] = 0
                j += i
        i += 1
    return s_num_list[-1]


# y = 10
# x = [i for i in range(y * y)]
# cProfile.run('sieve2(x, y)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task_2.py:91(sieve2)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#   100 loops, best of 5: 14.5 usec per loop        3
#   100 loops, best of 5: 607 usec per loop         10
#   100 loops, best of 5: 20.4 msec per loop        30
#   100 loops, best of 5: 985 msec per loop         100

#   Отказ от использования одной функции добавил примерно 1.5-кратный прирост производительности, но решето
#   все также проигрывает.
#   При этом его сложность должна остаться прежней.
