# 2. Посчитать четные и нечетные цифры введенного натурального числа.

number = input('Введите целое число: ')
odd = 0
even = 0
for num in number:
    if int(num) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'В числе {number}: {odd} нечетных и {even} четных цифр')