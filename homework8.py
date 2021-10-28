########## 3
#  Дано натуральное число N. Вычислите сумму его цифр
print('Task 3:')


def sum_numbers(n):
    return abs(n) % 10 + sum_numbers(abs(n) // 10) if abs(n) > 9 else abs(n)


number = input('Input number: ')
print(f"Sum of all digits of number: {sum_numbers(int(number))}")
print('Unit tests:')
print("sum_digits(256) == 13 ->", 13 == sum_numbers(256))
print("sum_digits(56)  == 11 ->", 11 == sum_numbers(56))
print("sum_digits(6)   == 6  ->", 6 == sum_numbers(6))
print("sum_digits(0)   == 0  ->", 0 == sum_numbers(0))
print("sum_digits(-2598) == 24  ->", 24 == sum_numbers(2598))

########## 4
#  Рекурсивная функцию для вычисления числа Фибоначи

print('Task 4:')


def fibonacci(n):
    if n == 0:
        return 0
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def array_fibonacci(n):
    fib1 = 0
    fib2 = 1
    if n == 0:
        print(0, end=' ')
    else:
        print(fib1, fib2, end=' ')
    for i in range(1, n):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')


el_num = input("Input number : ")
print(f"Result in Fibonacci : {fibonacci(int(el_num))}")
print('Array Fibonacci : ')
array_fibonacci(int(el_num))
print('\n ')
print('Unit tests:')
print("fibonacci(10) == 55 ->", 55 == fibonacci(10))
print("fibonacci(1)  == 1 ->", 1 == fibonacci(1))
print("fibonacci(6)   == 8  ->", 8 == fibonacci(6))
print("fibonacci(0)   == 0  ->", 0 == fibonacci(0))
print("fibonacci(11) == 89  ->", 89 == fibonacci(11))

######### 5
# функция для умножения всех чисел в списке. Рекурсивно
print('Task 5:')

import random

MAX_VALUE = 10
count_elements = 5
my_lst = []
for i in range(count_elements):
    my_lst.append(random.randint(0, MAX_VALUE))


def multiply_lst(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        index = len(lst) - 1
        return lst[index] * multiply_lst(lst[0:index])


print(f"my_list = {my_lst}")
print(f"Result: Multiply all elements of list = {multiply_lst(my_lst)}")
print('\n ')
print('Unit tests:')
print("Multiply all elements of list[1, 2] == 2 ->", 2 == multiply_lst([1, 2]))
print("Multiply all elements of list[1, 2, 0] == 0 ->", 0 == multiply_lst([1, 2, 0]))
print("Multiply all elements of list[0] == 0 ->", 0 == multiply_lst([0]))
print("Multiply all elements of list[-1, 2, 5, 2] == -20 ->", -20 == multiply_lst([-1, 2, 5, 2]))
print("Multiply all elements of list[100, 20] == 200 ->", 2000 == multiply_lst([100, 20]))

######## 6
# Дано натуральное число N.
# Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#  например: 8 - YES, 3 - NO
print('Task 6:')


def check_pow(result):
    n = 1
    while 2 ** n < result:
        n = n + 1
    return 'YES' if 2 ** n == result else 'NO'


number = input('Input number: ')
print(f"Result: Number is an exact power of two? :  {check_pow(int(number))}")
print('\n ')
print('Unit tests:')
print("2 is an exact power of two? :  == YES ->", 'YES' == check_pow(2))
print("8 is an exact power of two? :  == YES ->", 'YES' == check_pow(8))
print("3 is an exact power of two? :  == NO ->", 'NO' == check_pow(3))
print("1 is an exact power of two? :  == NO ->", 'NO' == check_pow(1))
print("16 is an exact power of two? :  == YES ->", 'YES' == check_pow(16))


####### 7
# inner функцию для вычисления сложения следующим образом:
# Создайте внешнюю функцию, которая будет принимать два параметра, a и b
# Создайте внутреннюю функцию внутри внешней функции, которая будет вычислять сложение a и b
# Наконец, внешняя функция добавит 5 и вернет ее
print('Task 7:')


def join_fun(a, b):
    return internal_fun(a, b) + 5


def internal_fun(a, b):
    return a + b


v1 = input('Input number a: ')
v2 = input('Input number b: ')
print(f"Result: a + b + 5 = {join_fun(int(v1), int(v2))}")
print('\n ')
print('Unit tests:')
print("(5 + 6) + 5  :  == 16 ->", 16 == join_fun(5, 6))
print("(10 + 20) + 5  :  == 35 ->", 35 == join_fun(10, 20))
print("(0 + 6) + 5  :  == 11 ->", 11 == join_fun(0, 6))
print("(100 + 6) + 5  :  == 111 ->", 111 == join_fun(100, 6))
print("(-5 + (-6)) + 5  :  == -6 ->", -6 == join_fun(-5, -6))


