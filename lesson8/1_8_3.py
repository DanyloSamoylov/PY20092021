

def make_operation(operator_, *args):
    argument_str = ''.join(str(el) + '.' for el in args)
    answer = argument_str.replace('.', operator_)
    print('выражение будет:', eval(answer[:-1]))


make_operation('+', 7, 7, 2)
make_operation('-', 5, 5, -10, -20)
make_operation('*', 7, 6)
