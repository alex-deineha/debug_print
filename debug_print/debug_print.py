import traceback
import builtins as __builtin__
from huepy import *


def get_inner_call_expression(code):
    return code[code.find('(') + 1:-1]


def get_expressions():
    stack = traceback.extract_stack()
    filename, lineno, function_name, code = stack[-3]
    inner_call_expression = get_inner_call_expression(code)
    expressions = get_elements(inner_call_expression)
    return expressions


def get_close_indexes_of_elements(str):
    close_indexes = []
    count = 0
    for i in range(len(str)):
        if str[i] in ['(', '[', '\"', "\'"]:
            count += 1
        elif str[i] in [')', ']', '\"', "\'"]:
            count -= 1
        if str[i] == ',' and count == 0:
            close_indexes.append(i)
    close_indexes.append(len(str))
    return close_indexes


def get_elements(str):
    close_indexes = get_close_indexes_of_elements(str)
    elements = []
    open_index = 0
    for close_index in close_indexes:
        elements.append(str[open_index:close_index].strip())
        open_index = close_index + 1
    return elements


def format_simple(expression, value):
    return good('') + grey(f'{expression}=') + blue(value)


def debug_print(*values):
    expressions = get_expressions()
    res = [format_simple(expression, value) for expression, value in zip(expressions, values)]
    __builtin__.print(' '.join(res))


def format_with_type(expression, value):
    return good('') + grey(f'{expression}') + \
           lcyan(f'({ str(type(value))[8:-2]})') \
           + grey('=') + blue(value)


def debug_print_with_type(*values):
    expressions = get_expressions()
    res = [format_with_type(expression, value) for expression, value in zip(expressions, values)]
    __builtin__.print(' '.join(res))
