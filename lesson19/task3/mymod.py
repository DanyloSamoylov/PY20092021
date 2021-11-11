import sys


def count_lines(file):
    with open(file, 'r') as f:
        result = len(f.readlines())
        return result


def count_chars(file):
    with open(file, 'r') as f:
        result = f.read().replace(' ', '')
        ch = 0
        for _ in result:
            ch += 1
        return ch


def test(file):
    try:
        lines = count_lines(file)
        chars = count_chars(file)
        return f'{lines} lines, {chars} chars in {file}'
    except IndentationError:
        print('something wrong')


# print(count_lines('text.txt'))
# print(count_chars('text.txt'))
# print(test('text.txt'))
