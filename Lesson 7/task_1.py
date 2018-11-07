# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.
import random


def buble_sort(array, reverse=False):
    if reverse:
        left = 1
        right = 0
    else:
        left = 0
        right = 1
    n = 1
    length = len(array)
    while n < length:
        count = True
        for i in range(n - 1, length - n):
            if array[i + left] > array[i + right]:
                array[i], array[i + 1] = array[i + 1], array[i]
                count = False
        if count:
            break
        for j in range(length - n, n - 1, -1):
            if array[j - left] < array[j - right]:
                array[j], array[j - 1] = array[j - 1], array[j]
        n += 1


lst = [random.randint(-100, 99) for _ in range(10)]
random.shuffle(lst)
print(f'Список до сортировки:\n{lst}')
buble_sort(lst, reverse=True)
print(f'Список после сортировки:\n{lst}')
