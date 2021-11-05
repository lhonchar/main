######## 1
# дебагер, найдите и исправьте ошибку.
# def buble_sort(l):
#     t = l.copy()
#     for n in range(0, len(t)):
#         for i in range(len(t)-n):
#             if t[i] > t[n]:
#                 t[i], t[n] = t[n], t[i]
#     return t

print('Task 1:')


def buble_sort(l):
    t = l.copy()
    for n in range(len(t) - 1):
        for i in range(0, len(t) - n - 1):
            if t[i] > t[i + 1]:
                t[i], t[i + 1] = t[i + 1], t[i]
    return t


nums = [4, 1, 6, 3, 2, 7, 8]
print("Input list = ", nums)
print("Sorted list =", buble_sort(nums))

print('\n ')
print('Unit tests:')
print("Original list = [4, 1, 6, 3, 8];  Sorted list = [1, 3, 4, 6, 8] => ", [1, 3, 4, 6, 8] ==
      buble_sort([4, 1, 6, 3, 8]))
print("Original list = [10, -1, 30];  Sorted list = [-1, 10, 30] => ", [-1, 10, 30] == buble_sort([10, -1, 30]))
print("Original list = [2, 0, 100];  Sorted list = [0, 2, 100] => ", [0, 2, 100] == buble_sort([2, 0, 100]))
print("Original list = [-20, -1, -30, 0];  Sorted list = [-30, -20, -1, 0] => ",
      [-30, -20, -1, 0] == buble_sort([-20, -1, -30, 0]))
print("Original list = [9, 0, 5, 6, 1, 10];  Sorted list = [0, 1, 5, 6, 9, 10] => ", [0, 1, 5, 6, 9, 10] ==
      buble_sort([9, 0, 5, 6, 1, 10]))

######## 2
# Представьте себе бухгалтерскую книгу в книжном магазине. В этой книге хранятся записи о номере заказа,
# названии книги, количестве и стоимости одной книги, как представлено ниже, в таблице.
# Напишите программу на Python, которая на вход получает список списков:
# [
# [34587, 'Learning Python, Mark Lutz', 4, 40.95],
# [98762, 'Programming Python, Mark Lutz', 5, 56.80],
# [77226, 'Head First Python, Paul Barry', 3, 32.95],
# [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
# ]
# и возвращает список кортежей. Каждый кортеж состоит из номера заказа и произведения цены на товары и
# количества. Стоимость товара должна быть увеличена на $10, если стоимость заказа меньше $100.
# Программа должна использовать lambda и map.

print('Task 2:')

import_list = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

print("Input list:")
print(import_list)


def fn_calculate(action, x, y):
    return action(x, y)


main_list = []
for i in range(len(import_list)):
    tmp_lst = [import_list[i][0],
               round(fn_calculate(lambda x, y: x * y + 10 if x * y < 100 else x * y, import_list[i][2],
                                  import_list[i][3]), 2)]
    main_list.append(tuple(tmp_lst))
print('\n ')
print(f"Result list = {main_list}")

############# 3
# Добавьте к исходному списку еще несколько товаров
print('\n ')

print('Task 3:')

add_list = [
    [24387, ' на русском', 2, 4.59],
    [18762, 'The C Programming Language (2nd Edition)', 12, 78.80],
    [87236, "C Programming Absolute Beginner's Guide", 1, 23.55],
    [58132, 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14', 9, 42.89]
]

print("Additional list:")
print(add_list)
full_list = import_list + add_list
print("Full list with addition:")
print(full_list)


############# 4
# Отсортируйте получившийся список по стоимости и выведите его на экран.
# *Используйте lambda
print('\n ')

print('Task 4:')

print(f"Sorted list with addition by Price = {sorted(full_list, key=lambda x: x[3])}")

############# 5
# Используя filter() оставьте только книги, количество которых больше 5ти.

print('\n ')

print('Task 5:')


def func_condition(lst):
    if lst[2] > 5:
        return 1
    else:
        return 0


b = filter(func_condition, full_list)
print(f"Filtered list with addition Where Book Count > 5 = {list(b)}")