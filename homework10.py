def to_fill_file(file_n, input_list):
    n_row = 1
    for elem in input_list:
        if n_row == 10:
            file_n.write(str(elem) + ' ' + '\n')
            n_row = 1
        else:
            file_n.write(str(elem) + ' ')
            n_row += 1


############ 1
# Напишите функцию для создания файла и записи в него случайных чисел,
# каждое число записывается в файл через пробел,
# но не больше 10ти чисел в строку.
# Всего случайных чисел должно быть 1000


print('Task 1:')


def to_generate_list(max_value, count_elements):
    import random
    my_lst = []
    for i in range(count_elements):
        my_lst.append(random.randint(0, max_value))
    return my_lst


def to_create_file_from_list(file_name, input_list):
    new_file = open(file_name, 'wt')
    to_fill_file(new_file, input_list)
    new_file.close()


def unit_test_to_fun(file_name):
    result_list = []
    n_file = open(file_name, 'r+')
    for line in n_file:
        result_list += list(map(int, (line.strip().split(' '))))
    return result_list


new_file_name = 'result_file.txt'
unit_test_file = 'unit_test_result.txt'

to_create_file_from_list(new_file_name, to_generate_list(100, 1000))
print(f"Created file : {new_file_name}", end="")

print('\n ')
print('Unit tests:')
input_list = [2, 3, 4]
expected_list = [2, 3, 4]
print(f"Input list = {input_list}", end="")
print(f"; Expected list = {expected_list}", end="")
to_create_file_from_list(unit_test_file, input_list)
print("; Actual list = ", unit_test_to_fun(unit_test_file), " => ",
      expected_list == unit_test_to_fun(unit_test_file))

input_list = [10, 30, 4, 0, 100]
expected_list = [10, 30, 4, 0, 100]
print(f"Input list = {input_list}", end="")
print(f"; Expected list = {expected_list}", end="")
to_create_file_from_list(unit_test_file, input_list)
print("; Actual list = ", unit_test_to_fun(unit_test_file), " => ",
      expected_list == unit_test_to_fun(unit_test_file))

input_list = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]
expected_list = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(f"Input list = {input_list}", end="")
print(f"; Expected list = {expected_list}", end="")
to_create_file_from_list(unit_test_file, input_list)
print("; Actual list = ", unit_test_to_fun(unit_test_file), " => ",
      expected_list == unit_test_to_fun(unit_test_file))

input_list = [10, 200, 30, 0, 0, 13]
expected_list = [10, 200, 30, 0, 0, 13]
print(f"Input list = {input_list}", end="")
print(f"; Expected list = {expected_list}", end="")
to_create_file_from_list(unit_test_file, input_list)
print("; Actual list = ", unit_test_to_fun(unit_test_file), " => ",
      expected_list == unit_test_to_fun(unit_test_file))

input_list = [-10, -2, 30, -10, 10, 5]
expected_list = [-10, -2, 30, -10, 10, 5]
print(f"Input list = {input_list}", end="")
print(f"; Expected list = {expected_list}", end="")
to_create_file_from_list(unit_test_file, input_list)
print("; Actual list = ", unit_test_to_fun(unit_test_file), " => ",
      expected_list == unit_test_to_fun(unit_test_file))

############# 2
# Напишите другую функцию, которая считывает первый файл
# и возводит каждое число в квадрат.
# Каждое полученное число должно быть дозаписано в исходный файл в таком же формате.
print('\n ')
print('Task 2:')


def to_add_data_to_file(file_name):
    add_list = []
    n_file = open(file_name, 'r+')
    for line in n_file:
        add_list += list(map((lambda x: x ** 2), list(map(int, (line.strip().split(' '))))))
    to_fill_file(n_file, add_list)
    n_file.close()


to_add_data_to_file(new_file_name)
print(f"New calculated data added to file : {new_file_name}")

print('\n ')
print('Unit tests:')
input_list = [2, 3, 4]
expected_list = [2, 3, 4, 4, 9, 16]
print(f"Input list = {input_list}", end="")
print(f"; Expected list = {expected_list}", end="")
to_create_file_from_list(unit_test_file, input_list)
to_add_data_to_file(unit_test_file)
print("; Actual list = ", unit_test_to_fun(unit_test_file), " => ",
      expected_list == unit_test_to_fun(unit_test_file))

input_list = [10, 30, 4, 0, 100]
expected_list = [10, 30, 4, 0, 100, 100, 900, 16, 0, 10000]
print(f"Input list = {input_list}", end="")
print(f"; Expected list = {expected_list}", end="")
to_create_file_from_list(unit_test_file, input_list)
to_add_data_to_file(unit_test_file)
print("; Actual list = ", unit_test_to_fun(unit_test_file), " => ",
      expected_list == unit_test_to_fun(unit_test_file))

input_list = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]
expected_list = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 9, 4, 16, 25, 36, 49, 64, 81, 100, 121, 144]
print(f"Input list = {input_list}", end="")
print(f"; Expected list = {expected_list}", end="")
to_create_file_from_list(unit_test_file, input_list)
to_add_data_to_file(unit_test_file)
print("; Actual list = ", unit_test_to_fun(unit_test_file), " => ",
      expected_list == unit_test_to_fun(unit_test_file))

input_list = [10, 200, 30, 0, 0, 13]
expected_list = [10, 200, 30, 0, 0, 13, 100, 40000, 900, 0, 0, 169]
print(f"Input list = {input_list}", end="")
print(f"; Expected list = {expected_list}", end="")
to_create_file_from_list(unit_test_file, input_list)
to_add_data_to_file(unit_test_file)
print("; Actual list = ", unit_test_to_fun(unit_test_file), " => ",
      expected_list == unit_test_to_fun(unit_test_file))

input_list = [-10, -2, 30, -10, 10, 5]
expected_list = [-10, -2, 30, -10, 10, 5, 100, 4, 900, 100, 100, 25]
print(f"Input list = {input_list}", end="")
print(f"; Expected list = {expected_list}", end="")
to_create_file_from_list(unit_test_file, input_list)
to_add_data_to_file(unit_test_file)
print("; Actual list = ", unit_test_to_fun(unit_test_file), " => ",
      expected_list == unit_test_to_fun(unit_test_file))