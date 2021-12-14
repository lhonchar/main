############ 1
# программа, которая прочитает файл numbers.txt и найдет число, которое встречается чаще всего
print('Task 1:')


def to_analyse_file(file_name):
    a_list = []
    n_file = open(file_name, 'r+')
    for line in n_file:
        a_list += map(int, (line.strip()))
    print('values : ', a_list)
    n_file.close()
    calc = dict((x, a_list.count(x)) for x in set(a_list))
    return max(calc, key=calc.get)


my_file_name = 'number.txt'

print(f"Opened file {my_file_name}")
print('The most common value :', to_analyse_file(my_file_name))
