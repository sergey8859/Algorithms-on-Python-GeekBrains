# 1. Определение количества различных подстрок с использованием хеш-функции.
import hashlib


def all_substr(s):
    h_lst = []
    s_lst = []

    for len_sub in range(1, len(s)):
        for i in range(len(s) - len_sub + 1):
            h_sub = hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest()
            if h_sub not in h_lst:
                h_lst.append(h_sub)
                s_lst.append(s[i:i + len_sub])

    if len(s_lst) > 0:
        return f'В строке "{s}" найдено {len(s_lst)} уникальных подстрок: \n{s_lst}'
    return 'Пустая строка'


s = input('Введите строку: ')
print(all_substr(s))
