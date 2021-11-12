####### 1
# интерактивный калькулятор.
# Предполагается, что пользовательский ввод представляет собой формулу, состоящую из
# числа, оператора (как минимум + и -) и другого числа, разделенных
# пробелом (например, 1 + 1). Используйте str.split ()
# a. Если входные данные не состоят из 3 элементов, генерируйте эксепшн FormulaError.
# b. Попробуйте преобразовать первый и третий элемент в float ( float_value =
# float(str_value)). Поймайте любую возникающую ValueError и сгенерируйте вместо него
# FormulaError
# c. Если второй элемент не является «+» или «-», киньте эксепшн FormulaError

print('Task 1:')


class FormulaError(Exception):
    def __init__(self, message='Must be a number', *args, **kwargs): # признаюсь это списала у Артема ))
        super().__init__(message, *args, **kwargs)
    pass


def fn_calc(operator, x, y):
    if operator == '+':
        return float(x) + float(y)
    elif operator == '-':
        return float(x) - float(y)
    elif operator == '*':
        return float(x) * float(y)


def my_calc(input_str):
    input_lst = str.split(input_str)
    try:
        if len(input_lst) != 3:
            raise FormulaError("FormulaError: Not enough arguments!")
        if input_lst[1] not in ('+', '-', '*'):
            raise FormulaError("FormulaError: Unknown arithmetic operator - " + str(input_lst[1]))

        return fn_calc(input_lst[1], input_lst[0], input_lst[2])

    except ValueError as v_err:
        # raise FormulaError()
        print("FormulaError: ValueError! {0}".format(v_err))

    except FormulaError as exp_string:
        print(exp_string)


if __name__ == '__main__':
    result_list = input('Enter a formula (number, operator, another number, separated by a space) : ')
    print(f"Result = {my_calc(result_list)}", end="")




