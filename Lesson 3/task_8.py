# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

matrix = [[] for _ in range(4)]

for line in matrix:
    line_sum = 0
    for i in range(4):
        num = int(input('Введите значение: '))
        line.append(num)
        line_sum += num
    line.append(line_sum)

for line in matrix:
    for num in line:
        print(f'\t{num:>5}', end='')
    print()
