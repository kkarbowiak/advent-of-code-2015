import re


def get_row_column_from_line(line):
    m = re.match('.*row ([0-9]+).*column ([0-9]+)', line)
    return int(m.group(1)), int(m.group(2))


def get_ith_code(initial, ith):
    result = initial

    i = 1
    while i < ith:
        result *= 252533
        result %= 33554393
        i += 1

    return result


def day25_1():
    row = 0
    col = 0
    with open('data/25') as data:
        row, col = get_row_column_from_line(data.readline())

    index = sum(range(1, row + col - 1)) + col
    code = get_ith_code(20151125, index)

    print('code =', code)


day25_1()
